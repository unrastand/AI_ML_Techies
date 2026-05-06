import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

sales_df = pd.read_csv('sales.csv')


sales_df.dropna(inplace=True)
sales_df.iloc[3,10]= 60

sales_df['Unit_Price'] = pd.to_numeric(sales_df['Unit_Price'])
sales_df['Total_Sales'] = pd.to_numeric(sales_df['Total_Sales'])

sb.heatmap(sales_df.corr(numeric_only=True), annot=True)
plt.title('Correlation Heatmap of Sales Data')
plt.show()