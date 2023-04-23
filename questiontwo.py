import pandas as pd

# Load the data
data = pd.read_csv('GDPR.csv', parse_dates=['Date'], dayfirst=True)

# Group the data by country and type of violation, and sum the amounts
grouped = data.groupby(['Country', 'Type'])['Amount'].sum()

# Sort the data in descending order based on the amount column
sorted_data = grouped.reset_index().sort_values(['Country', 'Amount'], ascending=[True, False])

# Loop over the sorted data and print the top violations for each country
for country, violations in sorted_data.groupby('Country'):
    print(f"\nThe most expensive violations in {country} are:")
    for i, row in violations.head().iterrows():
        print(f"{row['Type']}: {row['Amount']} euros")

