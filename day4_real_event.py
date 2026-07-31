import yfinance as yf
import pandas as pd

# Pull 2 years of Apple prices
aapl = yf.Ticker("AAPL")
prices = aapl.history(period="2y")

# Make dates easier to work with
prices['Simple_Date'] = prices.index.strftime('%Y-%m-%d')

# Apple's earnings date: January 25, 2024
earnings_date = '2024-01-25'

# Find that date in the price data
target = prices[prices['Simple_Date'] == earnings_date]

if not target.empty:
    # Get the position (row number) of that date
    idx = target.index[0]
    
    # Get prices: 1 day before, day of, 3 days after
    price_before = prices.loc[idx - 1, 'Close']
    price_day_of = prices.loc[idx, 'Close']
    price_after = prices.loc[idx + 3, 'Close']
    
    # Calculate returns
    ret_1d = (price_day_of - price_before) / price_before * 100
    ret_3d_after = (price_after - price_day_of) / price_day_of * 100
    
    print(f"Earnings date: {earnings_date}")
    print(f"Price day before: ${price_before:.2f}")
    print(f"Price day of: ${price_day_of:.2f}")
    print(f"Price 3 days after: ${price_after:.2f}")
    print(f"1-day return: {ret_1d:.2f}%")
    print(f"3-day post return: {ret_3d_after:.2f}%")
else:
    print("Date not found in price data")