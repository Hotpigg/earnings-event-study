import pandas as pd

# Load the price returns from Day 5
price_data = pd.read_csv('aapl_earnings_returns.csv')
print("Price data loaded:")
print(price_data)
print()

# Earnings data for the dates that worked
# NOTE: Verify these EPS numbers by Googling "AAPL earnings [date]"
earnings_info = {
    '2024-07-30': {'EPS_Estimate': 1.35, 'EPS_Actual': 1.40},
    '2024-10-31': {'EPS_Estimate': 1.60, 'EPS_Actual': 1.64},
    '2025-01-30': {'EPS_Estimate': 2.35, 'EPS_Actual': 2.40},
    '2025-04-24': {'EPS_Estimate': 1.53, 'EPS_Actual': 1.65},
}

# Convert earnings_info to a DataFrame
earnings_df = pd.DataFrame.from_dict(earnings_info, orient='index')
earnings_df.index.name = 'Date'
earnings_df = earnings_df.reset_index()
print("Earnings data:")
print(earnings_df)
print()

# Merge the two tables on Date
merged = pd.merge(price_data, earnings_df, on='Date')

# Calculate earnings surprise %
merged['Surprise_%'] = ((merged['EPS_Actual'] - merged['EPS_Estimate']) / merged['EPS_Estimate']) * 100

print("Merged data with surprise %:")
print(merged[['Date', 'Surprise_%', '1D_Return_%', '3D_Post_Return_%']])
print()

# THE KEY QUESTION: Does surprise predict the stock move?
correlation_1d = merged['Surprise_%'].corr(merged['1D_Return_%'])
correlation_3d = merged['Surprise_%'].corr(merged['3D_Post_Return_%'])

print(f"Correlation between earnings surprise and 1-day return: {correlation_1d:.3f}")
print(f"Correlation between earnings surprise and 3-day post return: {correlation_3d:.3f}")
print()

# Interpretation
if correlation_1d > 0.3:
    print("Result: Bigger surprises tend to move the stock more on day 1.")
elif correlation_1d < -0.3:
    print("Result: Bigger surprises actually lead to negative day-1 moves (possible 'sell the news').")
else:
    print("Result: No strong same-day relationship for this small sample.")

# Save the final dataset
merged.to_csv('aapl_earnings_analysis.csv', index=False)
print("\nSaved full analysis to aapl_earnings_analysis.csv")