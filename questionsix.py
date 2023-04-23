import pandas as pd
import plotly.express as px

df = pd.read_csv('GDPR.csv')

df = df.dropna(subset=['VIOLATED_ARTICLES', 'Amount'])

fig = px.box(df, x='VIOLATED_ARTICLES', y='Amount', title='Distribution of GDPR fines per article')

fig.show()
