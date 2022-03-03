S-Indices
=========

The :math:`S`-index measurements for planet hosting stars are listed below, with
the date and time of observation, and the uncertainty in the S-index.

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
    :file: db.html