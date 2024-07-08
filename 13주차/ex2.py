import pandas as pd

data = {'열': [1,2,2,3,4],
        '열2': ['A', 'B', 'B','C', 'D'],
        '열3': [-10, 20, 30, 40, 150],
        '열4': ['A', 'B', 'B', 'Z', 'Z']}

df = pd.DataFrame(data)
print(df , end="\n\n")

print("1************************************")
df.loc[df['열4'] == 'Z', '열4'] = 'F'
print(df , end="\n\n")

print("2************************************")
df.loc[(df['열3'] > 100) | (df['열3'] < 0) , '열3'] = 0
print(df , end="\n\n")

print("3************************************")
df.drop_duplicates(subset=['열2', '열4'], keep='first', inplace=True)
