# %%
import pandas as pd

df_customens = pd.read_csv("../data/customers.csv", sep=";")
df_customens

# %%
# Quantidade de linhas e colunas
df_customens.shape

# %%
df_customens.info(memory_usage='deep')

# %%
df_customens['Points'].describe()

# %%
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)

# %%
notas_novas = []
for i in notas:
    notas_novas.append(i + 1)

notas_novas

# %%
condicao = df_customens['Points'] > 1000

df_customens[condicao]

# %%
maximo = df_customens['Points'].max()
maximo

condicao = df_customens['Points'] == maximo
df_customens[condicao]

# %%
df_customens[df_customens['Points'] == df_customens['Points'].max()]['Name'].iloc[0]

# %%
condicao = (df_customens['Points'] >= 1000) & (df_customens['Points'] <= 2000)
condicao

# %%
df_customens[condicao]
# %%
a= [1, 2, 3, 4]
b = a.copy()
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %%

df_customens[['UUID', 'Name']]

# %%
colunas = df_customens.columns.tolist()
colunas.sort()

df_customens[colunas]

# %%
df_customens = df_customens[colunas]
df_customens

# %%
df_customens = df_customens.rename(columns={'Name': 'Nome', 'Points': 'Pontos'})

# %%
df_customens

# %%
df_customens.rename(columns={'UUID': 'Id'}, inplace=True)

# %%
df_customens

# %%
