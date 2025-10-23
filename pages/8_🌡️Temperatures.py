import streamlit as st
import pandas as pd
import os
import csv
import shutil

# Titolo dell'applicazione
st.set_page_config(page_title="Temperatures", page_icon="🌡️", layout= "centered")
st.title('🌡️ Temperatures Editor')

with st.expander("🆘 Help"):
    st.markdown("""
    - **What to do here?**  
      In this module You can see the temperatures table that will be used in the calculations expressed in Fahrenheit or Celsius.
      Here You can add, change and delete any row or restore the whole original temperatures table. You can choose to work indifferently in Fahrenheit or Celsius for each operation.
      The system automatically calculate the corresponding value in the other unit.                                     

    """)

# === Lettura del file CSV ===
file_path = "files/Temperatures.csv"
output_path = "files/Temperatures.csv"


if "df" not in st.session_state:
    if os.path.exists(file_path):
        # Leggi CSV gestendo separatore e virgola decimale se serve
        df = pd.read_csv(file_path, sep=";")
        df["TempC"] = pd.to_numeric(df["TempC"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
        df["TempF"] = pd.to_numeric(df["TempF"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
    else:
        df = pd.DataFrame(columns=["TempF", "TempC"])
    
    st.session_state.df = df  # 🔹 salva in sessione

df = st.session_state.df  # 🔹 lavora sempre sulla copia in memoria


st.subheader("📋 Temperatures Table")

posTable = st.empty()
posTable.dataframe(df, use_container_width=True)

# === Scelta dell'azione ===
action = st.radio("Select an action:", ["Add", "Change", "Delete", "Restore"], horizontal=True)

# === Funzioni di conversione ===
def c_to_f(c): return round(c * 9/5 + 32, 2)
def f_to_c(f): return round((f - 32) * 5/9, 2)
        

# === Aggiunta ===
if action == "Add":
    st.subheader("➕ Add a new temperature")
    mode = st.radio("Input the temperature in:", ["Fahrenheit", "Celsius"], horizontal=True, index= 1, key="unit_mode_add")
    
    temp = st.number_input("Temperature value:", value=0.0)
    
    if st.button("Add"):
        if mode == "Celsius":
            temp_c = temp
            temp_f = c_to_f(temp)
            temp_c = round(temp_c, 2)
            temp_f = round(temp_f, 2)
            # 🔹 Controllo duplicati: verifica se il valore Celsius esiste già
            if any(abs(df["TempC"] - temp_c) < 1e-6):  # tolleranza numerica
                st.warning(f"⚠️ The temperature {temp_c} °C is existing, no added.")

            else:    
                new_row = {"TempF": temp_f, "TempC": temp_c}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df = df.sort_values(by="TempC", ascending=True, na_position="last").reset_index(drop=True)
                st.session_state.df = df  # 🔹 aggiorna la versione in memoria
                st.success("✅ Temperature added!")
                st.session_state.df.to_csv(output_path, sep=";", index=False)
        else:
            
            temp_f = temp
            temp_c = f_to_c(temp)
            temp_c = round(temp_c, 2)
            temp_f = round(temp_f, 2) 
            # 🔹 Controllo duplicati: verifica se il valore Celsius esiste già
            if any(abs(df["TempF"] - temp_f) < 1e-6):  # tolleranza numerica
                st.warning(f"⚠️ The temperature {temp_f} °F is existing, no added.")

            else:    
                new_row = {"TempF": temp_f, "TempC": temp_c}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df = df.sort_values(by="TempC", ascending=True, na_position="last").reset_index(drop=True)
                st.session_state.df = df  # 🔹 aggiorna la versione in memoria
                st.success("✅ Temperature added!")
                st.session_state.df.to_csv(output_path, sep= ";", decimal=",", index=False, encoding="utf-8")
          

# === Modifica ===
elif action == "Change":
    st.subheader("✏️ Change Temperature")
    if len(df) == 0:
        st.info("No rows to modify.")
    else:
        index = st.number_input("Index of temperature to modify:", 0, len(df)-1, 0)
        mode = st.radio("Working unit:", ["Fahrenheit", "Celsius"], horizontal=True, index= 1, key="unit_mode")
        
        if mode== "Fahrenheit":
            mode1 = "TempF"
        elif mode == "Celsius":
            mode1 = "TempC"

        new_value = st.number_input("Change value:", value=float(df.loc[index, mode1]))
        if st.button("Apply Change"):
            if mode == "Celsius":
                df.loc[index, "TempC"] = new_value
                df.loc[index, "TempF"] = c_to_f(new_value)
            else:
                df.loc[index, "TempF"] = new_value
                df.loc[index, "TempC"] = f_to_c(new_value)
            
            st.session_state.df = df  # 🔹 aggiorna la versione in memoria
            st.success("✅ Change done!")
            st.session_state.df.to_csv(output_path, sep= ";", decimal=",", index=False, encoding="utf-8")

# === Eliminazione ===
elif action == "Delete":
    st.subheader("🗑️ Delete a temperature")
    if len(df) == 0:
        st.info("No rows to delete.")
    else:
        index = st.number_input("Index of the row to delete:", 0, len(df)-1, 0)
        #st.write(f"Temp = {df.iloc[index]['TempC']} °C") #, format="Temperature to delete: {:.2f} °C")
        st.markdown(f"<span style='color:green'>Temp = {df.iloc[index]['TempC']} °C</span>", unsafe_allow_html=True)

        if st.button("Delete"):
            df = df.drop(index).reset_index(drop=True)
            st.session_state.df = df  # 🔹 aggiorna la versione in memoria
            st.success("✅ Row deleted!")
            st.session_state.df.to_csv(output_path, sep= ";", decimal=",", index=False, encoding="utf-8")

# === Ripristino originale ===
elif action =="Restore":
    source = "files/Temperatures_Original.csv"
    target = "files/Temperatures.csv"

    st.subheader("♻️ Restore Original Temperatures")

    if st.button("Restore"):

        if os.path.exists(source):
            try:
                shutil.copy(source, target)
                st.success("✅ 'Original Temperatures List' restored correctly!")
                df1 = pd.read_csv(target, sep=";")
                df1["TempC"] = pd.to_numeric(df1["TempC"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
                df1["TempF"] = pd.to_numeric(df1["TempF"].astype(str).str.replace(",", ".", regex=False), errors="coerce")
                st.session_state.df = df1  # 🔹 aggiorna la versione in memoria
                    
            except Exception as e:
                st.error(f"❌ Error during restoring: {e}")
        else:
            st.error("⚠️ 'Original Temperatures' do not exist in the folder 'files'.")

# === Visualizzazione aggiornata ===
#st.subheader("📈 Table updated")
posTable.dataframe(st.session_state.df, use_container_width=True)

# === Salvataggio ===
#if st.button("💾 Save as new CSV"):
#    output_path = "files/Temperatures.csv"
#    st.session_state.df.to_csv(output_path, index=False)
#    st.success(f"✅ File salvato in: `{output_path}`")



