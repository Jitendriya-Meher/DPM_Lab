import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates

data = pd.read_csv("data.csv")
# print(data)

# 1
df = pd.DataFrame(data)
print("data frame : \n",df)

df2 = df.drop(['species'], axis=1)

mean_values = df2.mean()
std_dev_values = df2.std()
min_values = df2.min()
max_values = df2.max()

# 2
print("\nMean values: \n", mean_values)
print("\nStandard deviation values:\n", std_dev_values)
print("\nMinimum values:\n", min_values)
print("\nMaximum values:\n", max_values)

# 3
print("\ncounts:\n", df["species"].value_counts())

# 4
print("\n describe : \n",df.describe())

# 5
# Display the covariance matrix
print("\nCovariance Matrix:")
print(df2.cov())
# Display the correlation matrix
print("\nCorrelation Matrix:\n")
print(df2.corr())

#6
plt.hist(df["sepal_length"])
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
# plt.show()

#7
df.boxplot()
plt.title('Boxplot of Each Attribute in the Iris Dataset')
plt.xlabel('Attributes')
plt.ylabel('Value')
plt.show()

#8
sns.scatterplot(x="sepal_length",y="sepal_width",data=df)
plt.show()

sns.scatterplot(x="sepal_length",y="sepal_width",data=df)
plt.show()

#9
parallel_coordinates(df,"species")
plt.show()