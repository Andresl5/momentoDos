import streamlit as st
import pandas as pd

data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

data

''' filtro todos los puntajes de ingles igual a 46 '''

dataUno = data[data["puntaje_ingles"] == 46]

dataUno


''' filtro de puntaje sociales mayor o igual a 50 y puntaje naturales mayor o igual a 50'''

dataDos = data[(data['puntaje_sociales'] >= 50) & (data['puntaje_naturales'] >= 50)]

dataDos

''' filtrar establecimiento que contenga la palabra "parroquial"'''

dataTres = data[data['establecimiento'].str.contains("parroquial", case=False)]

dataTres

''' filtro puntaje de matematicas menor a cuarenta'''

def nota_matematicas(puntaje_matematicas):
    return puntaje_matematicas < 40

dataCuatro = data[nota_matematicas(data["puntaje_matematicas"])]

dataCuatro

''' filtrar el ponderado de lectura de for descendente'''

dataCinco = data.sort_values(by= "ponderado_lectura", ascending= False)

dataCinco