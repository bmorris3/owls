from bokeh.models import HoverTool, ColumnDataSource, CustomJS
from bokeh.plotting import figure, show
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
from datetime import datetime

df_owls = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=owls'
)
df_owls.index = df_owls['pl_hostname']

df = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/'
     '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
     '/gviz/tq?tqx=out:csv&sheet=sindices'
)
targets = df['Target'].unique()

coords = dict()

for target in targets:
    try:
        coords[target] = SkyCoord.from_name(target)
    except:
        coords[target] = SkyCoord(ra=0*u.deg, dec=0*u.deg)

coord_names = list(coords.keys())
coord_vec = SkyCoord(list(coords.values()))


gb = df.groupby('Target')
target_names = []
RAs = []
Decs = []
dates = []
targets = []
sindices = []
teffs = []
errs = []
Bs = []
Vs = []

for group in gb.groups:
    per_target = df.iloc[gb.groups[group]]

    target_name = per_target['Target'].values[0]

    if target_name in df_owls['pl_hostname'].unique():
        owls_entry = df_owls.loc[target_name]

        RAs.append(owls_entry['ra'])
        Decs.append(owls_entry['dec'])
        target_names.append(target_name)
        dates.append(per_target['Date'].values)
        targets.append(per_target['Target'].values[0])
        sindices.append(per_target['S'].values)
        errs.append(per_target['err'].values)
        Bs.append(owls_entry['B'])
        Vs.append(owls_entry['V'])
        teffs.append(owls_entry['st_teff'])

TOOLTIPS = [
    ('Target', "@name"),
    ('B', "@B"),
    ('V', "@V"),
    ('Teff', "@teff"),
    ('S', "@S")
]
TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

coords_filtered = SkyCoord(ra=RAs, dec=Decs, unit=(u.hourangle, u.deg))
bminusv = np.ma.asarray(Bs) - np.ma.asarray(Vs)
source1 = dict(
    x=coords_filtered.ra.deg, y=coords_filtered.dec.deg,
    name=target_names,
    B=np.ma.asarray(Bs), V=np.ma.asarray(Vs),
    teff=np.ma.asarray(teffs),
    index=target_names,
    s_size=[np.log(100 * s.mean()) for s in sindices],
    S=[', '.join(["{0:.2f}±{1:.2f}".format(s, e) for s, e in zip(sinds, errors)])
       for sinds, errors in zip(sindices, errs)],
    BminusV=list(
        map(lambda x: to_hex(plt.cm.Spectral_r((x - 0.2) / 2)), bminusv))
)

p1 = figure(tools=TOOLS, tooltips=TOOLTIPS)
p1.scatter(source=source1, x='x', y='y', radius='s_size',
           fill_color='BminusV',
           line_color=None)

p1.yaxis.axis_label = "Declination [deg]"
p1.xaxis.axis_label = "Right Ascension [deg]"

p1.add_tools(HoverTool(show_arrow=True,
                       line_policy='nearest',
                       tooltips=TOOLTIPS,
                       ))

show(p1)