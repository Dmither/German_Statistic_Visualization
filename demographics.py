import pandas as pd
import streamlit as st
import plotly.express as px

from choropleth_map import draw_st_choropleth_map


def demographics():
    demographics = pd.read_csv('germany_states_demographics.csv')

    st.header('Demographics')

    st.markdown('''
    * **Total population:** ~84 million
    * **Median age:** ~45 years
    * **Fertility rate:** ~1.4 children per woman
    * **Life expectancy:** ~81 years
    * **Share aged 65+:** ~22% of population
    * **Share aged under 15:** ~14%
    * **Natural population growth:** negative (deaths exceed births)
    * **Net migration:** positive and the main source of population growth
    * **Population density:** ~235 inhabitants per km²
    ''')

    tab1, tab2, tab3 = st.tabs([
        'Population',
        'Population density',
        'Average age'
    ])

    with tab1:
        st.subheader('Population:')
        population = demographics.sort_values('Population', ascending=False).set_index('State')['Population']
        fig = px.bar(
            data_frame=population,
            y=population.index,
            x=population.values,
            labels={"x": "Population", "y": "State"},
        )
        fig.update_traces(marker_color="#FEC95B")
        st.plotly_chart(fig)
        st.dataframe(population)

    with tab2:
        population_density = demographics.sort_values('Population Density', ascending=False).set_index('State')['Population Density']
        st.subheader('Population density:')
        draw_st_choropleth_map(population_density, color='YlOrBr', contrast=1.5, legend_num=10)
        st.dataframe(population_density)

    with tab3:
        average_age = demographics.sort_values('Average Age', ascending=False).set_index('State')['Average Age']
        st.subheader('Average age:')
        draw_st_choropleth_map(average_age, color='YlOrRd', legend_num=7)
        st.dataframe(average_age)
