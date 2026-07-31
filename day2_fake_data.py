import pandas as pd

# Create fake earnings data
data = {
    'Date': ['2024-01-25', '2024-04-25', '2024-07-30'],
    'Ticker': ['AAPL', 'AAPL', 'AAPL'],
    'EPS_Estimate': [2.10, 1.50, 1.35],
    'EPS_Actual': [2.18, 1.53, 1.40],
    'Price_Before': [185.0, 169.0, 225.0],
    'Price_After': [194.0, 173.0, 230.0]
}

df = pd.DataFrame(data)

# Calculate surprise %
df['Surprise_%'] = ((df['EPS_Actual'] - df['EPS_Estimate']) / df['EPS_Estimate']) * 100

# Calculate stock return
df['Stock_Return_%'] = ((df['Price_After'] - df['Price_Before']) / df['Price_Before']) * 100

# Show all rows
print("All data:")
print(df)

# Show only the rows where Apple beat estimates
beat = df[df['EPS_Actual'] > df['EPS_Estimate']]
print("\nBeat estimates:")
print(beat)

# Show only big beats (surprise > 5%)
big_beat = df[df['Surprise_%'] > 5]
print("\nBig beats:")
print(big_beat)