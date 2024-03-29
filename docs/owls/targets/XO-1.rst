XO-1
====

`Search exo.mast <https://exo.mast.stsci.edu/exomast_planet.html?planet=XO1b>`_

`Search SIMBAD <http://simbad.cds.unistra.fr/simbad/sim-basic?Ident=XO-1&submit=SIMBAD+search>`_

.. raw:: html

   <table border="1" class="dataframe">
     <thead>
       <tr style="text-align: right;">
         <th>Date</th>
         <th>S</th>
         <th>err</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td>2020-06-10 6:50:52</td>
         <td>0.219</td>
         <td>0.009</td>
       </tr>
     </tbody>
   </table>

`NASA Exoplanet Archive <https://exoplanetarchive.ipac.caltech.edu>`_ parameters
--------------------------------------------------------------------------------

.. raw:: html

   <table border="1" class="dataframe">
     <thead>
       <tr style="text-align: right;">
         <th></th>
         <th>XO-1</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <th>st_teff</th>
         <td>5750.0</td>
       </tr>
       <tr>
         <th>st_spectype</th>
         <td>G1 V</td>
       </tr>
       <tr>
         <th>st_rad</th>
         <td>0.88</td>
       </tr>
       <tr>
         <th>st_mass</th>
         <td>0.88</td>
       </tr>
       <tr>
         <th>st_rotp</th>
         <td>NaN</td>
       </tr>
       <tr>
         <th>sy_bmag</th>
         <td>11.878</td>
       </tr>
       <tr>
         <th>sy_vmag</th>
         <td>11.251</td>
       </tr>
       <tr>
         <th>sy_gaiamag</th>
         <td>11.004</td>
       </tr>
     </tbody>
   </table>

.. raw:: html

   <!-- include Aladin Lite CSS file in the head section of your page -->
   <link rel="stylesheet" href="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.css" />
    
   <!-- you can skip the following line if your page already integrates the jQuery library -->
   <script type="text/javascript" src="https://code.jquery.com/jquery-1.12.1.min.js" charset="utf-8"></script>
    
   <!-- insert this snippet where you want Aladin Lite viewer to appear and after the loading of jQuery -->
   <div id="aladin-lite-div" style="width:400px;height:400px;"></div>
   <script type="text/javascript" src="https://aladin.u-strasbg.fr/AladinLite/api/v2/latest/aladin.min.js" charset="utf-8"></script>
   <script type="text/javascript">
       var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:0.2, target: "XO-1"});
   </script>

TESS Light Curve
----------------

.. image:: figshare_pngs/XO-1.png
  :width: 650
  :alt: XO-1