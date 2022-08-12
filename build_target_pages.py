import os
import pandas as pd
from astroquery.ipac.nexsci.nasa_exoplanet_archive import (
    NasaExoplanetArchive, conf
)
from tqdm.auto import tqdm
from astropy.utils.data import download_file
from zipfile import ZipFile

conf.cache = True

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

figshare_url = "https://figshare.com/ndownloader/articles/20480538/versions/3"
figshare_path_tmp = download_file(figshare_url, cache=False)
figshare_path = 'docs/owls/targets/figshare_pngs'

with ZipFile(figshare_path_tmp, 'r') as zip_ref:
    zip_ref.extractall(figshare_path)

page = dict()

targets_page = f"""Targets
=======

.. toctree::

"""

params_to_write_out = [
    'st_teff', 'st_spectype', 'st_rad', 'st_mass', 'st_rotp',
    'sy_bmag', 'sy_vmag', 'sy_gaiamag'
]

aladin_lite = """<!-- include Aladin Lite CSS file in the head section of your page -->
<link rel="stylesheet" href="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.css" />
 
<!-- you can skip the following line if your page already integrates the jQuery library -->
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.1.min.js" charset="utf-8"></script>
 
<!-- insert this snippet where you want Aladin Lite viewer to appear and after the loading of jQuery -->
<div id="aladin-lite-div" style="width:400px;height:400px;"></div>
<script type="text/javascript" src="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.js" charset="utf-8"></script>
<script type="text/javascript">
    var aladin = A.aladin('#aladin-lite-div', {{survey: "P/DSS2/color", fov:0.2, target: "{0}"}});
</script>"""

embed_image = """.. image:: {0}
  :width: 650
  :alt: {1}"""

query_aliases = False

# Build individual webpages, one per target

pbar = tqdm(df_sinds.groupby('Target'))

for name, group in pbar:
    pbar.set_description(name)

    page[name] = group

    likely_planet_host = all([not name.startswith(key)
                              for key in ['HD', 'GJ']])
    if likely_planet_host:
        if query_aliases:
            aliases = NasaExoplanetArchive.query_aliases(
                f"{name.replace('.01', '')}", cache=True
            )
        nea = NasaExoplanetArchive.query_object(
            f"{name.replace('.01', '')} b" if not name.strip().endswith('A')
            else f"{name[:-1]} b",
            table="pscomppars", cache=True, regularize=False
        )
        if len(nea) > 0:
            nea_formatted = nea[params_to_write_out].to_pandas().transpose()
            nea_formatted.columns = [name]

    else:
        nea = []

    with open(f'docs/owls/targets/{name.replace(" ", "")}.rst', 'w') as f:
        f.write(name.replace('.01', '') + '\n' + len(name.replace('.01', '')) * '=' + '\n\n')
        f.write("`Search exo.mast <https://exo.mast.stsci.edu/exomast_planet.html?planet=" +
                f"{name.replace(' ', '').replace('-', '').replace('.01', '')}b>`_\n\n")
        f.write("`Search SIMBAD <http://simbad.cds.unistra.fr/simbad/sim-basic?"+
                f"Ident={name}&submit=SIMBAD+search>`_\n\n")

        f.write(".. raw:: html\n\n")
        f.write('   ' + '\n   '.join(
            group[['Date', 'S', 'err']].to_html(index=False).splitlines()
        ) + '\n\n')

        if len(nea) > 0:
            nea_header = '`NASA Exoplanet Archive <https://exoplanetarchive.ipac.caltech.edu>`_ parameters'
            f.write(nea_header + '\n' + len(nea_header) * '-' + '\n\n')

            if query_aliases:
                f.write("Aliases: " + ', '.join(aliases) + '\n\n')

            f.write(".. raw:: html\n\n")
            f.write('   ' + '\n   '.join(
                nea_formatted.to_html(index=True).splitlines()
            ) + '\n\n')

        f.write(".. raw:: html\n\n")
        f.write('   ' + '\n   '.join(
            aladin_lite.format(name.replace('.01', '')).splitlines()
        ) + '\n\n')

        png_path = f'figshare_pngs/{name.replace(".01", "").replace(" ", "")}.png'

        if os.path.exists(png_path):
            fs_header = 'TESS Light Curve'
            f.write(fs_header + '\n' + len(fs_header) * '-' + '\n\n')

            f.write(embed_image.format(png_path, name.replace('.01', '').replace(" ", "")))

    if not name.replace(" ", "") in targets_page:
        targets_page += f'  targets/{name.replace(" ", "")}.rst\n'



# Write out targets.rst page
with open(f'docs/owls/targets.rst', 'w') as f:
    f.write(targets_page)
