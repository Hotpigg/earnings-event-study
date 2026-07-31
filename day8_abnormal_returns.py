import yfinance as yf
import pandas as pd

# Load your existing results
df = pd.read_csv('multi_company_earnings_returns.csv')
print("Loaded stock returns:")
print(df.head())
print()

# Pull S&P 500 (SPY ETF) prices for the same period
print("Pulling market data...")
spy = yf.Ticker("SPY")
spy_prices = spy.history(period="2y")
spy_prices['Simple_Date'] = spy_prices.index.strftime('%Y-%m-%d')

# Create dictionaries for fast lookup
spy_1d_before = {}
spy_day_of = {}
spy_3d_after = {}

for i in range(1, len(spy_prices) - 3):
    date = spy_prices.iloc[i]['Simple_Date']
    spy_1d_before[date] = spy_prices.iloc[i - 1]['Close']
    spy_day_of[date] = spy_prices.iloc[i]['Close']
    spy_3d_after[date] = spy_prices.iloc[i + 3]['Close']

# Calculate abnormal returns
abnormal_1d = []
abnormal_3d = []

for _, row in df.iterrows():
    date = row['Date']
    
    if date in spy_day_of:
        # Market returns for same windows
        mkt_ret_1d = (spy_day_of[date] - spy_1d_before[date]) / spy_1d_before[date] * 100
        mkt_ret_3d = (spy_3d_after[date] - spy_day_of[date]) / spy_day_of[date] * 100
        
        # Abnormal return = stock return - market return
        ab_1d = row['1D_Return_%'] - mkt_ret_1d
        ab_3d = row['3D_Post_Return_%'] - mkt_ret_3d
        
        abnormal_1d.append(round(ab_1d, 2))
        abnormal_3d.append(round(ab_3d, 2))
    else:
        abnormal_1d.append(None)
        abnormal_3d.append(None)

df['Mkt_1D_Return_%'] = [round((spy_day_of.get(d, 0) - spy_1d_before.get(d, 0)) / spy_1d_before.get(d, 1) * 100, 2) if d in spy_day_of else None for d in df['Date']]
df['Abnormal_1D_Return_%'] = abnormal_1d
df['Abnormal_3D_Post_Return_%'] = abnormal_3d

# Save enhanced dataset
df.to_csv('multi_company_abnormal_returns.csv', index=False)

print("Enhanced dataset with abnormal returns:")
print(df[['Ticker', 'Date', '1D_Return_%', 'Mkt_1D_Return_%', 'Abnormal_1D_Return_%']])
print()

print(f"Average raw 1-day return: {df['1D_Return_%'].mean():.2f}%")
print(f"Average market 1-day return: {df['Mkt_1D_Return_%'].mean():.2f}%")
print(f"Average abnormal 1-day return: {df['Abnormal_1D_Return_%'].mean():.2f}%")
print()

# Find the biggest outperformance and underperformance
best = df.loc[df['Abnormal_1D_Return_%'].idxmax()]
worst = df.loc[df['Abnormal_1D_Return_%'].idxmin()]

print(f"Best abnormal 1-day return: {best['Ticker']} on {best['Date']} = {best['Abnormal_1D_Return_%']:.2f}%")
print(f"Worst abnormal 1-day return: {worst['Ticker']} on {worst['Date']} = {worst['Abnormal_1D_Return_%']:.2f}%")