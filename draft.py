import re
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import plotly.express as px
from lxml import etree

def color_svg_paths(svg, color_map, value_map):
    root = etree.fromstring(svg.encode())
    SVG_NS = "http://www.w3.org/2000/svg"
    NSMAP = {"svg": SVG_NS}

    for path in root.xpath("//svg:path", namespaces=NSMAP):
        state_id = path.get("id")

        if state_id in color_map:
            path.set("fill", color_map[state_id])



    svg = etree.tostring(root, encoding="unicode")
    return svg

with open('map.svg', 'r') as file:
    map_svg = file.read()

demographics = pd.read_csv('./germany_states_demographics.csv')
metric = demographics.sort_values('Population Density', ascending=False).set_index('State')['Population Density']

Q1 = metric.quantile(0.25)
Q3 = metric.quantile(0.75)
IQR = Q3 - Q1
values = list(
    state for state in metric
    if Q1 - 1.5 * IQR <= state <= Q3 + 1.5 * IQR
)
vmin, vmax = min(values), max(values)
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
cmap = plt.cm.get_cmap('Greens')
color_map = {state: mcolors.to_hex(cmap(norm(val))) for state, val in dict(zip(metric.index, metric.values)).items()}

data=metric

colored_svg = color_svg_paths(
    svg=map_svg,
    color_map=color_map,
    value_map=data
)

tooltip_html = """
<div id='tooltip' style='display:none'>AAA</div>
<style>
#tooltip{
    width: 100px;
    position: absolute;
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    transform: translate(10px, -10px);
    pointer-events: none;
    z-index: 9999;
}
svg {
    overflow: visible;
}
svg path {
    position: relative;
}
svg path:hover {
    position: relative;
}
</style>
"""


st.markdown(tooltip_html, unsafe_allow_html=True)
st.markdown(colored_svg, unsafe_allow_html=True)
