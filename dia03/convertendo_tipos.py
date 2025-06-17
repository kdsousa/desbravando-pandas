# %%
import pandas as pd 

df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%
df.dtypes

# %%
df['Points'].astype(str)

# %%
df['Points_dobble'] = df['Points'] * 2

# %%
df[['Points', 'Points_dobble']].astype(str)

# %%
df['Lista'] = [[1, 2] for i in df.index]

df

# %%
df.dtypes

# %%
