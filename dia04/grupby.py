# %%
import pandas as pd

df = pd.read_excel('../data/transactions.xlsx')
df

# %%
condicao =  df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df [condicao]
df_user

# %%
df_user['Points'].sum()

# %%
df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()

# %%
df.groupby(['IdCustomer']).agg({'Points': 'sum', 'UUID': 'count', 'DtTransaction': 'max'}).rename(columns={'Points': 'Valor', 'UUID': 'Frequancia', 'DtTransaction': 'UltimaData'})

# %%
df

# %%
import datetime

data1 = df['DtTransaction'][0]
now = datetime.datetime.now()

(now - data1).days
# %%
df 

# %%
