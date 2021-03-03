import pandas as pd

sheets = [
    'owls',
    'sindices'
]

urls = [
    ('https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=owls'),
    ('https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=sindices')
]

for url, sheet in zip(urls, sheets):
    df = pd.read_csv(url)
    df.to_csv(f"owls/data/{sheet}.csv")