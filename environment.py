import pandas as pd
import streamlit as st

from choropleth_map import draw_st_choropleth_map


def environment():
    environment = pd.read_csv('germany_states_environment.csv')

    st.header('Environment')

    tab1, tab2, tab3 = st.tabs([
        'CO2 emissions',
        'Air quality',
        'Water quality',
    ])

    with tab1:
        st.subheader('CO₂ emissions per capita (t CO₂e/person)')
        co2 = environment.sort_values(
            'CO2_emissions_per_capita_tonnes', ascending=False
        ).set_index('State')['CO2_emissions_per_capita_tonnes']
        draw_st_choropleth_map(co2, "Oranges", contrast=1, legend_num=10, legend_points=1)
        st.dataframe(co2)

    with tab2:
        st.subheader('Air quality – PM2.5 annual mean (µg/m³)')
        air = environment.sort_values(
            'PM2_5_annual_mean_ug_m3', ascending=False
        ).set_index('State')['PM2_5_annual_mean_ug_m3']
        draw_st_choropleth_map(air, "RdYlGn_r", contrast=1, legend_num=10, legend_points=1)
        st.dataframe(air)

    with tab3:
        st.subheader('Water quality – Bathing waters “excellent” (%)')
        water = environment.sort_values(
            'Bathing_water_excellent_percent', ascending=False
        ).set_index('State')['Bathing_water_excellent_percent']
        draw_st_choropleth_map(water, "Blues", contrast=1, legend_num=10)
        st.dataframe(water)
