import pandas as pd

df = pd.read_csv("file.csv", sep=',')
print(df, end='\n\n')

sr_name = df['이름']
print(sr_name, end='\n\n')

sr_two = df.loc[1]
print(sr_two, end='\n\n')

cell_name = df.loc[1]['이름']
print(cell_name, end='\n\n')

cell_name = df.loc[1,'이름']
print(cell_name, end='\n\n')

print(df.head(2))
print(df.tail(1))
