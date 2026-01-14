import pandas as pd
import streamlit as st
import plotly.express as px


def cities():
    cities = pd.read_csv('./germany_big_cities.csv', index_col=0)

    st.header('Biggest cities')


    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        'Population',
        'Income',
        'Crimes',
        'Tourism',
        'Rent',
        # 'Air quality'
    ])

    with tab1:
        st.subheader('Population density (inh/km²)')
        population_density = cities['Population_density']
        fig = px.bar(
            data_frame=population_density,
            y=population_density.index,
            x=population_density.values,
            labels={"x": "Population_density", "y": "City"},
        )
        fig.update_traces(marker_color="#58A1CF")
        st.plotly_chart(fig)
        st.dataframe(population_density)

    with tab2:
        st.subheader('Income proxy (GDP per capita €)')
        gdp_per_capita = cities['GDP_per_capita']
        fig = px.bar(
            data_frame=gdp_per_capita,
            y=gdp_per_capita.index,
            x=gdp_per_capita.values,
            labels={"x": "GDP_per_capita", "y": "City"},
        )
        fig.update_traces(marker_color="#46AE60")
        st.plotly_chart(fig)
        st.dataframe(gdp_per_capita)

    with tab3:
        st.subheader('Crime rate (crimes/100 k)')
        crime_rate = cities['Crime_rate']
        fig = px.bar(
            data_frame=crime_rate,
            y=crime_rate.index,
            x=crime_rate.values,
            labels={"x": "Crime_rate", "y": "City"},
        )
        fig.update_traces(marker_color="#F6553C")
        st.plotly_chart(fig)
        st.dataframe(crime_rate)

    with tab4:
        st.subheader('Tourism pressure (overnights per 1000 inh.)')
        tourism_pressure = cities['Tourism_pressure']
        fig = px.bar(
            data_frame=tourism_pressure,
            y=tourism_pressure.index,
            x=tourism_pressure.values,
            labels={"x": "Tourism_pressure", "y": "City"},
        )
        fig.update_traces(marker_color="#58A1CF")
        st.plotly_chart(fig)
        st.dataframe(tourism_pressure)

    with tab5:
        st.subheader('Average rent per square meter')
        average_rent = cities['Average_rent']
        fig = px.bar(
            data_frame=average_rent,
            y=average_rent.index,
            x=average_rent.values,
            labels={"x": "Average_rent", "y": "City"},
        )
        fig.update_traces(marker_color="#796EB2")
        st.plotly_chart(fig)
        st.dataframe(average_rent)
