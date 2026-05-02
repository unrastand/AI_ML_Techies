# Project Goal:
# 1. Identify major causes of accident
# 2.Find most dangerous state for car accidents
# 3. Dictate patterns and trends in car accidents

 
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

dataset_df = pd.read_csv('carAccident_data.csv')
dataset_df.info()

# Remove negative values from the dataset
Num_Killed_df = dataset_df[dataset_df['Num_Killed'] >= 0]
Num_Injured_df = dataset_df[dataset_df['Num_Injured'] >= 0]
Total_Vehicles_Involved_df = dataset_df[dataset_df['Total_Vehicles_Involved'] >= 0]

# Remove duplicate
dataset_df.drop_duplicates(inplace=True)

# Fill missing values
dataset_df = dataset_df.fillna(0)

# Analyze the data
basic_stats = dataset_df[['Num_Killed', 'Num_Injured', 'Total_Vehicles_Involved']].describe()

top_states_by_death = dataset_df.groupby('State')['Num_Killed'].mean().sort_values(ascending=False).head(10)

causes_of_accidents = ['SPV', 'DAD', 'PWR', 'FTQ', 'Other_Factors']
label = ['Speeding', 'Distracted Driving', 'Poor Weather', 'Failure to Yield', 'Other Factors']
cause_counts = dataset_df[causes_of_accidents].sum().sort_values(ascending=False)

correlation_with_deaths = dataset_df.corr(numeric_only=True)['Num_Killed'].sort_values(ascending=False)

# Visualize the data
plt.figure()
sb.barplot(x=top_states_by_death.index, y=top_states_by_death.values)
plt.title('Top 10 States by Average Number of Deaths in Car Accidents')
plt.xlabel('State')
plt.ylabel('Average Number of Deaths')
plt.show()

sb.barplot(x=label, y=cause_counts.values)
plt.xticks(rotation=30) 
plt.title('Causes of Car Accidents')
plt.xlabel('Cause')
plt.ylabel('Count')
plt.show()
