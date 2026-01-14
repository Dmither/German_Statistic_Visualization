import pandas as pd
import streamlit as st

from choropleth_map import draw_st_choropleth_map


def tourism_rent():
    tourism_rent = pd.read_csv('germany_states_tourism_rent.csv')

    st.header('Tourism and rent')

    tab1, tab2 = st.tabs([
        'Tourism pressure',
        'Cost of rent',
    ])

    with tab1:
        tourism = tourism_rent.sort_values('Tourism_pressure', ascending=False).set_index('State')['Tourism_pressure']
        st.subheader('Tourism pressure overnights per 1000 inhabitants:')
        draw_st_choropleth_map(tourism, color='Purples', contrast=1.2, legend_num=10, legend_points=1)
        st.dataframe(tourism)

    with tab2:
        rent = tourism_rent.sort_values('Average_rent_per_sqm', ascending=False).set_index('State')['Average_rent_per_sqm']
        st.subheader('Average rent per square meter:')
        draw_st_choropleth_map(rent, color='Oranges', legend_num=10, legend_points=1)
        st.dataframe(rent)
