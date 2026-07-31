import pandas as pd

# Load the data back from the file
df = pd.read_csv('fake_earnings.csv')

print("Loaded data:")
print(df)

# Filter for big beats (surprise > 3%)
big_beat = df[df['Surprise_%'] > 3]
print("\nBig beats:")
print(big_beat)

# Save only the big beats to a new file
big_beat.to_csv('big_beaters.csv', index=False)
print("\nSaved big_beaters.csv")