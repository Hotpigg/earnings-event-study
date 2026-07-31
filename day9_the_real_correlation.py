import pandas as pd

# Load abnormal returns from Day 8
df = pd.read_csv('multi_company_abnormal_returns.csv')
print(f"Loaded {len(df)} events")
print()

# Earnings data: EPS Estimate vs Actual
# Format: 'Ticker|Date': {'estimate': X.XX, 'actual': X.XX}
# VERIFY THESE NUMBERS ON GOOGLE IF YOU WANT PRECISION
earnings_data = {
    'AAPL|2024-07-30': {'estimate': 1.35, 'actual': 1.40},
    'AAPL|2024-10-31': {'estimate': 1.60, 'actual': 1.64},
    'AAPL|2025-01-30': {'estimate': 2.35, 'actual': 2.40},
    'AAPL|2025-04-24': {'estimate': 1.53, 'actual': 1.65},
    
    'MSFT|2024-07-30': {'estimate': 2.93, 'actual': 2.95},
    'MSFT|2024-10-24': {'estimate': 3.10, 'actual': 3.30},
    'MSFT|2025-01-29': {'estimate': 3.20, 'actual': 3.23},
    'MSFT|2025-04-24': {'estimate': 3.10, 'actual': 3.10},
    
    'TSLA|2024-10-23': {'estimate': 0.60, 'actual': 0.72},
    'TSLA|2025-01-29': {'estimate': 0.73, 'actual': 0.66},
    'TSLA|2025-04-22': {'estimate': 0.42, 'actual': 0.41},
    'TSLA|2025-07-23': {'estimate': 0.60, 'actual': 0.52},
    
    'AMZN|2024-07-30': {'estimate': 1.14, 'actual': 1.26},
    'AMZN|2024-10-31': {'estimate': 1.14, 'actual': 1.43},
    'AMZN|2025-01-30': {'estimate': 1.38, 'actual': 1.89},
    'AMZN|2025-04-24': {'estimate': 1.36, 'actual': 1.59},
}

# Add EPS data to the dataframe
df['EPS_Estimate'] = df.apply(lambda row: earnings_data.get(f"{row['Ticker']}|{row['Date']}", {}).get('estimate', None), axis=1)
df['EPS_Actual'] = df.apply(lambda row: earnings_data.get(f"{row['Ticker']}|{row['Date']}", {}).get('actual', None), axis=1)

# Remove rows where we don't have earnings data
df = df.dropna(subset=['EPS_Estimate', 'EPS_Actual'])

# Calculate earnings surprise %
df['Surprise_%'] = ((df['EPS_Actual'] - df['EPS_Estimate']) / df['EPS_Estimate']) * 100

print("Dataset with earnings surprises:")
print(df[['Ticker', 'Date', 'Surprise_%', 'Abnormal_1D_Return_%', 'Abnormal_3D_Post_Return_%']])
print()

# THE REAL CORRELATION
corr_1d = df['Surprise_%'].corr(df['Abnormal_1D_Return_%'])
corr_3d = df['Surprise_%'].corr(df['Abnormal_3D_Post_Return_%'])

print(f"Correlation: Surprise % vs Abnormal 1-Day Return: {corr_1d:.3f}")
print(f"Correlation: Surprise % vs Abnormal 3-Day Post Return: {corr_3d:.3f}")
print()

# Interpretation
if corr_1d > 0.3:
    print("Finding: Bigger earnings surprises tend to drive bigger abnormal returns on day 1.")
elif corr_1d < -0.3:
    print("Finding: Bigger surprises lead to negative abnormal returns (possible 'sell the news' effect).")
else:
    print("Finding: No strong linear relationship between surprise and abnormal return in this sample.")
    print("Possible reasons: market already priced it in, guidance mattered more than EPS, or sample is too small.")

# Save the full analysis
df.to_csv('full_earnings_analysis.csv', index=False)
print("\nSaved complete analysis to full_earnings_analysis.csv")