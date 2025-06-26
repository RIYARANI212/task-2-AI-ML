# Customer Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
df = pd.read_csv('customer_data.csv')
df.head()

# Summary Statistics
df.info()
df.describe()
df.median(numeric_only=True)
df.mode(numeric_only=True).iloc[0]

# Histogram
df.hist(figsize=(10, 6), bins=10)
plt.suptitle('Histogram of Numeric Features')
plt.show()

# Boxplot
sns.boxplot(data=df.select_dtypes(include='number'))
plt.title('Boxplot of Numeric Features')
plt.xticks(rotation=45)
plt.show()

# Pairplot
sns.pairplot(df, hue='Gender')
plt.suptitle('Pairwise Relationships', y=1.02)
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Plotly Interactive Visuals
px.histogram(df, x='Age', nbins=10, title='Age Distribution').show()
px.scatter(df, x='AnnualIncome', y='SpendingScore', color='Gender', title='Income vs Spending').show()
