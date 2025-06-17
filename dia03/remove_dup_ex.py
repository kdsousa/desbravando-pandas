# %%
import pandas as pd

df = pd.read_excel('../data/transactions.xlsx')
df

# %%
df = (df.sort_values('DtTransaction', ascending=False)
   .drop_duplicates(subset=['IdCustomer'], keep='first')
)

# %%
df['IdCustomer'].nunique()

# %%
