from numpy import average
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('flowers.csv')
df.info()


#function to convert values

def convert_range(value):
   try:
      if isinstance(value, str):
          if '-' in value:
              low, high = value.split('-')
              return (float(low) + float(high)) / 2
          elif value.lower() == 'variable':
              return None
          return float(value.replace('variable', '').strip())
   except:
      return None

df['height (cm)'] = df['height (cm)'].apply(convert_range)
df['longevity (years)'] = df['longevity (years)'].apply(convert_range)
df['average number of petals'] = df['average number of petals'].apply(convert_range)

df.info('average number of petals')
print(isinstance(df['average number of petals'][0], float))

X = df[['height (cm)', 'longevity (years)']]
y = df['average number of petals']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))