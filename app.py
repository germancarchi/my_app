import streamlit as st
import libreria_personal as lp
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mi primera aplicacion en Streamlit")
st.sidebar.title("Parametros")

modulo = st.sidebar.selectbox("Seleccione un modulo",["Módulo 1","Módulo 2","Módulo 3"])

if modulo == "Módulo 1":
    st.write("Se encuentra en el módulo 1")
    gravedad_especifica = st.number_input("Ingrese la gravedad específica:",min_value=0.1,max_value=1.0,value=0.8)
    st.write(lp.grado_API(gravedad_especifica))
elif modulo == "Módulo 2":
    st.write("Se encuentra en el módulo 2")
    df = pd.read_excel("Data_Bombas.xlsx")
    st.write(df)
    st.write(df.columns)
    fig,ax = plt.subplots ()
    ax.pie (df["Presión (psi)"],labels=df["Bomba"],autopct="%1.1f%%")
    st.write(fig)
else :
    st.write("Se encuentra en el módulo 3")
    archivo_cargado = st.file_uploader("Ingrese su archivo CSV o EXCEL",type=["csv","xls","xlsx"])
    if archivo_cargado is not None:
        st.write("Su archivo ha sido cargado")
        if archivo_cargado.name.endswith(".csv"):
            df = pd.read_csv(archivo_cargado)
        else :
            df = pd.read_excel(archivo_cargado)
        st.write(df)
    else:
        st.write("Cargar el archivo")

        

