# %%
import pandas as pd 

data_user = {

    'id': [1, 2, 3, 4],
    'nome': ['Téo', 'Mat', 'Nah', 'Mah'],
    'idade': [31, 31, 32, 32]

}

df_user = pd.DataFrame(data_user)
df_user

# %%
data_tranacoes = {

    'id_user': [1, 1, 1, 2, 3, 3],
    'vl': [432, 532, 123, 6, 4, 87],
    'qtProdutos': [2, 1, 3, 6, 10, 2]

}

df_transacao = pd.DataFrame(data_tranacoes)
df_transacao

# %%
df_transacao.merge(df_user, 
                   how='left', 
                   left_on='id_user',
                   right_on='id')

# %%
