from dash import  html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.utils import app_description
from utils.other_components import  up_next, make_md, make_feature_card, make_img_card
import utils.links as links

register_page(
    __name__, description=app_description, title="Dash AG Grid Examples: dbc components", path=links.components_dbc
)


text1 = """
# Custom Components Examples

Here are some examples of using Dash Bootstrap Components in Dash AG Grid cells.  

For more information, please see the [Components](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) section of the Dash AG Grid docs.
 
## dbc.Progress
"""

text2 = """
## dbc.Button with icons
"""

text3 = """
## dbc.Spinner

See a use-case in the docs [Infinite Row Model with Loading Spinner](https://dash.plotly.com/dash-ag-grid/infinite-row-model#loading-spinner)
"""

text4="""
## dbc.Switch

"""


text5="""
## dbc.DropdownMenu

The trick to making this work is to add some CSS so that when the button is clicked, the focused row has a
lower z-index, which makes the menu visible. 

Place this in a `.css` file in the `assets` folder
```
.ag-row-focus {
    z-index: 999;
}
```

"""

next  =f'<dccLink href="{links.get_started_V31}" children="Getting Started with Dash AG Grid V31" />'

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_renderer_dbc_progress", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_renderer_dbc_button", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.cell_renderer_dbc_spinner", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.dbc_switch", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.dbc_dropdownmenu", make_layout=make_tabs),
        up_next()
    ],
)
