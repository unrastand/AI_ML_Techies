import pandas as pd
sales_df = pd.read_csv('sales.csv')
sales_df.info()
sales_df.describe()
sales_df.isnull().sum()
sales_df.dropna(inplace=True)
sales_df.to_csv('sales_cleaned.csv', index=False)
sales_df.info()