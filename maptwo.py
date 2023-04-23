import pandas as pd
import plotly.express as px

# read in the data
data = pd.read_csv('GDPR.csv', parse_dates=['Date'], dayfirst=True)

# group the data by country and type of violation, and sum the amounts
grouped = data.groupby(['Country', 'Type'])['Amount'].sum().reset_index()

# sort the data in descending order based on the amount column
sorted_data = grouped.sort_values(['Country', 'Amount'], ascending=[True, False])

# create the bar chart
fig = px.bar(sorted_data, x='Country', y='Amount', color='Type', title='Top GDPR Violations by Country')

# adjust the size of the graph
fig.update_layout(
    autosize=True,
    width=1600,
    height=600,
)

fig.show()
