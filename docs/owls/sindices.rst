S-Indices
=========

If you use these S-index measurements in your work, please reach out to
`Brett <mailto:morrisbrettm@gmail.com>`_ to arrange citations for this database.

Interactive plot
----------------

Click a measurement below to find more information about the target.

.. altair-plot::
    :hide-code:

    import pandas as pd
    import altair as alt
    import numpy as np

    url = ('https://docs.google.com/spreadsheets/d/'
             '11Z7B76FXBkEwcGmhp72sC6AQdP8ER8K_eU5RAW8ed2M'
             '/gviz/tq?tqx=out:csv&sheet=sindices')
    df = pd.read_csv(url)

    df['spacelessnames'] = [line.replace(' ', '') for line in df['Target']]

    multiple_entries = []

    for i, target in enumerate(df['Target']):
        multiple_entries.append(i)

    input_dropdown = alt.binding_select(
        options=np.unique(df['Target']), name='Target'
    )

    highlight = alt.selection_single(on='click', fields=['Target'],
        init=dict(Target=False), bind=input_dropdown
    )

    # the base chart
    base = alt.Chart(df[['Date', 'Target', 'S', 'err', 'spacelessnames']].iloc[multiple_entries]).encode(
        x='Date:T',
        y=alt.X('S:Q', scale=alt.Scale(type='log')),
        color=alt.Color('Target:N', legend=None),
    ).transform_calculate(
        ymin="datum.S-datum.err",
        ymax="datum.S+datum.err",
        url=f'https://owls.readthedocs.io/en/latest/owls/targets/' + alt.datum.spacelessnames + '.html'
    )

    points = base.mark_circle().encode(
        opacity=alt.condition(highlight, alt.value(1), alt.value(0.5)),
        size=alt.condition(highlight, alt.value(100), alt.value(50)),
        href='url:N',
        tooltip='Target:N'
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
        size=alt.condition(~highlight, alt.value(2), alt.value(5)),
        opacity=alt.condition(highlight, alt.value(1), alt.value(0.))
    )

    # Draw text labels near the points, and highlight based on selection
    text = lines.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(highlight, 'Target:N', alt.value(' ')),
        size=alt.value(10)
    )

    (errorbars + points + lines + text)

