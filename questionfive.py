import plotly.express as px
import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv('GDPR.csv')

# Aggregate the data by country and sum the amount
df_agg = df.groupby('Country', as_index=False).agg({'Amount': 'sum'})

# Create the choropleth map with a custom colorscale
fig = px.choropleth(df_agg, 
                    locations="Country", 
                    locationmode='country names',
                    color="Amount",
                    color_continuous_scale=px.colors.sequential.Purpor,
                    range_color=(0, df_agg['Amount'].max()),
                    title='Total amount fined by country'
                    )

fig.show()