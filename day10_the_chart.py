import pandas as pd
import matplotlib.pyplot as plt

# Load the full analysis
df = pd.read_csv('full_earnings_analysis.csv')

# Create a figure with 2 subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Color map for tickers
colors = {'AAPL': 'blue', 'MSFT': 'green', 'TSLA': 'red', 'AMZN': 'orange'}

# Plot 1: Surprise % vs Abnormal 1-Day Return
for ticker in df['Ticker'].unique():
    subset = df[df['Ticker'] == ticker]
    axes[0].scatter(subset['Surprise_%'], subset['Abnormal_1D_Return_%'], 
                    label=ticker, color=colors.get(ticker, 'gray'), s=80, alpha=0.7)

axes[0].axhline(y=0, color='black', linestyle='--', linewidth=0.8)
axes[0].axvline(x=0, color='black', linestyle='--', linewidth=0.8)
axes[0].set_xlabel('Earnings Surprise %', fontsize=12)
axes[0].set_ylabel('Abnormal 1-Day Return %', fontsize=12)
axes[0].set_title('Same-Day Reaction: Buy the Rumor, Sell the News?', fontsize=13)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Surprise % vs Abnormal 3-Day Post Return
for ticker in df['Ticker'].unique():
    subset = df[df['Ticker'] == ticker]
    axes[1].scatter(subset['Surprise_%'], subset['Abnormal_3D_Post_Return_%'], 
                    label=ticker, color=colors.get(ticker, 'gray'), s=80, alpha=0.7)

axes[1].axhline(y=0, color='black', linestyle='--', linewidth=0.8)
axes[1].axvline(x=0, color='black', linestyle='--', linewidth=0.8)
axes[1].set_xlabel('Earnings Surprise %', fontsize=12)
axes[1].set_ylabel('Abnormal 3-Day Post Return %', fontsize=12)
axes[1].set_title('Post-Earnings Drift: Does the Market Underreact?', fontsize=13)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('earnings_analysis_chart.png', dpi=150)
print("Chart saved as earnings_analysis_chart.png")

plt.show()