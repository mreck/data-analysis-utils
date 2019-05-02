%%javascript
IPython.OutputArea.prototype._should_scroll = function(lines) { return false; };


##### imports ###################################


import numpy as np
import pandas as pd

from IPython.core.display import display, HTML

import matplotlib.pyplot as plt

import seaborn as sns

from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10

output_notebook()


##### misc ######################################


def print_html(html_txt, center=True, h=None, raw=False):
    if not raw:
        if center:
            html_txt = '<center>{}</center>'.format(html_txt)
        if h:
            html_txt = '<h{}>{}</h{}>'.format(h, html_txt, h)
    display(HTML(html_txt))


def combine_other(df, column, top=10, name='other'):
    if len(d[column].unique()) > top:
        most_common = d[column].value_counts()[:top].index
        d.loc[~d[column].isin(most_common), column] = name


def flatten_columns(df):
    df.columns = ["_".join(x).rstrip('_') for x in df.columns.ravel()]

    
def figsize(w=16, h=10):
    plt.rcParams["figure.figsize"] = (w,h)


figsize()


##### plotting ##################################


def date_time_scatter_plot(x, y, src, category, categories, size=(950,950)):
    p = figure(plot_width = size[0],
               plot_height = size[1],
               x_axis_type = 'datetime',
               y_axis_type = 'datetime')

    for i, c in enumerate(categories):
        p.circle(source = src[src[category]==c],
                 x = x,
                 y = y,
                 size = 5,
                 alpha = .7,
                 color = Category10[10][i],
                 legend = category)

    show(p)
   
