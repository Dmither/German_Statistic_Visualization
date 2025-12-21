import pandas as pd
import streamlit as st
import plotly.express as px

from choropleth_map import draw_st_choropleth_map


def socials():
    socials = pd.read_csv('germany_states_socials.csv')

    st.header('Socials')

    tab1, tab2, tab3 = st.tabs([
        'Education level',
        'Number of universities',
        'Crime rates',
    ])

    with tab1:
        st.subheader('Tertiary education (%)')
        education = socials.sort_values(
            'Tertiary_education_percent', ascending=False
        ).set_index('State')['Tertiary_education_percent']
        draw_st_choropleth_map(education, "YlGnBu", contrast=1, legend_num=10)
        st.dataframe(education)

    with tab2:
        st.subheader('Number of universities')
        universities = socials.sort_values(
            'Universities', ascending=False
        ).set_index('State')['Universities']
        fig = px.bar(
            data_frame=universities,
            y=universities.index,
            x=universities.values,
            labels={"x": "GDP billion EUR", "y": "State"},
        )
        fig.update_traces(marker_color="#1F80B8")
        st.plotly_chart(fig)
        st.dataframe(universities)

    with tab3:
        st.subheader('Crime rates')
        crime_rates = socials.sort_values(
            'Crime_rate_per_100000', ascending=False
        ).set_index('State')['Crime_rate_per_100000']
        draw_st_choropleth_map(crime_rates, "Reds", contrast=1.1, legend_num=10)
        st.dataframe(crime_rates)
