import pandas as pd

urls = [
    ('https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=owls'),
    ('https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=sindices')
]

df_owls = pd.read_csv(urls[0])
df_sinds = pd.read_csv(urls[1])

page = dict()

targets_page = f"""Targets
=======

.. toctree::

"""

# Build individual webpages, one per target
for name, group in df_sinds.groupby('Target'):
    page[name] = group

    with open(f'docs/owls/targets/{name.replace(" ", "")}.rst', 'w') as f:
        f.write(name + '\n' + len(name) * '=' + '\n\n')
        f.write(".. raw:: html\n\n")
        f.write('   ' + '\n   '.join(
            group[['Date', 'S', 'err']].to_html(index=False).splitlines()
        ))

    targets_page += f'  targets/{name.replace(" ", "")}.rst\n'

# Write out targets.rst page
with open(f'docs/owls/targets.rst', 'w') as f:
    f.write(targets_page)
