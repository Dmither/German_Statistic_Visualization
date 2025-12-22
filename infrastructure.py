import pandas as pd
import streamlit as st
import plotly.express as px

from choropleth_map import draw_st_choropleth_map


def infrastructure():
    infrastructure = pd.read_csv('germany_states_infrastructure.csv')

    st.header('Infrastructure')

    st.markdown('''
    * **Transport:** Extensive road network (Autobahnen), high-speed rail (ICE), major ports (Hamburg, Bremen), international airports (Frankfurt, Munich, Berlin)
    * **Internet:** Widespread broadband, increasing gigabit coverage (~80% households with high-speed connections nationally)
    * **Energy:** Transitioning to renewables (wind, solar, hydro, biomass), ~54% of electricity from renewables
    ''')

    tab1, tab2 = st.tabs([
        'Internet speed',
        'Hospital beds',
    ])

    with tab1:
        st.subheader('Gigabit broadband availability in households (%)')
        gigabit = infrastructure.sort_values(
            'Gigabit_per_households', ascending=False
        ).set_index('State')['Gigabit_per_households']
        draw_st_choropleth_map(gigabit, "Blues", contrast=1, legend_num=10)
        st.dataframe(gigabit)


    with tab2:
        st.subheader('Hospital beds per 100000 inhabitants')
        beds = infrastructure.sort_values(
            'Hospital_beds_per_100000', ascending=False
        ).set_index('State')['Hospital_beds_per_100000']
        draw_st_choropleth_map(beds, "YlGn", contrast=1, legend_num=10)
        st.dataframe(beds)
