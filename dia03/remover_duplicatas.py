# %%
import pandas as pd

data = {'Nome': ['Téo', 'Nah', 'Maria', 'Nah', 'Lara', 'Téo'],
        'idade': [32, 33, 2, 33, 31, 32],
        'updated_at': [1, 2, 3, 1, 2, 3]}

# %%
df = pd.DataFrame(data)

# %%
df.drop_duplicates()

# %%
df.drop_duplicates(subset=['Nome', 'idade'])

# %%
df
# %%
