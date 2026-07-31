import yfinance as yf
import pandas as pd

# Earnings dates for each company
# These are approximate — verify on Google if you want exact precision
earnings_calendar = {
    'AAPL': ['2024-07-30', '2024-10-31', '2025-01-30', '2025-04-24', '2025-07-29'],
    'MSFT': ['2024-07-30', '2024-10-24', '2025-01-29', '2025-04-24', '2025-07-29'],
    'TSLA': ['2024-10-23', '2025-01-29', '2025-04-22', '2025-07-23'],
    'AMZN': ['2024-07-30', '2024-10-31', '2025-01-30', '2025-04-24', '2025-07-31'],
}

all_results = []

for ticker, dates in earnings_calendar.items():
    print(f"\nProcessing {ticker}...")
    
    # Pull prices for this ticker
    stock = yf.Ticker(ticker)
    prices = stock.history(period="2y")
    prices['Simple_Date'] = prices.index.strftime('%Y-%m-%d')
    
    for date in dates:
        target = prices[prices['Simple_Date'] == date]
        
        if not target.empty:
            idx = prices.index.get_loc(target.index[0])
            
            # Check we have enough data around the date
            if idx >= 1 and idx + 3 < len(prices):
                price_before = prices.iloc[idx - 1]['Close']
                price_day_of = prices.iloc[idx]['Close']
                price_after = prices.iloc[idx + 3]['Close']
                
                ret_1d = (price_day_of - price_before) / price_before * 100
                ret_3d = (price_after - price_day_of) / price_day_of * 100
                
                all_results.append({
                    'Ticker': ticker,
                    'Date': date,
                    'Price_Before': round(price_before, 2),
                    'Price_Day_Of': round(price_day_of, 2),
                    'Price_3Days_After': round(price_after, 2),
                    '1D_Return_%': round(ret_1d, 2),
                    '3D_Post_Return_%': round(ret_3d, 2)
                })
                
                print(f"  {date}: 1D={ret_1d:.2f}%, 3D_Post={ret_3d:.2f}%")
            else:
                print(f"  {date}: Not enough price data")
        else:
            print(f"  {date}: Date not found")

# Combine everything into one table
df = pd.DataFrame(all_results)
df.to_csv('multi_company_earnings_returns.csv', index=False)

print(f"\n{'='*50}")
print(f"TOTAL EVENTS COLLECTED: {len(df)}")
print(f"\nBreakdown by company:")
print(df['Ticker'].value_counts())
print(f"\nAverage 1-day return across all events: {df['1D_Return_%'].mean():.2f}%")
print(f"Average 3-day post return across all events: {df['3D_Post_Return_%'].mean():.2f}%")
print(f"\nSaved to multi_company_earnings_returns.csv")