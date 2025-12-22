import pandas as pd
import streamlit as st
from choropleth_map import draw_st_choropleth_map


def general():
    demographics = pd.read_csv('germany_states.csv')

    st.markdown('''
    # **Germany, general Information**
    ''')



    st.markdown('''
    **Official name:** Federal Republic of Germany (Bundesrepublik Deutschland)
    
    **Capital:** Berlin
    
    **Official language:** German
    
    **Government:** Federal parliamentary republic
    
    **Area:** ~357,022 km²
    
    **Population (2025 est.):** ~84 million
    
    **Currency:** Euro (€)
    
    **Time zone:** Central European Time (CET, UTC+1)
    
    **Climate:** Temperate seasonal, with maritime influence in the north and continental in the east/southeast
    ''')

    st.markdown('''
    ## **Germany’s Federal States (Bundesländer)**
    ''')

    states = demographics.sort_values('N', ascending=True).set_index('State')['N']

    draw_st_choropleth_map(states, color='tab20', contrast=1.5, legend_num=0)

    st.markdown('''
    Germany has **16 states**, divided into **three city-states** and **13 territorial states**. Each state has its own government, constitution, and some legislative powers.
    | State                                  | Capital     | Area (km²) | Population (millions) | Economy                 | Notes                                               |
    | -------------------------------------- | ----------- | ---------- | --------------------- | ----------------------- | --------------------------------------------------- |
    | Baden-Württemberg                      | Stuttgart   | 35,752     | 11.1                  | Industry & tech hub     | Strong automotive sector (Mercedes, Porsche)        |
    | Bavaria (Bayern)                       | Munich      | 70,550     | 13.1                  | Industry & tourism      | Home to BMW, Siemens, Alps tourism                  |
    | Berlin                                 | Berlin      | 891        | 3.8                   | Services & government   | City-state, cultural & political center             |
    | Brandenburg                            | Potsdam     | 29,476     | 2.5                   | Energy & agriculture    | Surrounds Berlin; coal power historically important |
    | Bremen                                 | Bremen      | 419        | 0.7                   | Port & trade            | City-state, smallest state by area & population     |
    | Hamburg                                | Hamburg     | 755        | 1.9                   | Port & logistics        | City-state, major shipping hub                      |
    | Hesse (Hessen)                         | Wiesbaden   | 21,115     | 6.3                   | Finance & industry      | Frankfurt financial center                          |
    | Mecklenburg-Vorpommern                 | Schwerin    | 23,180     | 1.6                   | Tourism & agriculture   | Baltic Sea coast, low population density            |
    | Lower Saxony (Niedersachsen)           | Hanover     | 47,618     | 8.0                   | Industry & agriculture  | Volkswagen HQ in Wolfsburg                          |
    | North Rhine-Westphalia (NRW)           | Düsseldorf  | 34,112     | 18.0                  | Industry & services     | Most populous, Ruhr industrial region               |
    | Rhineland-Palatinate (Rheinland-Pfalz) | Mainz       | 19,854     | 4.1                   | Wine & chemicals        | Famous wine regions (Mosel, Rhine)                  |
    | Saarland                               | Saarbrücken | 2,569      | 0.9                   | Industry                | Small state, steel & automotive industry            |
    | Saxony (Sachsen)                       | Dresden     | 18,449     | 4.0                   | Industry & technology   | Strong automotive & microelectronics sectors        |
    | Saxony-Anhalt (Sachsen-Anhalt)         | Magdeburg   | 20,446     | 2.2                   | Chemicals & agriculture | Former East Germany; energy production              |
    | Schleswig-Holstein                     | Kiel        | 15,802     | 2.9                   | Ports & wind energy     | Between North and Baltic Seas; strong renewables    |
    | Thuringia (Thüringen)                  | Erfurt      | 16,202     | 2.1                   | Industry & forestry     | Central Germany; historical towns                   |
    ''')
    '''
    **Official name:** Federal Republic of Germany (Bundesrepublik Deutschland)
    
    **Capital:** Berlin
    
    **Official language:** German
    
    **Government:** Federal parliamentary republic
    
    **Area:** ~357,022 km²
    
    **Population (2025 est.):** ~84 million
    
    **Currency:** Euro (€)
    
    **Time zone:** Central European Time (CET, UTC+1)
    
    **Climate:** Temperate seasonal, with maritime influence in the north and continental in the east/southeast
    
    ### Economy
    
    * **GDP (2024 est.):** ~$5.8 trillion USD (nominal)
    * **GDP per capita:** ~$69,000 USD
    * **Major sectors:** Industry (automotive, machinery, chemicals), services, technology, energy
    * **Exports:** Machinery, vehicles, chemicals, electronics
    
    ### Infrastructure
    
    * **Transport:** Extensive road network (Autobahnen), high-speed rail (ICE), major ports (Hamburg, Bremen), international airports (Frankfurt, Munich, Berlin)
    * **Internet:** Widespread broadband, increasing gigabit coverage (~80% households with high-speed connections nationally)
    * **Energy:** Transitioning to renewables (wind, solar, hydro, biomass), ~54% of electricity from renewables
    
    ### Society & Health
    
    * **Life expectancy:** ~81 years
    * **Healthcare:** High-quality universal coverage, strong hospital and doctor density
    * **Education:** Free primary to tertiary education, strong vocational and technical training system
    
    ### Environment
    
    * **CO₂ emissions per capita:** ~6.95 t (2023) nationally, with variation across states
    * **Air quality:** PM2.5 ~7.3 µg/m³ (population-weighted)
    * **Water quality:** High; >97% of bathing waters meet EU standards
    
    ---
    
    ## 🗺️ **Germany’s Federal States (Bundesländer)**
    
    Germany has **16 states**, divided into **three city-states** and **13 territorial states**. Each state has its own government, constitution, and some legislative powers.
    
    | #  | State                                  | Capital     | Area (km²) | Population (millions) | Economy                 | Notes                                               |
    | -- | -------------------------------------- | ----------- | ---------- | --------------------- | ----------------------- | --------------------------------------------------- |
    | 1  | Baden-Württemberg                      | Stuttgart   | 35,752     | 11.1                  | Industry & tech hub     | Strong automotive sector (Mercedes, Porsche)        |
    | 2  | Bavaria (Bayern)                       | Munich      | 70,550     | 13.1                  | Industry & tourism      | Home to BMW, Siemens, Alps tourism                  |
    | 3  | Berlin                                 | Berlin      | 891        | 3.8                   | Services & government   | City-state, cultural & political center             |
    | 4  | Brandenburg                            | Potsdam     | 29,476     | 2.5                   | Energy & agriculture    | Surrounds Berlin; coal power historically important |
    | 5  | Bremen                                 | Bremen      | 419        | 0.7                   | Port & trade            | City-state, smallest state by area & population     |
    | 6  | Hamburg                                | Hamburg     | 755        | 1.9                   | Port & logistics        | City-state, major shipping hub                      |
    | 7  | Hesse (Hessen)                         | Wiesbaden   | 21,115     | 6.3                   | Finance & industry      | Frankfurt financial center                          |
    | 8  | Mecklenburg-Vorpommern                 | Schwerin    | 23,180     | 1.6                   | Tourism & agriculture   | Baltic Sea coast, low population density            |
    | 9  | Lower Saxony (Niedersachsen)           | Hanover     | 47,618     | 8.0                   | Industry & agriculture  | Volkswagen HQ in Wolfsburg                          |
    | 10 | North Rhine-Westphalia (NRW)           | Düsseldorf  | 34,112     | 18.0                  | Industry & services     | Most populous, Ruhr industrial region               |
    | 11 | Rhineland-Palatinate (Rheinland-Pfalz) | Mainz       | 19,854     | 4.1                   | Wine & chemicals        | Famous wine regions (Mosel, Rhine)                  |
    | 12 | Saarland                               | Saarbrücken | 2,569      | 0.9                   | Industry                | Small state, steel & automotive industry            |
    | 13 | Saxony (Sachsen)                       | Dresden     | 18,449     | 4.0                   | Industry & technology   | Strong automotive & microelectronics sectors        |
    | 14 | Saxony-Anhalt (Sachsen-Anhalt)         | Magdeburg   | 20,446     | 2.2                   | Chemicals & agriculture | Former East Germany; energy production              |
    | 15 | Schleswig-Holstein                     | Kiel        | 15,802     | 2.9                   | Ports & wind energy     | Between North and Baltic Seas; strong renewables    |
    | 16 | Thuringia (Thüringen)                  | Erfurt      | 16,202     | 2.1                   | Industry & forestry     | Central Germany; historical towns                   |
    
    ---
    
    ### Key Observations About the States
    
    1. **Population density**: Highest in NRW, Berlin, Hamburg; lowest in Mecklenburg-Vorpommern, Brandenburg.
    2. **Economy**: Industrial powerhouses in Bavaria, Baden-Württemberg, NRW; service & finance in Berlin and Hesse.
    3. **Environment**: CO₂ per capita highest in industrial/coal states (NRW, Brandenburg, Saxony-Anhalt), lowest in city-states (Berlin, Hamburg).
    4. **Infrastructure**: Transport and broadband coverage highest in urbanized and southern states.
    5. **Tourism & natural resources**: Bavaria (Alps), Mecklenburg-Vorpommern (Baltic Sea), Schleswig-Holstein (North Sea), Black Forest in Baden-Württemberg.
    '''
