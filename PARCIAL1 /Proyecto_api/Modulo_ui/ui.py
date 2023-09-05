from Modulo_api import api
from tabulate import tabulate


def consultar_datos(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta):
    resultado_consulta = api.obtener_api(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta)
    return resultado_consulta

def tabular_datos(dataframe,dt_mediana):

    print("BIEVENIDO AQUI ESTAN LOS  DATOS DE SU CONSULTA")
    
    titulo = ["DEPARTAMENTO", "MUNICIPIO", "CULTIVO", "TOPOGRAFIA"]  # Agrega los títulos que necesites
    
    # Tabular los datos utilizando tabulate
    tabla_datos = tabulate(dataframe, titulo, tablefmt='fancy_grid')    
    tabla_mediana = tabulate(dt_mediana, headers=["Descripción", "Mediana"], tablefmt="psql")
    print(tabla_datos)
    print(tabla_mediana)

    


limite_consulta = 19 
departamento_consulta = 'META'
municipio_consulta = 'ACACÍAS'
cultivo_consulta = 'Cacao'

"""
limite_consulta = int(input("Ingrese el límite de consulta: "))
departamento_consulta = input("Ingrese el departamento de consulta: ")
municipio_consulta = input("Ingrese el municipio de consulta: ")
cultivo_consulta = input("Ingrese el cultivo de consulta: ")"""


consulta = consultar_datos(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta)# Llamar a la función para tabular los datos
dataframe = api.beautifull_data(consulta)
convertidos = api.convert_data_values(consulta)
dt_mediana = api.mediana(convertidos)
tabla_resultante = tabular_datos(dataframe,dt_mediana)

