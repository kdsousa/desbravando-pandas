# %%
import pandas as pd 
import numpy as np

df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%
df['Points_dobble'] = df['Points'] * 2
df

# %%
df['Points_ratio'] = df['Points_dobble'] / df['Points']
df

# %%
df['Constante'] = 1
df

# %%
df['Points_log'] = np.log(df['Points'])
df

# %%
nome_alta = []
for i in df['Name']:
    nome_alta.append(i.upper())

df['Nome_alta'] = nome_alta 
df

# %%
df['Name'].str.upper()

# %%
def get_first(nome:str):
    nome = nome.upper()
    return nome.split('_')[0]

# %%
df['Name_First'] = df['Name'].apply(get_first)
df

# %%
get_f = lambda nome: nome.split('_')[0]
get_f('Keplin')

# %%
df['Name'].apply(lambda x: x.split('_')[0])

# %%
def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'baixo'
    elif pontos < 3500: 
        return 'medio'
    else:
        return 'alto'
    
df['Faixa_Pontos'] = df['Points'].apply(intervalo_pontos)
df

# %%
