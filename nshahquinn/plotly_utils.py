from pathlib import Path
import pandas as pd
import plotly.graph_objects as pgo
import plotly.io as pio


def set_theme():
    pio.templates["nsq"] = pgo.layout.Template(
        layout=dict(
            width=1000,
            height=600,
            font=dict(
                # For display in JupyterLab, the font must be installed on your own computer
                # For Kaleido PNG export, the font must be in ~/.fonts on the stat host
                family="Montserrat",
                size=20,
                color="#000000",
                # Ideally, it would be the medium weight rather than the regular, but I haven't found
                # a way to make that work with Kaleido PNG export
            ),
            margin=dict(
                t=25,
                r=25,
                b=25,
                l=25
            ),
            legend_font_size=22,
            title=dict(
                pad_t=10,
                automargin=True,
            ),
            colorway=["#3366cc", "#f9955c", "#009988", "#861556", "#da2901"],
            xaxis_showgrid=False,
            yaxis=dict(
                ticklabelstandoff=5,
                zeroline=True,
                zerolinewidth=3,
            ),
        ),
        data_scatter=[pgo.Scatter(
            line_width=3,
        )]
    )

    pio.templates.default = "plotly_white+nsq"
    pio.kaleido.scope.default_scale = 3


def output_fig(
    fig,
    name,
    # The default assumption is that I'm working in a notebook in the `notebooks` folder of
    # a project repo
    image=True,
    html=True,
    directory="../figures",
):
    directory = Path(directory)
    try:
        directory.resolve()
    except FileNotFoundError:
        # Only support creating one directory level
        directory.mkdir(parents=False)
        directory.resolve()
    
    fig.show()
    
    if image:
        fig.write_image(
            directory / f"{name}.png",
            scale=3,
            # Validation already happened during fig.show
            validate=False,
        )
    
    if html:
        fig.write_html(
            directory / f"{name}.html",
            full_html=False,
            include_plotlyjs=False,
            # Validation already happened during fig.show
            validate=False,
        )


def time_position(t):
    """
    Converts a (date)time into milliseconds since the Unix epoch, which is the only format
    Plotly accepts for specifying shape positions along a (date)time axis. This works
    around https://github.com/plotly/plotly.py/issues/3065.
    """
    return t.timestamp() * 1000

def add_vline(
    fig,
    t,
    annotation_text,
    annotation_position="top left",
    annotation_align="right",
    annotation_font_size=12,
    annotation_borderpad=5,
    **kwargs,
):  
    try:
        x = time_position(t)
    # e.g. if t is a string rather than a pandas.Timestamp
    except AttributeError:
        x = time_position(pd.Timestamp(t))
                                
    fig.add_vline(
        x=x,
        annotation_text=annotation_text,
        annotation_position=annotation_position,
        annotation_align=annotation_align,
        annotation_font_size=annotation_font_size,
        annotation_borderpad=annotation_borderpad,
        line_width=1,
        **kwargs,
    )
