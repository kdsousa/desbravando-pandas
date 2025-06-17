# %%
import pandas as pd

# %%
df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%
df.info()

# %%
# Ordenando a coluna
df.sort_values(by ='Points', ascending=False, inplace=True)
df.rename(columns={'Name': 'Nome', 'Points': 'Pontos'}, inplace=True)
# %%
df.sort_values(by =['Points', 'Name'], ascending=[False, True])


# %%
df = (df.sort_values(by ='Points', ascending=False)
        .rename(columns={'Name': 'Nome', 'Points': 'Pontos'}))

# %%
df

# %%
