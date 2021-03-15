S-Indices
=========

The :math:`S`-index measurements for planet hosting stars are listed below, with
the date and time of observation, and the uncertainty in the S-index.

.. bokeh-plot:: owls/figures/bp.py
    :source-position: none

If you use these S-index measurements in your work, please reach out to
`Brett <mailto:morrisbrettm@gmail.com>`_ to arrange citations of this database.

.. altair-plot::
    :hide-code:

    import pandas as pd
    import altair as alt

    url = ('https://docs.google.com/spreadsheets/d/'
             '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
             '/gviz/tq?tqx=out:csv&sheet=sindices')
    df = pd.read_csv(url)

    highlight = alt.selection(type='single', on='mouseover',
                              fields=['Target'], nearest=True)
    # the base chart
    base = alt.Chart(df[['Date', 'Target', 'S', 'err']]).encode(
        x='Date:T',
        y=alt.X('S:Q', scale=alt.Scale(type='log')),
        color='Target:N'
    ).transform_calculate(
        ymin="datum.S-datum.err",
        ymax="datum.S+datum.err"
    )

    points = base.mark_circle().encode(
        opacity=alt.condition(highlight, alt.value(1), alt.value(0.5)),
        size=alt.condition(highlight, alt.value(100), alt.value(50))
    ).add_selection(
        highlight
    ).properties(
        width=600,
        height=600
    )

    errorbars = base.mark_errorbar().encode(
        x="Date:T",
        y=alt.Y("ymin:Q", title='S-index'),
        y2="ymax:Q"
    )


    lines = base.mark_line().encode(
        size=alt.condition(~highlight, alt.value(3), alt.value(5)),
        opacity=alt.condition(highlight, alt.value(1), alt.value(0.5))
    )


    # Draw text labels near the points, and highlight based on selection
    text = lines.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(highlight, 'Target:N', alt.value(' ')),
        size=alt.value(10)
    )

    (errorbars + points + lines + text).interactive()

.. raw:: html

    <embed>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th></th>
              <th>S</th>
              <th>err</th>
            </tr>
            <tr>
              <th>Target</th>
              <th>Date</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>2MASSJ17122552+3343384</th>
              <th>2020-07-06 07:09:54.679400</th>
              <td>1.435457</td>
              <td>0.059106</td>
            </tr>
            <tr>
              <th rowspan="7" valign="top">55 Cnc</th>
              <th>2021-01-05 10:49:13.649104</th>
              <td>0.192278</td>
              <td>0.008063</td>
            </tr>
            <tr>
              <th>2021-02-06 07:49:31.050900</th>
              <td>0.193850</td>
              <td>0.008084</td>
            </tr>
            <tr>
              <th>2021-02-06 07:57:14.219702</th>
              <td>0.192995</td>
              <td>0.008053</td>
            </tr>
            <tr>
              <th>2021-02-06 08:04:49.139020</th>
              <td>0.193199</td>
              <td>0.008061</td>
            </tr>
            <tr>
              <th>2021-02-20 08:41:26.069007</th>
              <td>0.199105</td>
              <td>0.008293</td>
            </tr>
            <tr>
              <th>2021-02-20 08:49:05.939054</th>
              <td>0.199017</td>
              <td>0.008292</td>
            </tr>
            <tr>
              <th>2021-02-20 08:56:39.570993</th>
              <td>0.198386</td>
              <td>0.008269</td>
            </tr>
            <tr>
              <th>AD Leo</th>
              <th>2021-02-06 08:39:31.507770</th>
              <td>9.469713</td>
              <td>0.392347</td>
            </tr>
            <tr>
              <th>BD+20 594</th>
              <th>2020-10-31 08:06:18.189795</th>
              <td>0.190947</td>
              <td>0.008635</td>
            </tr>
            <tr>
              <th>DS Leo</th>
              <th>2021-02-06 09:00:08.620995</th>
              <td>4.687123</td>
              <td>0.194442</td>
            </tr>
            <tr>
              <th>EPIC-211945201</th>
              <th>2021-01-06 09:05:51.509741</th>
              <td>0.149802</td>
              <td>0.006651</td>
            </tr>
            <tr>
              <th>GJ 338A</th>
              <th>2021-02-06 08:14:50.438958</th>
              <td>1.953923</td>
              <td>0.081028</td>
            </tr>
            <tr>
              <th>GJ 338B</th>
              <th>2021-02-06 08:25:00.180209</th>
              <td>1.986366</td>
              <td>0.082246</td>
            </tr>
            <tr>
              <th>GJ 436</th>
              <th>2021-01-06 12:21:39.907856</th>
              <td>0.817394</td>
              <td>0.035727</td>
            </tr>
            <tr>
              <th>Gliese 436</th>
              <th>2020-06-10 04:36:45.489895</th>
              <td>0.749116</td>
              <td>0.032333</td>
            </tr>
            <tr>
              <th>HAT-P-13</th>
              <th>2021-01-06 08:31:23.509330</th>
              <td>0.146181</td>
              <td>0.006694</td>
            </tr>
            <tr>
              <th>HAT-P-14</th>
              <th>2020-06-07 06:32:42.519832</th>
              <td>0.178182</td>
              <td>0.007566</td>
            </tr>
            <tr>
              <th>HAT-P-16</th>
              <th>2020-10-02 09:10:39.149179</th>
              <td>0.174709</td>
              <td>0.007560</td>
            </tr>
            <tr>
              <th>HAT-P-17</th>
              <th>2020-08-05 08:46:45.278984</th>
              <td>0.182186</td>
              <td>0.007993</td>
            </tr>
            <tr>
              <th>HAT-P-1</th>
              <th>2020-09-27 05:26:45.250369</th>
              <td>0.155731</td>
              <td>0.006933</td>
            </tr>
            <tr>
              <th>HAT-P-24</th>
              <th>2021-01-05 07:39:30.110406</th>
              <td>0.177322</td>
              <td>0.007801</td>
            </tr>
            <tr>
              <th>HAT-P-26</th>
              <th>2020-06-10 05:45:17.179482</th>
              <td>0.194043</td>
              <td>0.009098</td>
            </tr>
            <tr>
              <th>HAT-P-6</th>
              <th>2020-08-02 08:16:13.859024</th>
              <td>0.198598</td>
              <td>0.009290</td>
            </tr>
            <tr>
              <th>HAT-P-8</th>
              <th>2020-09-29 07:06:48.760433</th>
              <td>0.154384</td>
              <td>0.007454</td>
            </tr>
            <tr>
              <th>HD 119130</th>
              <th>2020-06-07 04:02:40.300787</th>
              <td>0.181205</td>
              <td>0.007835</td>
            </tr>
            <tr>
              <th>HD 149026</th>
              <th>2020-06-07 06:08:14.181226</th>
              <td>0.165060</td>
              <td>0.007045</td>
            </tr>
            <tr>
              <th>HD 17156</th>
              <th>2020-10-02 09:33:55.250477</th>
              <td>0.158136</td>
              <td>0.006784</td>
            </tr>
            <tr>
              <th rowspan="2" valign="top">HD 189733</th>
              <th>2020-07-02 08:44:43.698633</th>
              <td>0.577223</td>
              <td>0.023938</td>
            </tr>
            <tr>
              <th>2020-07-02 08:52:17.278752</th>
              <td>0.600969</td>
              <td>0.025585</td>
            </tr>
            <tr>
              <th rowspan="2" valign="top">HD 209458</th>
              <th>2020-08-02 07:24:51.279848</th>
              <td>0.167905</td>
              <td>0.007266</td>
            </tr>
            <tr>
              <th>2020-08-02 07:33:27.129313</th>
              <td>0.163470</td>
              <td>0.007041</td>
            </tr>
            <tr>
              <th rowspan="3" valign="top">HD 219134</th>
              <th>2020-08-02 07:47:07.460168</th>
              <td>0.296397</td>
              <td>0.014269</td>
            </tr>
            <tr>
              <th>2020-08-02 07:51:44.348829</th>
              <td>0.299908</td>
              <td>0.013349</td>
            </tr>
            <tr>
              <th>2020-08-02 07:56:20.169582</th>
              <td>0.284801</td>
              <td>0.012300</td>
            </tr>
            <tr>
              <th>HD 3167</th>
              <th>2020-08-02 08:50:10.031444</th>
              <td>0.199570</td>
              <td>0.008712</td>
            </tr>
            <tr>
              <th>HD 80606</th>
              <th>2020-06-10 02:58:20.489657</th>
              <td>0.174850</td>
              <td>0.007444</td>
            </tr>
            <tr>
              <th>HD 89345</th>
              <th>2021-01-06 10:11:02.791121</th>
              <td>0.164773</td>
              <td>0.007134</td>
            </tr>
            <tr>
              <th rowspan="2" valign="top">HD 97658</th>
              <th>2020-06-10 04:14:29.048622</th>
              <td>0.242906</td>
              <td>0.010142</td>
            </tr>
            <tr>
              <th>2021-01-06 12:42:17.960243</th>
              <td>0.232152</td>
              <td>0.009808</td>
            </tr>
            <tr>
              <th rowspan="2" valign="top">HD106315</th>
              <th>2020-06-07 03:18:57.070638</th>
              <td>0.299078</td>
              <td>0.018265</td>
            </tr>
            <tr>
              <th>2020-06-07 03:33:37.880626</th>
              <td>0.184965</td>
              <td>0.007823</td>
            </tr>
            <tr>
              <th>HD189733</th>
              <th>2020-09-27 07:04:03.779634</th>
              <td>0.546260</td>
              <td>0.022826</td>
            </tr>
            <tr>
              <th>HD80653</th>
              <th>2021-01-06 09:38:28.387680</th>
              <td>0.163855</td>
              <td>0.007115</td>
            </tr>
            <tr>
              <th>HIP 116454</th>
              <th>2020-08-02 09:22:45.009414</th>
              <td>0.302313</td>
              <td>0.013104</td>
            </tr>
            <tr>
              <th>K2-105</th>
              <th>2020-10-31 10:09:04.900914</th>
              <td>0.281662</td>
              <td>0.013148</td>
            </tr>
            <tr>
              <th>K2-111</th>
              <th>2020-10-02 10:37:14.979053</th>
              <td>0.160218</td>
              <td>0.007058</td>
            </tr>
            <tr>
              <th>K2-131</th>
              <th>2021-02-06 11:07:39.729807</th>
              <td>0.530798</td>
              <td>0.025967</td>
            </tr>
            <tr>
              <th>K2-136</th>
              <th>2020-10-02 11:10:24.192202</th>
              <td>1.463629</td>
              <td>0.062074</td>
            </tr>
            <tr>
              <th>K2-162</th>
              <th>2021-02-06 10:02:16.900230</th>
              <td>0.462411</td>
              <td>0.023068</td>
            </tr>
            <tr>
              <th>K2-182</th>
              <th>2021-01-05 09:23:38.552354</th>
              <td>0.423854</td>
              <td>0.018611</td>
            </tr>
            <tr>
              <th>K2-209</th>
              <th>2020-10-31 07:30:11.450592</th>
              <td>0.363052</td>
              <td>0.016888</td>
            </tr>
            <tr>
              <th>K2-222</th>
              <th>2020-10-02 08:04:08.239021</th>
              <td>0.176199</td>
              <td>0.007447</td>
            </tr>
            <tr>
              <th>K2-229</th>
              <th>2021-02-20 09:19:05.250155</th>
              <td>0.453186</td>
              <td>0.019253</td>
            </tr>
            <tr>
              <th>K2-232</th>
              <th>2020-10-31 08:39:50.920137</th>
              <td>0.172170</td>
              <td>0.007369</td>
            </tr>
            <tr>
              <th>K2-244</th>
              <th>2021-02-06 10:35:00.500925</th>
              <td>0.253501</td>
              <td>0.011691</td>
            </tr>
            <tr>
              <th>K2-261</th>
              <th>2021-01-06 11:49:05.578766</th>
              <td>0.260283</td>
              <td>0.012164</td>
            </tr>
            <tr>
              <th>K2-263</th>
              <th>2020-10-31 10:43:35.788816</th>
              <td>0.194842</td>
              <td>0.008887</td>
            </tr>
            <tr>
              <th>K2-266</th>
              <th>2021-01-05 11:17:39.250756</th>
              <td>0.376427</td>
              <td>0.017925</td>
            </tr>
            <tr>
              <th>K2-285</th>
              <th>2020-09-29 06:01:27.920626</th>
              <td>0.403200</td>
              <td>0.020138</td>
            </tr>
            <tr>
              <th>K2-291</th>
              <th>2020-10-02 11:44:08.989145</th>
              <td>0.295287</td>
              <td>0.012215</td>
            </tr>
            <tr>
              <th>K2-3</th>
              <th>2021-01-05 11:50:13.878818</th>
              <td>1.110212</td>
              <td>0.050464</td>
            </tr>
            <tr>
              <th>K2-65</th>
              <th>2020-09-29 04:55:15.850841</th>
              <td>0.367762</td>
              <td>0.019112</td>
            </tr>
            <tr>
              <th>K2-77</th>
              <th>2020-10-06 10:20:40.871027</th>
              <td>0.568361</td>
              <td>0.025576</td>
            </tr>
            <tr>
              <th>KELT-18</th>
              <th>2020-09-29 02:30:40.760337</th>
              <td>0.263926</td>
              <td>0.012111</td>
            </tr>
            <tr>
              <th>KELT-23A</th>
              <th>2020-09-29 03:07:01.790108</th>
              <td>0.162068</td>
              <td>0.008728</td>
            </tr>
            <tr>
              <th>KELT-2</th>
              <th>2020-10-31 09:41:29.400016</th>
              <td>0.154043</td>
              <td>0.006602</td>
            </tr>
            <tr>
              <th>KELT-7</th>
              <th>2021-01-06 08:05:46.607991</th>
              <td>0.241517</td>
              <td>0.009987</td>
            </tr>
            <tr>
              <th>Kelt-8</th>
              <th>2020-09-27 02:38:22.839665</th>
              <td>0.170000</td>
              <td>0.007461</td>
            </tr>
            <tr>
              <th>Kepler 37</th>
              <th>2020-09-27 03:14:01.230159</th>
              <td>0.229122</td>
              <td>0.009563</td>
            </tr>
            <tr>
              <th>Kepler 408</th>
              <th>2020-09-27 03:43:37.030062</th>
              <td>0.158708</td>
              <td>0.006773</td>
            </tr>
            <tr>
              <th>Kepler 409</th>
              <th>2020-09-27 04:12:49.810456</th>
              <td>0.174710</td>
              <td>0.007439</td>
            </tr>
            <tr>
              <th>Kepler-102</th>
              <th>2020-09-27 02:00:46.640155</th>
              <td>0.506344</td>
              <td>0.022445</td>
            </tr>
            <tr>
              <th>Kepler-10</th>
              <th>2020-09-29 04:15:53.500307</th>
              <td>0.258214</td>
              <td>0.013024</td>
            </tr>
            <tr>
              <th>Kepler-21</th>
              <th>2020-07-06 10:59:27.067502</th>
              <td>0.220324</td>
              <td>0.011891</td>
            </tr>
            <tr>
              <th>Kepler-410A</th>
              <th>2020-09-29 03:42:57.830395</th>
              <td>0.146883</td>
              <td>0.006567</td>
            </tr>
            <tr>
              <th>Kepler-444,</th>
              <th>2020-07-06 10:40:16.310196</th>
              <td>0.168951</td>
              <td>0.007355</td>
            </tr>
            <tr>
              <th>Kepler-68</th>
              <th>2020-09-27 04:47:23.730126</th>
              <td>0.162178</td>
              <td>0.006996</td>
            </tr>
            <tr>
              <th>Kepler-96</th>
              <th>2020-09-27 06:02:51.680260</th>
              <td>0.289933</td>
              <td>0.012397</td>
            </tr>
            <tr>
              <th>Qatar 6</th>
              <th>2020-06-10 06:18:16.460076</th>
              <td>0.612936</td>
              <td>0.026039</td>
            </tr>
            <tr>
              <th>TOI 1180</th>
              <th>2021-03-03 10:46:06.180114</th>
              <td>0.468931</td>
              <td>0.021855</td>
            </tr>
            <tr>
              <th>TOI 1260</th>
              <th>2021-03-03 07:58:49.059260</th>
              <td>1.071458</td>
              <td>0.050740</td>
            </tr>
            <tr>
              <th>TOI 1411</th>
              <th>2021-03-03 11:11:14.089055</th>
              <td>1.151526</td>
              <td>0.050728</td>
            </tr>
            <tr>
              <th>TOI 1416</th>
              <th>2021-02-20 10:47:27.570620</th>
              <td>0.323840</td>
              <td>0.013459</td>
            </tr>
            <tr>
              <th>TOI 1693</th>
              <th>2021-02-20 07:12:15.329935</th>
              <td>0.617835</td>
              <td>0.042675</td>
            </tr>
            <tr>
              <th>TOI 1701</th>
              <th>2021-02-20 07:44:53.839972</th>
              <td>0.392439</td>
              <td>0.019686</td>
            </tr>
            <tr>
              <th>TOI 1730</th>
              <th>2021-02-20 08:18:48.351729</th>
              <td>0.987623</td>
              <td>0.052394</td>
            </tr>
            <tr>
              <th>TOI 1801</th>
              <th>2021-02-06 09:28:31.078548</th>
              <td>2.340220</td>
              <td>0.100339</td>
            </tr>
            <tr>
              <th>TOI 1807</th>
              <th>2021-03-03 10:13:23.168634</th>
              <td>1.010801</td>
              <td>0.042054</td>
            </tr>
            <tr>
              <th>TOI 1823</th>
              <th>2021-03-03 09:40:22.691426</th>
              <td>0.395286</td>
              <td>0.017120</td>
            </tr>
            <tr>
              <th>TOI 1827</th>
              <th>2021-02-20 10:19:53.639620</th>
              <td>0.710629</td>
              <td>0.032573</td>
            </tr>
            <tr>
              <th>TOI 2018</th>
              <th>2021-02-20 11:15:37.730031</th>
              <td>1.132817</td>
              <td>0.047469</td>
            </tr>
            <tr>
              <th>TOI 2079</th>
              <th>2021-03-03 09:07:34.429440</th>
              <td>0.300977</td>
              <td>0.020624</td>
            </tr>
            <tr>
              <th>TOI 2104</th>
              <th>2021-03-03 07:24:54.789425</th>
              <td>0.405837</td>
              <td>0.018410</td>
            </tr>
            <tr>
              <th>TOI 2105</th>
              <th>2021-03-03 08:34:57.927359</th>
              <td>0.395933</td>
              <td>0.018326</td>
            </tr>
            <tr>
              <th>TrES-4</th>
              <th>2020-06-07 06:59:17.791284</th>
              <td>0.155919</td>
              <td>0.007618</td>
            </tr>
            <tr>
              <th>WASP 52</th>
              <th>2020-10-02 07:28:51.401861</th>
              <td>0.535647</td>
              <td>0.024027</td>
            </tr>
            <tr>
              <th>WASP 93</th>
              <th>2020-10-02 08:37:57.788825</th>
              <td>0.219129</td>
              <td>0.009266</td>
            </tr>
            <tr>
              <th>WASP-106</th>
              <th>2021-01-06 11:16:28.750072</th>
              <td>0.222759</td>
              <td>0.010285</td>
            </tr>
            <tr>
              <th rowspan="2" valign="top">WASP-107</th>
              <th>2021-02-06 11:35:14.108361</th>
              <td>0.903957</td>
              <td>0.048056</td>
            </tr>
            <tr>
              <th>2021-02-20 09:51:42.998096</th>
              <td>0.964473</td>
              <td>0.044743</td>
            </tr>
            <tr>
              <th>WASP-113</th>
              <th>2020-06-07 05:11:03.759921</th>
              <td>0.161444</td>
              <td>0.007871</td>
            </tr>
            <tr>
              <th>WASP-11</th>
              <th>2021-01-06 07:40:39.800633</th>
              <td>0.410321</td>
              <td>0.021583</td>
            </tr>
            <tr>
              <th>WASP-127</th>
              <th>2021-01-06 10:43:39.589520</th>
              <td>0.170009</td>
              <td>0.007400</td>
            </tr>
            <tr>
              <th>WASP-13</th>
              <th>2021-01-05 10:29:42.160990</th>
              <td>0.164105</td>
              <td>0.007116</td>
            </tr>
            <tr>
              <th>WASP-14</th>
              <th>2020-06-07 04:35:19.028525</th>
              <td>0.170026</td>
              <td>0.007312</td>
            </tr>
            <tr>
              <th>WASP-35</th>
              <th>2020-10-31 09:12:29.160571</th>
              <td>0.178577</td>
              <td>0.007858</td>
            </tr>
            <tr>
              <th>WASP-38</th>
              <th>2020-06-07 05:44:56.130712</th>
              <td>0.165328</td>
              <td>0.007064</td>
            </tr>
            <tr>
              <th>WASP-47</th>
              <th>2020-08-05 09:14:51.331758</th>
              <td>0.205374</td>
              <td>0.010679</td>
            </tr>
            <tr>
              <th>WASP-65</th>
              <th>2021-01-05 09:56:29.999034</th>
              <td>0.252413</td>
              <td>0.011172</td>
            </tr>
            <tr>
              <th>WASP-69</th>
              <th>2020-08-05 07:40:50.870217</th>
              <td>0.817902</td>
              <td>0.033983</td>
            </tr>
            <tr>
              <th>WASP-80</th>
              <th>2020-09-29 05:28:04.321073</th>
              <td>0.382145</td>
              <td>0.032443</td>
            </tr>
            <tr>
              <th>WASP-84</th>
              <th>2020-10-31 11:16:37.630289</th>
              <td>0.508729</td>
              <td>0.021288</td>
            </tr>
            <tr>
              <th>WASP-90</th>
              <th>2020-08-05 08:13:39.960764</th>
              <td>0.165840</td>
              <td>0.007591</td>
            </tr>
            <tr>
              <th>Wolf 503</th>
              <th>2020-06-10 05:12:09.091291</th>
              <td>0.290947</td>
              <td>0.012529</td>
            </tr>
            <tr>
              <th>XO-1</th>
              <th>2020-06-10 06:50:52.270067</th>
              <td>0.231123</td>
              <td>0.009858</td>
            </tr>
            <tr>
              <th>XO-2 N</th>
              <th>2021-01-05 08:48:32.980029</th>
              <td>0.195795</td>
              <td>0.008712</td>
            </tr>
            <tr>
              <th>XO-4</th>
              <th>2021-01-05 08:14:59.059953</th>
              <td>0.172461</td>
              <td>0.007381</td>
            </tr>
            <tr>
              <th>YZ CMi</th>
              <th>2021-02-06 07:28:48.028795</th>
              <td>0.403284</td>
              <td>0.019000</td>
            </tr>
            <tr>
              <th>corot7</th>
              <th>2020-10-06 11:29:06.901421</th>
              <td>1.616847</td>
              <td>0.074871</td>
            </tr>
            <tr>
              <th>gj3470</th>
              <th>2020-10-06 12:09:53.606879</th>
              <td>0.288826</td>
              <td>0.012136</td>
            </tr>
            <tr>
              <th>hat-p-20</th>
              <th>2020-10-02 12:33:58.780814</th>
              <td>0.729760</td>
              <td>0.029793</td>
            </tr>
            <tr>
              <th>kelt-24</th>
              <th>2020-06-10 03:58:33.439603</th>
              <td>0.201734</td>
              <td>0.008445</td>
            </tr>
            <tr>
              <th>qatar-8</th>
              <th>2020-06-10 03:33:14.370353</th>
              <td>0.177423</td>
              <td>0.008104</td>
            </tr>
          </tbody>
        </table>
    </embed>
