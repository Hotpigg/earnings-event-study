import yfinance as yf

aapl = yf.Ticker("AAPL")
prices = aapl.history(period="2y")

print("First 10 dates in the data:")
print(prices.index[:10])

print("\nLast 10 dates in the data:")
print(prices.index[-10:])

# Check if Jan 25, 2024 is there
target_date = "2024-01-25"
dates_list = prices.index.strftime('%Y-%m-%d').tolist()

print(f"\nIs {target_date} in the data? {target_date in dates_list}")

# Find dates close to it
print("\nDates around Jan 2024:")
for d in dates_list:
    if "2024-01" in d:
        print(d)