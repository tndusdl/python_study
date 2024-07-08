import pandas as pd

air = pd.read_csv('air.csv')

print("1*******************************")
print(air, end="\n\n")
air.info()

print("2*******************************")
print(air.isnull().sum(), end="\n\n")

print("3*******************************")
air_d = air.dropna(axis=0)
print(air_d, end="\n\n")

print("4*******************************")
air_d2 = air.dropna(axis=1)
print(air_d2, end="\n\n")

print("5*******************************")
air_m1 = air.fillna(0)
print(air_m1, end="\n\n")

print("6*******************************")
mean = air['PM10'].mean()
air_m2 = air['PM10'].fillna(mean)
print(air_m2, end="\n\n")
