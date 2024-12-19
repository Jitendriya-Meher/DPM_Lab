import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'

# 1
data = pd.read_csv("BC.csv")
# data = pd.read_csv(url)
# print(data)

df = pd.DataFrame(data)
print(df)

# 2
df.replace('?', np.nan, inplace=True)
# print(df)

# 3
print("\nNull cols 3 :\n",df.isnull().sum())

#4
# df.replace(np.nan, 0 , inplace=True)


bData = []

for i in (df["Bare_Nuclei"]):
    # print(i,type(i))
    bData.append(float(i))

# print(df["Bare_Nuclei"].median())

# print("\nNull cols :\n",df.isnull().sum())

bData = pd.DataFrame(data=bData)

med = bData.median()

print("\n\nmedian = ",med[0])

df.replace(np.nan, med[0] , inplace=True)

print("\nNull cols after 4 :\n",df.isnull().sum())


# print(df)