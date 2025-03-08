import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


data = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\api\data Analaysis\Super_International_Market.csv', encoding= 'latin1')
print(data)

# for copy data file 
df = data.copy()
print(df)


"""
Functions used:
- `df.head()`: Displays the first 5 rows of the DataFrame by default.
- `df.tail()`: Displays the last 5 rows of the DataFrame by default.
- `df.info()`: Provides a concise summary of the DataFrame, including the number of non-null entries and data types.
- `df.shape`: Returns a tuple representing the dimensionality of the DataFrame (number of rows, number of columns).
- `df.describe()`: Generates descriptive statistics that summarize the central tendency, dispersion, and shape of the DataFrame's distribution, excluding NaN values.
"""
df.head()

df.tail()

df.info()

df.shape

df.describe()

df.describe(include ='all')

df.dtypes


# column that contain float values
float_type = df[['Postal Code', 'Sales', 'Discount', 'Profit', 'Shipping Cost']]
float_type.head()

else_type = df[['Row ID', 'Order ID', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country']]
else_type.head()

data_type = df[['Order Date','Ship Date']]
data_type.head()

df['Order Date'] = pd.to_datetime(df['Order Date'], format= 'mixed', errors= 'coerce')

df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed')

# Verify the conversion
print(df[['Order Date', 'Ship Date']].dtypes)

df.dtypes


df.columns



df['Ship Mode'] = df['Ship Mode'].astype('category')
df['Segment'] = df['Segment'].astype('category')
df['Country'] = df['Country'].astype('category')
df['Market'] = df['Market'].astype('category')
df['Region'] = df['Region'].astype('category')
df['Category'] = df['Category'].astype('category')
df['Sub-Category'] = df['Sub-Category'].astype('category')
df['Order Priority'] = df['Order Priority'].astype('category')

df.info()



# Data Cleaning =>

df.duplicated().sum()

df.isnull().sum()

df.shape

df.nunique()

postal_code_mode = df['Postal Code'].mode()[0]
postal_code_mode
df['Postal Code'] = df['Postal Code'].fillna(postal_code_mode)
df['Postal Code'].head()

df['Postal Code'].isnull().sum()

df.columns

Sale_nevigate = df['Sales']>= 0
Sale_nevigate


negative_Sales = df[df['Sales'] < 0]
if not negative_Sales.empty:
    print(negative_Sales)
negative_Sales


# check negative value in profit column

negative_profit = df[df['Profit'] < 0]
if not negative_profit.empty:
    print("Negative Value in 'Profit':")
    print(negative_profit.head(30))
    

mean_profit = df[df['Profit'] > 0] ['Profit'].mean()
data.loc[data['Profit'] < 0, 'Profit'] =  mean_profit
mean_profit


# Replace negative 'profit' values with the calculate mean
df['Profit'] = df['Profit'].apply(lambda x: mean_profit if x < 0 else x)

print("Negative value in 'profit' have been replaced with the mean of non-negative profits.")
print(df['Profit'].head(5))

df.info()

# Segement The Data :>

segement_data = df[['Customer ID', 'Customer Name', 'Category', 'Product Name', 'Sub-Category', 'Sales', 'Profit', 'Quantity', 'Discount',
                    'Order Date', 'City', 'State', 'Region', 'Market', 'Order Priority']]

segement_data.head()






# Sales and Profit Analysis
# 1. What is the trend of sales and profit over time?

# Convert 'Order Date' to datetime if not already done
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', errors='coerce')

# Extract year from 'Order Date'
df['Year'] = df['Order Date'].dt.year

# Group data by 'Year' and calculate the sum of 'Sales' and 'Profit'
sales_profit_trend_by_year = df.groupby('Year')[['Sales', 'Profit']].sum().reset_index()

# Print the sales and profit trend by year
print(sales_profit_trend_by_year)

# Plot the trend of sales and profit over time
plt.figure(figsize=(14, 7))

# Plot Sales trend with points
plt.plot(sales_profit_trend_by_year['Year'], sales_profit_trend_by_year['Sales'], label='Sales', linewidth=2.5, color='blue', marker='o')

# Plot Profit trend with points
plt.plot(sales_profit_trend_by_year['Year'], sales_profit_trend_by_year['Profit'], label='Profit', linewidth=2.5, color='green', marker='o')

# Add title and labels
plt.title('Trend of Sales and Profit Over Time', color='blue')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.grid(True, linestyle='--' )
plt.legend(loc='upper left', fontsize=12)

plt.tight_layout()

# Show the plot
plt.show()


# Generate Sales and Profit Report
sales_profit_report = sales_profit_trend_by_year.copy()
sales_profit_report.columns = ['Year', 'Total Sales', 'Total Profit']

# Print the Sales and Profit Report
print("\nSales and Profit Report:")
print(sales_profit_report)







# Analysis of Sales and Profit by Region and Market

# Group data by 'Region' and calculate the sum of 'Sales' and 'Profit'
region_sales_profit = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()

# Group data by 'Market' and calculate the sum of 'Sales' and 'Profit'
market_sales_profit = df.groupby('Market')[['Sales', 'Profit']].sum().reset_index()

# Plot Sales and Profit by Region
plt.figure(figsize=(14, 7))

# Plot Sales by Region
plt.subplot(1, 2, 1)
plt.bar(region_sales_profit['Region'], region_sales_profit['Sales'], color='blue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)

# Plot Profit by Region
plt.subplot(1, 2, 2)
plt.bar(region_sales_profit['Region'], region_sales_profit['Profit'], color='green')
plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Profit')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()




# Plot Sales and Profit by Market
bar_width = 0.5
markets = market_sales_profit['Market']
sales = market_sales_profit['Sales']
profit = market_sales_profit['Profit']

# Create bar chart for Sales
plt.bar(markets, sales, bar_width, label='Sales', color='blue')

# Create bar chart for Profit stacked on top of Sales
plt.bar(markets, profit, bar_width, bottom=sales, label='Profit', color='green')

# Add title and labels
plt.title('Sales and Profit by Market')
plt.xlabel('Market')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

# Print the Sales and Profit by Region
print("\nSales and Profit by Region:")
print(region_sales_profit)

# Print the Sales and Profit by Market
print("\nSales and Profit by Market:")
print(market_sales_profit)







# Which city and states are most profitable?

city_state_profit = segement_data.groupby(['City', 'State'])['Profit'].sum().reset_index()

top_city_state_profit = city_state_profit.sort_values(by='Profit', ascending=False).head()

top_city_state_profit




# Sort the data for top cities and states by Profit
top_city_state_profit = city_state_profit.sort_values(by='Profit', ascending=False).head()

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting Profit by City and State (Bar Chart)
top_city_state_profit.plot(kind='bar', x='City', y='Profit', ax=ax, color='#2ca02c')

# Set the title and labels
ax.set_title('Top Cities and States by Profit', fontsize=14, color='darkblue')
ax.set_ylabel('Profit ($)', fontsize=12)
ax.set_xlabel('City', fontsize=12)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()




# which products are the most popular (highest quantity sold)?

# Analysis of the most popular products (highest quantity sold)

# Group data by 'Product Name' and calculate the sum of 'Quantity'
product_quantity = df.groupby('Product Name')['Quantity'].sum().reset_index()

# Sort the data for top products by Quantity
top_products = product_quantity.sort_values(by='Quantity', ascending=False).head()

# Create the pie chart
plt.figure(figsize=(14, 7))
plt.pie(top_products['Quantity'], labels=top_products['Product Name'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

# Set the title
plt.title('Top 10 Most Popular Products (Highest Quantity Sold)', fontsize=14, color='darkblue')

# Show the plot
plt.tight_layout()
plt.show()

# Print the top products by quantity sold
print("\nTop 10 Most Popular Products (Highest Quantity Sold):")
print(top_products)




# What is the sales and profit distribution across different markets?

# Analysis of Sales and Profit Distribution Across Different Markets

# Group data by 'Market' and calculate the sum of 'Sales' and 'Profit'
market_sales_profit = df.groupby('Market')[['Sales', 'Profit']].sum().reset_index()

# Plot Sales and Profit by Market using stacked bar chart
plt.figure(figsize=(14, 7))

# Plot Sales and Profit by Market
bar_width = 0.5
markets = market_sales_profit['Market']
sales = market_sales_profit['Sales']
profit = market_sales_profit['Profit']

# Create bar chart for Sales
plt.bar(markets, sales, bar_width, label='Sales', color='blue')

# Create bar chart for Profit stacked on top of Sales
plt.bar(markets, profit, bar_width, bottom=sales, label='Profit', color='green')

# Add title and labels
plt.title('Sales and Profit Distribution Across Different Markets', fontsize=14, color='darkblue')
plt.xlabel('Market', fontsize=12)
plt.ylabel('Amount', fontsize=12)
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

# Print the Sales and Profit by Market
print("\nSales and Profit by Market:")
print(market_sales_profit)