import streamlit as st
import pandas as pd

dic = {
    "Matrícula" : [1111, 2222, 3333, 4444, 5555],
    "Nome" : ["João das Neves", "Joana Darc", "Leia", "Marcos", "Miguel A."],
    "Idade" : [18, 19, 18, 28, 26], 
    "Curso" : ["Metaverso", "Dev Fullstack", "Dev Fullstack", "Fotografia", "Design"]
}

dicDF = pd.DataFrame(dic)

st.write(dicDF)

#lista = [8.0, 9.1, 7.5, 7.4, 7.6, 7.8, 8.0, 9.3, 7.0, 7.0, 7.2, 7.5]
#x = pd.Series(lista)

#st.title("Título da primeira página")
#st.write(x.mean())
#st.write(x.median())
#print(x.mean())
#print(x.median())

