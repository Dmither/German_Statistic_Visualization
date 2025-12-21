import re
from typing import Literal
from lxml import etree

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def color_svg_paths(svg, color_map):
    root = etree.fromstring(svg.encode())
    SVG_NS = "http://www.w3.org/2000/svg"
    NSMAP = {"svg": SVG_NS}

    for path in root.xpath("//svg:path", namespaces=NSMAP):
        state_id = path.get("id")

        if state_id in color_map:
            path.set("fill", color_map[state_id])

    svg = etree.tostring(root, encoding="unicode")
    return svg

def get_contrast_text_color(hex_color):
    rgb = mcolors.to_rgb(hex_color)
    brightness = 0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2]
    return "#000000" if brightness > 0.5 else "#FFFFFF"


def draw_st_choropleth_map(metric: pd.Series, color:Literal[
'Greys'
'Purples'
'Blues'
'Greens'
'Oranges'
'Reds'
'YlOrBr'
'YlOrRd'
'OrRd'
'PuRd'
'RdPu'
'BuPu'
'GnBu'
'PuBu'
'YlGnBu'
'PuBuGn'
'BuGn'
'YlGn'
]='Greys', contrast:float=1, legend_num:int=5):
    """
    :param metric: a Series, where index is state and value is a numerical value for this state
    :param color: pick one option, see available colors
    :param contrast: should be between 0.5 and 3 including
    :param legend_num: numbers of legend blocks
    :return: None

    Available colors:
    - perceptually uniform: viridis, plasma, inferno, magma, cividis;
    - sequential: Greys, Purples, Blues, Greens, Oranges, Reds, YlOrBr, YlOrRd,
    OrRd, PuRd, RdPu, BuPu, GnBu, PuBu, YlGnBu, PuBuGn, BuGn, YlGn;
    - diverging: PiYG, PRGn, BrBG, PuOr, RdGy, RdBu, RdYlBu, RdYlGn, Spectral,
    coolwarm, bwr, seismic;
    - qualitative (categorical): tab10, tab20, tab20b, tab20c, Pastel1,
    Pastel2, Paired, Accent, Dark2, Set1, Set2, Set3;
    - cyclic: twilight, twilight_shifted, hsv;
    - miscellaneous: flag, prism, ocean, gist_earth, terrain, gist_stern,
    gnuplot, gnuplot2, CMRmap, cubehelix, brg, gist_rainbow, rainbow,
    jet
    """

    if not 0.5 <= contrast <= 3:
        raise ValueError('Contrast should be between 0.5 and 3 including')

    with open('map.svg', 'r') as file:
        map_svg = file.read()

    Q1 = metric.quantile(0.25)
    Q3 = metric.quantile(0.75)
    IQR = Q3 - Q1
    values = list(
        state for state in metric
        if Q1 - 1.5 * IQR <= state <= Q3 + 1.5 * IQR
    )
    vmin, vmax = min(values), max(values) / contrast
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    cmap = plt.cm.get_cmap(color)
    color_map = {state: mcolors.to_hex(cmap(norm(val))) for state, val in dict(zip(metric.index, metric.values)).items()}

    legend_values = np.linspace(vmin, vmax, legend_num)
    legend_colors = [mcolors.to_hex(cmap(norm(val))) for val in legend_values]

    legend_html = "<div style='display:flex; align-items:center;'>"
    for color, val in zip(legend_colors[:-1], legend_values[:-1]):
        legend_html += f"""
        <div style='background:{color}; width:80px; height:20px; margin-right:5px; display: flex; align-items: center; justify-content: center;'>
        """
        legend_html += f"<span style='text-align: center; color:{get_contrast_text_color(color)}'>{val:.0f}</span>"
        legend_html += "</div>"
    legend_html += f"""
            <div style='background:{legend_colors[-1]}; width:80px; height:20px; margin-right:5px; display: flex; align-items: center; justify-content: center;'>
            """
    legend_html += f"<span style='text-align: center; color:{get_contrast_text_color(legend_colors[-1])}'>more</span>"
    legend_html += "</div>"
    legend_html += "</div>"

    colored_svg = color_svg_paths(map_svg, color_map)

    st.markdown(colored_svg, unsafe_allow_html=True)
    st.text('')
    st.markdown(legend_html, unsafe_allow_html=True)
    st.text('')
