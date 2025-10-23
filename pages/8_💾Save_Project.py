import streamlit as st
import pandas as pd
import csv
import os

from generaFileUnito import SalvaDati

# Titolo dell'applicazione
st.set_page_config(page_title="Save_Project")
st.title('💾Save Project')

with st.expander("🆘 Help"):
    st.markdown("""
    - **What to do here?**  
      In this module you can choose a personal file name and download it in your local drive. 
      The file include all project data and you can recall it when you need by ticking the option "stored project" in the main module. 
                                               

    """)

dati_generali = pd.read_csv("files/DatiGenerali.csv")
dati_piping = pd.read_csv("files/piping_groups.csv")
dati_components = pd.read_csv("files/component_groups.csv")
dati_temperatures = pd.read_csv("files/temperatures.csv", sep=';')

dati_temperatures["TempC"] = pd.to_numeric(dati_temperatures["TempC"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
dati_temperatures["TempF"] = pd.to_numeric(dati_temperatures["TempF"].astype(str).str.replace(",", ".", regex=False), errors="coerce")


# Dizionario con i tuoi DataFrame
dati_dict = {
    "General Data": dati_generali,
    "Piping Data": dati_piping,
    "Components Data": dati_components,
    "Temperature Data": dati_temperatures
}

# Lista dei DataFrame vuoti
vuoti = [nome for nome, df in dati_dict.items() if df.empty]

# Controllo e messaggi
if vuoti:
    st.warning("⚠️ Some data files are empty!")
    for nome in vuoti:
        st.error(f"❌ {nome} is empty!")
else:
    #st.success("✅ All data files are complete!")
    
    # Mostra un'anteprima dei dati separati
    st.write("General Data:")
    st.dataframe(dati_generali)
    
    st.write("Piping Data:")
    st.dataframe(dati_piping)

    st.write("Components Data:")
    st.dataframe(dati_components)

    st.write("Temperatures Data:")
    st.dataframe(dati_temperatures)
     
    SalvaDati()






