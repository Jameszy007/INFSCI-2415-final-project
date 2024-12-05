# Data Preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/vgchartz-2024.csv")

# Display the first few rows of the dataset and its summary for analysis
data.head(), data.info()

# Cleaning data: handling missing values in sales and scores
data_cleaned = data.dropna(subset=['total_sales', 'critic_score'])

# Extracting year from release_date
data_cleaned['release_year'] = pd.to_datetime(data_cleaned['release_date'], errors='coerce').dt.year

# Summarizing data for the first analysis (game genres and total sales)
genre_sales = data_cleaned.groupby('genre')['total_sales'].sum().sort_values(ascending=False)

# Plot 1: Total Sales by Game Genre
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_sales.values, y=genre_sales.index, palette="viridis")
plt.title('Total Sales by Game Genre')
plt.xlabel('Total Sales (Millions)')
plt.ylabel('Game Genre')
plt.tight_layout()
plt.show()
plt.savefig('D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/total_sales_by_genre.png')

# Summarizing data for the second analysis (games count by platform)
platform_counts = data_cleaned['console'].value_counts()

# Plot 2: Game Releases by Platform
plt.figure(figsize=(10, 6))
sns.barplot(x=platform_counts.index, y=platform_counts.values, palette="pastel")
plt.title('Game Releases by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/game_releases_by_platform.png')

# Summarizing data for the third analysis (critic score vs total sales)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data_cleaned, x='critic_score', y='total_sales', alpha=0.6)
plt.title('Critic Score vs Total Sales')
plt.xlabel('Critic Score')
plt.ylabel('Total Sales (Millions)')
plt.tight_layout()
plt.show()
plt.savefig('D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/critic_score_vs_total_sales.png')

# Summarizing data for the fourth analysis (sales by region)
region_sales = data_cleaned[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()

# Plot 4: Sales Distribution by Region
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color=['#4CAF50', '#FFC107', '#03A9F4', '#E91E63'])
plt.title('Sales Distribution by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (Millions)')
plt.tight_layout()
plt.show()
plt.savefig('D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/sales_distribution_by_region.png')

# Summarizing data for the fifth analysis (sales trend over years)
sales_trend = data_cleaned.groupby('release_year')['total_sales'].sum()

# Plot 5: Total Sales Over Years
plt.figure(figsize=(10, 6))
sales_trend.plot(kind='line', marker='o', color='#673AB7')
plt.title('Total Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Total Sales (Millions)')
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('D:/PITT/2024/Fall/INFSCI 2415/final project/data visualization/total_sales_over_years.png')