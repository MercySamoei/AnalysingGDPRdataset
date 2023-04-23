import pandas as pd
df = pd.read_csv("GDPR.csv")

fine_by_article = df.groupby("VIOLATED_ARTICLES")["Amount"].sum()

fine_by_article_sorted = fine_by_article.sort_values(ascending=False)

print("Articles with the Highest Associated Fine:")
for article, fine in fine_by_article_sorted.head(10).iteritems():
    print(f"Article number: {article}, Associated Fine: {fine}")


import matplotlib.pyplot as plt
import numpy as np

# Extract x and y data from fine_by_article_sorted
x_values = fine_by_article_sorted.index.tolist()
y_values = fine_by_article_sorted.values.tolist()
colors = np.arange(len(x_values))

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Fine by Violated Article")
ax.set_xlabel("Violated Article")
ax.set_ylabel("Fine (EUR)")

# Add the scatter markers
scatter = ax.scatter(x_values, y_values, c=colors, cmap='viridis')

# Set the colorbar
colorbar = fig.colorbar(scatter)
colorbar.set_label("Color")

# Show the plot
plt.show()
    
