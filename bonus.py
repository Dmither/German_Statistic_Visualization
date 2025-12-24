import pandas as pd
import streamlit as st
import plotly.express as px
from choropleth_map import draw_st_choropleth_map

def bonus():
    files = [
        'germany_states_demographics.csv',
        'germany_states_economics.csv',
        'germany_states_socials.csv',
        'germany_states_infrastructure.csv',
        'germany_states_environment.csv',
        'germany_states_climate.csv'
    ]
    data_list = [pd.read_csv(file) for file in files]
    data = pd.merge(
        pd.merge(
        pd.merge(
            data_list[0], data_list[1], on='State', how="inner"
        ), data_list[2], on='State', how="inner"
        ), data_list[3], on='State', how="inner"
    )

    bonus_data = pd.read_csv('germany_states_uk_ru.csv')

    st.header('Bonus')

    (tab1,tab2,tab3) = st.tabs([
        'Heatmap',
        'Ukrainians',
        'Moskals',
    ])

    with tab1:
        st.subheader('Heatmap:')

        corr = data.corr(numeric_only=True)
        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="balance",
            zmin=-1,
            zmax=1
        )
        st.plotly_chart(fig)

    with tab2:
        ukrainians = bonus_data.sort_values('Ukrainians', ascending=False).set_index('State')[
            'Ukrainians']
        st.subheader('Ukrainians (%):')
        draw_st_choropleth_map(ukrainians, color='Greens', contrast=1, legend_num=5, legend_points=1)
        st.dataframe(ukrainians)
    with tab3:
        moskals = bonus_data.sort_values('Moskals', ascending=False).set_index('State')[
            'Moskals']
        st.subheader('Moskals (%):')
        draw_st_choropleth_map(moskals, color='Reds', contrast=1, legend_num=5, legend_points=1)
        st.dataframe(moskals)
