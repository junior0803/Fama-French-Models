import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as wx
from ipywidgets import interact
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from pandas.plotting import register_matplotlib_converters
from IPython.core.display import display, HTML
import famafrench
register_matplotlib_converters()

def create_factor_radios():
    return {
        'f_mer': wx.Checkbox(description='MER', indent=False, layout=chkbox_layout, value=True),
        'f_smb': wx.Checkbox(description='SMB', indent=False, layout=chkbox_layout, value=True),
        'f_hml': wx.Checkbox(description='HML', indent=False, layout=chkbox_layout, value=True),
        'f_rmw': wx.Checkbox(description='RMW', indent=False, layout=chkbox_layout),
        'f_cma': wx.Checkbox(description='CMA', indent=False, layout=chkbox_layout),
    }

def create_portfolio_dropdown():
    return wx.Dropdown(options=famafrench.portfolios.keys(), description='Portfolio', layout=wx.Layout(width='500px'))
def create_ma_radios(value):
    return wx.RadioButtons(value=value, options=famafrench.lookup_ma.keys(), description='Roll Avg')

chkbox_layout = wx.Layout(width='70px')
wx_pname = create_portfolio_dropdown()
wx_ma = create_ma_radios('3Y')
wx_factor_list = create_factor_radios()
wx_daterange=wx.SelectionRangeSlider(options=range(1960,2021), index=(0, len(range(1960,2021))-1), description='Range', continuous_update=False, layout=wx.Layout(width='500px'))
wx_out=wx.interactive_output(famafrench.fit_portfolio_returns, {'pname':wx_pname, **wx_factor_list , 'ma': wx_ma, 'daterange': wx_daterange})
wx_out.layout.height='700px'
wx_out_r2hist = wx.interactive_output(famafrench.draw_R2_hist, {'pname':wx_pname, 'daterange': wx_daterange})
wx_out_r2series = wx.interactive_output(famafrench.draw_R2_series, {'pname':wx_pname, **wx_factor_list, 'daterange': wx_daterange})
display(
    wx_pname, 
    wx.HBox([wx_daterange, *(wx_factor_list.values())]),
    wx.HBox([wx_out_r2hist, wx_out_r2series]),
    wx.HBox([wx_out, wx_ma]))