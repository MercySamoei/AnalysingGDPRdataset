import pandas as pd

df = pd.read_csv('GDPR.csv')
vodafone_df = df[df['Controller_Processor'].str.contains('Vodafone')]
total_vodafone_violations = vodafone_df['VIOLATED_ARTICLES'].sum()

print(f"Total GDPR violations by Vodafone: {total_vodafone_violations}")
