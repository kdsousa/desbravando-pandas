"""
Converter o seguinte dicionário para DataFrame e obtenh:
    - Sumário de cada coluna 
    - Média da coluna idade
    - Último nome da coluna nome

dados = {
    'nome': ['Téo', 'Nah', 'Napoleão'], 
    'idade': [31, 32, 14]
}
"""

# %%
import pandas as pd
dados = {
    'nome': ['Téo', 'Nah', 'Napoleão'], 
    'idade': [31, 32, 14]
}

df = pd.DataFrame(dados)
df

# %%
df.describe()
df['nome'].describe()

# %%
df['idade'].mean()

# %%
df['nome'].iloc[-1]

# %%
df['nome'].tail(1)
# %%
