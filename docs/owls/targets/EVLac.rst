EV Lac
======

`Search exo.mast <https://exo.mast.stsci.edu/exomast_planet.html?planet=EVLacb>`_

`Search SIMBAD <http://simbad.cds.unistra.fr/simbad/sim-basic?Ident=EV Lac&submit=SIMBAD+search>`_

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
         <td>9/11/2021 9:26:27</td>
         <td>9.614</td>
         <td>0.405</td>
       </tr>
       <tr>
         <td>9/13/2022 9:34:17</td>
         <td>11.345</td>
         <td>0.490</td>
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
       var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:0.2, target: "EV Lac"});
   </script>

TESS Light Curve
----------------

.. image:: figshare_pngs/EVLac.png
  :width: 650
  :alt: EVLac