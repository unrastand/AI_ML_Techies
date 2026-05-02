import pandas as pd

titanic_df = pd.read_csv('./prosper/titanic.csv')

# 1. How many passengers were on the Titanic?
num_passengers = len(titanic_df['PassengerId'])
print(f"Number of passengers on the Titanic: {num_passengers}")

# Print the first 10 rows of the DataFrame and use .describe() to get a summary of the numerical columns in the dataset.

print(titanic_df.describe())
print(titanic_df.info())