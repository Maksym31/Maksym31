import pandas as pd
df = pd.read_json('result.json')

subdf1 = df.groupby('team')[['aerial_won']].sum().sort_values('aerial_won')
print(subdf1)
subdf2 = df.groupby('team')[['total_pass']].sum().sort_values('total_pass')
print(subdf2)
subdf3 = df.groupby(['team','formation_used'])[['total_pass']].count().sort_values('total_pass')
print(subdf3)
subdf4 = df.groupby('opponent')[['fwd_pass']].sum().sort_values('fwd_pass')
print(subdf4)
subdf5 = df.groupby('team')[['touches']].mean().sort_values('touches')
print(subdf5)