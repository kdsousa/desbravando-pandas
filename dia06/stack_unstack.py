# %%
import pandas as pd

df = pd.read_csv('../data/consolidado.csv', sep=';')
df

# %%
df = df.set_index(['cod', 'nome', 'período'])

# %%
df_stack = df.stack().reset_index().rename(columns={'level_3': 'Tipo Homicidio'})

# %%
df_stack

# %%
df_stack.set_index(['cod', 'nome', 'período', 'Tipo Homicidio']).unstack()

# %%
