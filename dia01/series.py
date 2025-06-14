# %%
import pandas as pd 

# %%
idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0 
for i in idades:
    total += (media - i) ** 2

variancia = total / (len(idades) -1)

variancia
# %%
series_idades = pd.Series(idades)