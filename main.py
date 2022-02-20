# Data analysis of Billionaire
# Data set forbes list


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv("Billionaire.csv")
df10 = dataframe.head(10)
print(df10)
print(dataframe.columns)

plt.figure(figsize = (10,6))
sns.barplot(x = df10['Rank'], y = df10['Age'], hue = df10['Name'])
plt.show()



