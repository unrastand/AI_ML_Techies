import pandas as pd

data = {"Name": ["John", "Alice", "Bob"],"Age": [25, 30, 22]}
df = pd.DataFrame(data)
print(df)

df.to_csv('data.csv', index=False)
