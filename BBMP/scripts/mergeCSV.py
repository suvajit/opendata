import pandas as pd

a = pd.read_csv("../data/Census_2011.csv")
b = pd.read_csv("../data/bbmpwards.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='WARD_NO')
merged.to_csv("output.csv", index=False)
