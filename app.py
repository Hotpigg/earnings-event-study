import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Earnings Event Study", layout="wide")

# Title
st.title("📊 Earnings Surprise vs. Stock Returns")
st.markdown("**An event-study analysis of how earnings surprises drive abnormal returns across AAPL, MSFT, TSLA, and AMZN.**")

# Load data
df = pd.read_csv('full_earnings_analysis.csv')

# Sidebar filters
st.sidebar.header("Filters")
selected_tickers = st.sidebar.multiselect("Select Companies", df['Ticker'].unique(), default=df['Ticker'].unique())
min_surprise = st.sidebar.slider("Minimum Surprise %", float(df['Surprise_%'].min()), float(df['Surprise_%'].max()), float(df['Surprise_%'].min()))

# Filter data
filtered = df[(df['Ticker'].isin(selected_tickers)) & (df['Surprise_%'] >= min_surprise)]

# Key metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Events", len(filtered))
col2.metric("Avg Abnormal 1D Return", f"{filtered['Abnormal_1D_Return_%'].mean():.2f}%")
col3.metric("Avg Abnormal 3D Return", f"{filtered['Abnormal_3D_Post_Return_%'].mean():.2f}%")
col4.metric("Best Single Event", f"{filtered['Abnormal_1D_Return_%'].max():.2f}%")

st.divider()

# Data table
st.subheader("Event-Level Data")
st.dataframe(filtered[['Ticker', 'Date', 'Surprise_%', 'Abnormal_1D_Return_%', 'Abnormal_3D_Post_Return_%']].sort_values('Surprise_%', ascending=False), use_container_width=True)

st.divider()

# Charts
st.subheader("Visual Analysis")
col_left, col_right = st.columns(2)

colors = {'AAPL': '#007AFF', 'MSFT': '#00A86B', 'TSLA': '#FF3B30', 'AMZN': '#FF9500'}

with col_left:
    st.markdown("**Same-Day Reaction**")
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    for ticker in filtered['Ticker'].unique():
        subset = filtered[filtered['Ticker'] == ticker]
        ax1.scatter(subset['Surprise_%'], subset['Abnormal_1D_Return_%'], 
                   label=ticker, color=colors.get(ticker, 'gray'), s=80, alpha=0.7)
    ax1.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
    ax1.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
    ax1.set_xlabel('Earnings Surprise %')
    ax1.set_ylabel('Abnormal 1-Day Return %')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    st.pyplot(fig1)

with col_right:
    st.markdown("**3-Day Post-Earnings Drift**")
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    for ticker in filtered['Ticker'].unique():
        subset = filtered[filtered['Ticker'] == ticker]
        ax2.scatter(subset['Surprise_%'], subset['Abnormal_3D_Post_Return_%'], 
                   label=ticker, color=colors.get(ticker, 'gray'), s=80, alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
    ax2.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
    ax2.set_xlabel('Earnings Surprise %')
    ax2.set_ylabel('Abnormal 3-Day Post Return %')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)

st.divider()

# Interpretation
st.subheader("Key Findings")
st.markdown("""
- **Same-day reaction (-0.230 correlation):** Large earnings surprises show a slight negative same-day abnormal return, suggesting the market front-runs positive news ("buy the rumor, sell the news").
- **Post-earnings drift (+0.344 correlation):** Abnormal returns over the 3 days following earnings show positive correlation with surprise magnitude, consistent with the **Post-Earnings Announcement Drift (PEAD)** anomaly documented in academic finance literature.
- **Outlier:** Amazon's Q1 2025 earnings (36.9% surprise) generated significant abnormal returns, highlighting that extreme surprises may drive continued price discovery after the initial announcement.
""")