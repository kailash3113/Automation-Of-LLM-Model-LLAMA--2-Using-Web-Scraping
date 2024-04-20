import pandas as pd

df = pd.read_csv("DataFrame.csv")
df.reset_index(drop=True,inplace=True)

df.to_csv("test_df.csv",index=False)
