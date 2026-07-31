import yfinance as yf

# Get Apple stock data
aapl = yf.Ticker("AAPL")

# Pull 1 year of daily prices
data = aapl.history(period="1y")

# Print the first 5 rows
print("First 5 days:")
print(data.head())

print("\nLast 5 days:")
print(data.tail())