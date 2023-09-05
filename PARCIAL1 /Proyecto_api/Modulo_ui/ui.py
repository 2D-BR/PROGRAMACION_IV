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

    


