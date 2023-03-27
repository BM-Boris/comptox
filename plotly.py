import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objs as go
import plotly.offline as offline

def Plotly_3D(x_axis, y_axis, z_axis, labels, marker_size, title_name, output_html_name):
    trace = go.Scatter3d(
        x = x_axis,
        y = y_axis,
        z = z_axis,
        mode='markers',
        marker=dict(
            size=marker_size,
            colorscale='Viridis',
            opacity=0.7, 
        ),
        text = labels,
        hoverinfo='text'
    )

    # create a layout
    layout = go.Layout(
        title=title_name,
        scene=dict(
            xaxis=dict(title=''),
            yaxis=dict(title=''),
            zaxis=dict(title=''),
            aspectmode='cube'
        )
    )

    # create a figure
    fig = go.Figure(data=[trace], layout=layout)
    offline.plot(fig, filename=output_html_name, auto_open=True)