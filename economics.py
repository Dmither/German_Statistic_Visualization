import pandas as pd
import streamlit as st
import plotly.express as px

from choropleth_map import draw_st_choropleth_map


def economics():
    economics = pd.read_csv('germany_states_economics.csv')

    st.header('Economics')

    st.markdown('''
    * **GDP (2024 est.):** ~$5.8 trillion USD (nominal)
    * **GDP per capita:** ~$69,000 USD
    * **Major sectors:** Industry (automotive, machinery, chemicals), services, technology, energy
    * **Exports:** Machinery, vehicles, chemicals, electronics
    ''')

    tab1, tab2, tab3 = st.tabs([
        'GDP',
        'Average income',
        'Unemployment rate',
    ])

    with tab1:
        st.subheader('GDP')
        gpd = economics.sort_values('GDP_billion_EUR', ascending=False).set_index('State')['GDP_billion_EUR']
        fig = px.bar(
            data_frame=gpd,
            y=gpd.index,
            x=gpd.values,
            labels={"x": "GDP billion EUR", "y": "State"},
        )
        fig.update_traces(marker_color="#46AE60")
        st.plotly_chart(fig)
        st.dataframe(gpd)

        st.subheader('GDP per capita')
        gpd_per_capita = economics.sort_values('GDP_per_capita_EUR', ascending=False).set_index('State')['GDP_per_capita_EUR']
        draw_st_choropleth_map(gpd_per_capita, "Greens", legend_num=10)
        st.dataframe(gpd_per_capita)

    with tab2:
        st.subheader('Average gross income (EUR) per year')
        avg_gross_income = economics.sort_values('Average_gross_income_EUR_per_year', ascending=False).set_index('State')[
            'Average_gross_income_EUR_per_year']
        draw_st_choropleth_map(avg_gross_income, "YlGn", contrast=1, legend_num=10)
        st.dataframe(avg_gross_income)

    with tab3:
        st.subheader('Unemployment rate (%)')
        unemployment = economics.sort_values('Unemployment_rate_percent', ascending=False).set_index('State')['Unemployment_rate_percent']
        draw_st_choropleth_map(unemployment, "YlOrBr", contrast=1.2 , legend_num=10, legend_points=1)
        st.dataframe(unemployment)

