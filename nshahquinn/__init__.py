import plotly.io as pio
import plotly.graph_objects as pgo

pio.templates["nsq"] = pgo.layout.Template(
    layout={
        "font": {
            "family": "Montserrat",
            "size": 16
        },
        "margin": {
            "t": 50,
            "r": 25,
            "b": 25,
            "l": 25
        }
    }
)


def set_plotly_defaults():
    pio.templates.default = "plotly+nsq"

    pio.renderers['jupyterlab'].config["toImageButtonOptions"] = {
        'format': 'png', # one of png, svg, jpeg, webp
        'filename': 'plotly_graph',
        'height': 625,
        'width': 1000,
        'scale': 2 # Multiply title/legend/axis/canvas sizes by this factor
    }
