# %%
import pandas as pd 
import sqlalchemy

# %%
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')
engine

# %%
df_transactions_cart = pd.read_sql_table('transactions_cart', engine)
df_transactions_cart

# %%
query = 'SELECT * FROM customers LIMIT 10'

df_customers = pd.read_sql_query(query, engine)
df_customers

# %%
query = '''
    SELECT * 
    FROM customers AS t1
    LEFT JOIN transactions AS t2
    ON t1.UUID = t2.IdCustomer
    LIMIT 10
'''

df_join = pd.read_sql_query(query, engine)
df_join

# %%
