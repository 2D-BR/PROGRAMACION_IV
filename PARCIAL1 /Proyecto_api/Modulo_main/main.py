from Modulo_api import api
from Modulo_ui import ui


def consultas_usuario(departamento_consulta, municipio_consulta , cultivo_consulta, limite_consulta):
    if limite_consulta > 1000:
        print("demasiados datos puede  colgarse,digete un limite menor")
        Menu_usuario()
    else:
        consulta = ui.consultar_datos(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta)
        dataframe = api.beautifull_data(consulta)
        convertidos = api.convert_data_values(consulta)
        dt_mediana = api.mediana(convertidos)
        ui.tabular_datos(dataframe,dt_mediana)

def Menu_usuario():
    while True:
        print("\nMenú:")
        print("1. Consultar datos")
        print("2. Salir")
        
        seleccion = input("Seleccione una opción: ")
        
        if seleccion == "1":
            
            

            limite_consulta = int(input("Ingrese el límite de consulta: "))
            departamento_consulta = input("Ingrese el departamento de consulta: ")
            municipio_consulta = input("Ingrese el municipio de consulta: ")
            cultivo_consulta = input("Ingrese el cultivo de consulta: ")
            
            consultas_usuario(departamento_consulta, municipio_consulta, cultivo_consulta,limite_consulta)

        elif seleccion == "2":
            print("Saliendo de las conjuntos adios!.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")





Menu_usuario()

"""
limite_consulta = 19 
departamento_consulta = 'META'
municipio_consulta = 'ACACÍAS'
cultivo_consulta = 'Cacao'


limite_consulta = 2 
departamento_consulta = 'HUILA'
municipio_consulta = 'GIGANTE'
cultivo_consulta = 'Aguacate'


limite_consulta = 19 
departamento_consulta = 'CUNDINAMARCA'
municipio_consulta = 'FUNZA'
cultivo_consulta = 'Uchuva'
"""    