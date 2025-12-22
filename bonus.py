import pandas as pd
import streamlit as st
import plotly.express as px

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

    st.header('Bonus')

    (tab1,) = st.tabs([
        'Heatmap',
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
