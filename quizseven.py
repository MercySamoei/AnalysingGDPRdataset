
import pandas as pd
data = pd.read_csv('GDPR.csv')
counts = data["VIOLATED_ARTICLES"].value_counts(sort = False).nlargest(10)
top_ten = counts.head()
print("Top 10 Most Violated Articles:")
for i, (article, count) in enumerate(zip(top_ten.index, top_ten.values), start=1):
    print(f"Article number: {article}, Number of violations: {count}")

   
