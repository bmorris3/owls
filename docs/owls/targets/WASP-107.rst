WASP-107
========

`Search exo.mast <https://exo.mast.stsci.edu/exomast_planet.html?planet=WASP107b>`_

`Search SIMBAD <http://simbad.cds.unistra.fr/simbad/sim-basic?Ident=WASP-107&submit=SIMBAD+search>`_

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
         <td>2/6/21 11:35</td>
         <td>0.828252</td>
         <td>0.050076</td>
       </tr>
       <tr>
         <td>2/20/21 9:51</td>
         <td>0.888993</td>
         <td>0.044313</td>
       </tr>
       <tr>
         <td>3/20/22 6:43</td>
         <td>0.877483</td>
         <td>0.041541</td>
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
         <th>WASP-107</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <th>st_teff</th>
         <td>4425</td>
       </tr>
       <tr>
         <th>st_spectype</th>
         <td>K6</td>
       </tr>
       <tr>
         <th>st_rad</th>
         <td>0.67</td>
       </tr>
       <tr>
         <th>st_mass</th>
         <td>0.68</td>
       </tr>
       <tr>
         <th>st_rotp</th>
         <td>17</td>
       </tr>
       <tr>
         <th>sy_bmag</th>
         <td>14.913</td>
       </tr>
       <tr>
         <th>sy_vmag</th>
         <td>11.592</td>
       </tr>
       <tr>
         <th>sy_gaiamag</th>
         <td>11.174</td>
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
       var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:0.2, target: "WASP-107"});
   </script>

