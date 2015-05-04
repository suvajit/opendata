#
# Merge two CSV file based on common field
# here WARD_NO is the common field
#
# @author jeet_sen@yahoo.co.in	

import pandas as pd

a = pd.read_csv("../work/Bangalore_Ward_Population_2011.csv")
b = pd.read_csv("../work/bbmpwards_old_data.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='WARD_NO')
merged.to_csv("../work/bbmp_wards_data_merged.csv", index=False)
