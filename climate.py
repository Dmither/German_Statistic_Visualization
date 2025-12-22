import pandas as pd
import streamlit as st

from choropleth_map import draw_st_choropleth_map


def climate():
    climate = pd.read_csv('germany_states_climate.csv')

    st.header('Climate')

    tab1, tab2, tab3 = st.tabs([
        'Temperature',
        'Rainfall',
        'Wind speed',
    ])

    with tab1:
        temp_tab1, temp_tab2 = st.tabs([
            'January',
            'July',
        ])
        with temp_tab1:
            st.subheader('Average January Temp (°C) ')
            temp_jan = climate.sort_values(
                'Avg_Jan_Temp_C', ascending=False
            ).set_index('State')['Avg_Jan_Temp_C']
            draw_st_choropleth_map(temp_jan, "Blues_r", contrast=1, legend_num=10, legend_points=1)
            st.dataframe(temp_jan)
        with temp_tab2:
            st.subheader('Average July Temp (°C) ')
            temp_jul = climate.sort_values(
                'Avg_Jul_Temp_C', ascending=False
            ).set_index('State')['Avg_Jul_Temp_C']
            draw_st_choropleth_map(temp_jul, "Oranges", contrast=1, legend_num=10, legend_points=1)
            st.dataframe(temp_jul)

    with tab2:
        st.subheader('Annual rainfall (mm)')
        air = climate.sort_values(
            'Annual_Rain_mm', ascending=False
        ).set_index('State')['Annual_Rain_mm']
        draw_st_choropleth_map(air, "Blues", contrast=1, legend_num=10)
        st.dataframe(air)

    with tab3:
        st.subheader('Average wind speed (km/h)')
        water = climate.sort_values(
            'Avg_Wind_km_h', ascending=False
        ).set_index('State')['Avg_Wind_km_h']
        draw_st_choropleth_map(water, "Blues", contrast=1, legend_num=10, )
        st.dataframe(water)
