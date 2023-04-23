import pandas as pd

data = pd.read_csv('GDPR.csv')

data = data.dropna(subset=['Date'])

data['Date'] = pd.to_datetime(data['Date'])

grouped = data.groupby([data['Date'].dt.year, 'Type'])['Type'].count()

for year in range(data['Date'].dt.year.min(), data['Date'].dt.year.max() + 1):
    year_data = grouped[year]
    if year_data.empty:
        print(f"No offences recorded in {year}.")
    else:
        print(f"In {year}:")
        for offence, count in year_data.items():
            print(f"{offence}: {count}")
