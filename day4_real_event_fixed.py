import yfinance as yf

# Pull 2 years of Apple prices
aapl = yf.Ticker("AAPL")
prices = aapl.history(period="2y")

# Make dates easier to work with
prices['Simple_Date'] = prices.index.strftime('%Y-%m-%d')

# Use a date that exists in your data: July 30, 2024
earnings_date = '2024-07-30'

# Find that date in the price data
target = prices[prices['Simple_Date'] == earnings_date]

if not target.empty:
    # Get the INTEGER POSITION (row number), not the date label
    idx = prices.index.get_loc(target.index[0])
    
    # Get prices using .iloc (integer position)
    price_before = prices.iloc[idx - 1]['Close']
    price_day_of = prices.iloc[idx]['Close']
    price_after = prices.iloc[idx + 3]['Close']
    
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