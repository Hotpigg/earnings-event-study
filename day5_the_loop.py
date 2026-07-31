import yfinance as yf
import pandas as pd

# Pull Apple prices
aapl = yf.Ticker("AAPL")
prices = aapl.history(period="2y")
prices['Simple_Date'] = prices.index.strftime('%Y-%m-%d')

# Apple's earnings dates in your data window
earnings_dates = [
    '2024-07-30',
    '2024-10-31',
    '2025-01-30',
    '2025-04-24',
    '2025-07-29'
]

results = []

for date in earnings_dates:
    target = prices[prices['Simple_Date'] == date]
    
    if not target.empty:
        idx = prices.index.get_loc(target.index[0])
        
        # Make sure we have enough days before and after
        if idx >= 1 and idx + 3 < len(prices):
            price_before = prices.iloc[idx - 1]['Close']
            price_day_of = prices.iloc[idx]['Close']
            price_after = prices.iloc[idx + 3]['Close']
            
            ret_1d = (price_day_of - price_before) / price_before * 100
            ret_3d = (price_after - price_day_of) / price_day_of * 100
            
            results.append({
                'Date': date,
                'Price_Before': round(price_before, 2),
                'Price_Day_Of': round(price_day_of, 2),
                'Price_3Days_After': round(price_after, 2),
                '1D_Return_%': round(ret_1d, 2),
                '3D_Post_Return_%': round(ret_3d, 2)
            })
            
            print(f"{date}: 1D={ret_1d:.2f}%, 3D_Post={ret_3d:.2f}%")
        else:
            print(f"{date}: Not enough price data around this date")
    else:
        print(f"{date}: Date not found in data")

# Save results
df = pd.DataFrame(results)
df.to_csv('aapl_earnings_returns.csv', index=False)
print(f"\nSaved {len(results)} events to aapl_earnings_returns.csv")
print(df)