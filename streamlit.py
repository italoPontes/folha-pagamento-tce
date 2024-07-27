import streamlit as st  # Importa el módulo streamlit para crear aplicaciones web interactivas
import pandas as pd  # Importa el módulo pandas para manipulación y análisis de datos
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

# Define el nombre del archivo de entrada que contiene los datos
input_file_name = 'consolidado_2024.csv'

# Lee el archivo CSV y lo carga en un DataFrame de pandas
df = pd.read_csv(input_file_name, sep=';')

# Establece el título de la aplicación web
st.title("TCE PB - Folha de Pagamento")

# Crea una entrada de texto en la aplicación web para que el usuario ingrese su búsqueda
text = st.text_input("Digite o CPF do funcionário.")

df_filtered = df[df['cpf_servidor'].apply(lambda x: True if text in str(x) else False)]

# Muestra el DataFrame filtrado en la aplicación web
st.dataframe(df_filtered)

cpf_test = df_filtered[df_filtered['cpf_servidor'].apply(lambda x: True if text in str(x) else False)]
cpf_test = cpf_test.groupby('data')['valor_remuneracao_total'].sum().reset_index()

st.line_chart(cpf_test, x='data', y='valor_remuneracao_total')

pr = df.profile_report()
st_profile_report(pr)