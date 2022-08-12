from astropy.utils.data import download_file
from zipfile import ZipFile

figshare_url = "https://figshare.com/ndownloader/articles/20480538/versions/3"
figshare_path_tmp = download_file(figshare_url, cache=False)
figshare_path = 'docs/owls/targets/figshare_pngs'

with ZipFile(figshare_path_tmp, 'r') as zip_ref:
    zip_ref.extractall(figshare_path)
