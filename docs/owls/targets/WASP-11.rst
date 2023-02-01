WASP-11
=======

`Search exo.mast <https://exo.mast.stsci.edu/exomast_planet.html?planet=WASP11b>`_

`Search SIMBAD <http://simbad.cds.unistra.fr/simbad/sim-basic?Ident=WASP-11&submit=SIMBAD+search>`_

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
         <td>2021-01-06 7:40:40</td>
         <td>0.383</td>
         <td>0.023</td>
       </tr>
       <tr>
         <td>2021-10-29 7:00:16</td>
         <td>0.290</td>
         <td>0.013</td>
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
         <th>WASP-11</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <th>st_teff</th>
         <td>4800.0</td>
       </tr>
       <tr>
         <th>st_spectype</th>
         <td>K3 V</td>
       </tr>
       <tr>
         <th>st_rad</th>
         <td>0.89</td>
       </tr>
       <tr>
         <th>st_mass</th>
         <td>1.42</td>
       </tr>
       <tr>
         <th>st_rotp</th>
         <td>NaN</td>
       </tr>
       <tr>
         <th>sy_bmag</th>
         <td>12.575</td>
       </tr>
       <tr>
         <th>sy_vmag</th>
         <td>11.567</td>
       </tr>
       <tr>
         <th>sy_gaiamag</th>
         <td>11.5535</td>
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
       var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:0.2, target: "WASP-11"});
   </script>

TESS Light Curve
----------------

.. image:: figshare_pngs/WASP-11.png
  :width: 650
  :alt: WASP-11