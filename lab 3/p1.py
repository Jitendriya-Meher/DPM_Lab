import pandas as pd
import random
data = {
    'user_id':['1','2','3','4','5','6','1','2','3','4','5','6'],
    'item_name':['item1','item2','item3','item4','item5','item6','item1','item2','item3','item1','item2','item3'],
    'transaction_amount':[100.87,200.18,300.099,400.1,500.23,600.22,100.87,200.18,300.099,100.87,200.18,300.099]
}

df = pd.DataFrame(data)
df
groupDf = df.groupby('user_id')
groupDf
for i,user in groupDf:
    sum = 0
    count = 0
    for i in range (len(user)):
        sum += user.iloc[i]['transaction_amount']
        count += 1
    print(f"user_id = {user.iloc[0]['user_id']} , average transaction = {sum/count}")
    
groupDf.mean(numeric_only=True)
n = int(len(df)*0.1)
for i in range (n):
    i = random.randint(0,len(df)-1)
    print(df.loc[i])
def sampledDf(df,seed):
    sampled_df = df.sample(frac=0.1, random_state=seed)
    print(sampled_df)

sampledDf(df,42)