import pandas as pd

data = pd.read_csv('GDPR.csv')

data = data.dropna(subset=['Controller_Processor'])
# if data['VIOLATED_ARTICLES'].isnull().values.any():
#     print("VIOLATED_ARTICLES has NaN values.")
# else:
#     print("VIOLATED_ARTICLES does not have NaN values.")
#data['Date'] = pd.to_datetime(data['Date'])


# group the data by company and count the number of violations
grouped = data.groupby(['Controller_Processor'])['VIOLATED_ARTICLES'].count()

for company, count in grouped.items():
    if pd.isna(company):
        print(f"No company name recorded for {count} violations.")
    else:
        print(f"{company} committed {count} violations.")




