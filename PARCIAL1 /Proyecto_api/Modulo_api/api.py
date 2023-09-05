import pandas as pd
from sodapy import Socrata
from statistics import median


#MODULO API

#Globalizamos la conexion con la api
client = Socrata("www.datos.gov.co", None)

# Crear el cliente de la API
def obtener_api(departamento_consulta,municipio_consulta,cultivo_consulta,limite_consulta):

    consult_result = client.get("ch4u-f3i5", limit = limite_consulta, departamento = departamento_consulta, municipio = municipio_consulta, cultivo = cultivo_consulta)
    return consult_result

#organiza los datos para verlos mas esteticos 
def beautifull_data(consult_result):
    consult_dataframe = pd.DataFrame.from_records(consult_result, columns=["departamento", "municipio", "cultivo","topografia" ])
   
    return consult_dataframe



"""def sort_dataframe(consult_dataframe):
    #es el mismo consult_dataframe pero ordenado 
    orderly_dataframe = consult_dataframe.sort_values(by='f_sforo_p_bray_ii_mg_kg')
    print(orderly_datafame)"""


def mediana(consult_result):
    
    #dataframes medians
    df_m = pd.DataFrame(consult_result, columns = ['departamento', "municipio", "cultivo","topografia",'ph_agua_suelo_2_5_1_0' ,'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg'])
    mediana_ph = median(df_m["ph_agua_suelo_2_5_1_0"])
    mediana_fosforo = median(df_m["f_sforo_p_bray_ii_mg_kg"])
    mediana_potasio= median(df_m['potasio_k_intercambiable_cmol_kg'])
    

    data_mediana = [
    ["Mediana del pH del agua", mediana_ph],
    ["Mediana del fosforo", mediana_fosforo],
    ["Mediana del potasio", mediana_potasio]]

    return data_mediana



#vuelve  numeros valores string que representan numeros y elimina asigando 0 a los valore s  con "<" 
def convert_data_values(consult_result):
    
    for i in consult_result:
        if i['ph_agua_suelo_2_5_1_0'][0] != '<': 

            i['ph_agua_suelo_2_5_1_0'] = float(i['ph_agua_suelo_2_5_1_0'])

        else:
            i['ph_agua_suelo_2_5_1_0'] = float(0)

    for j in consult_result:
        if j['f_sforo_p_bray_ii_mg_kg'][0] != '<': 

            j['f_sforo_p_bray_ii_mg_kg'] = float(j['f_sforo_p_bray_ii_mg_kg'])

        else:
            j['f_sforo_p_bray_ii_mg_kg'] = float(0)
    
    for n in consult_result:
        if n['potasio_k_intercambiable_cmol_kg'][0] != '<': 

            n['potasio_k_intercambiable_cmol_kg'] = float(n['potasio_k_intercambiable_cmol_kg'])

        else:
            n['potasio_k_intercambiable_cmol_kg'] = float(0)

 
    
    return consult_result


"""
limite_consulta = 19 
departamento_consulta = 'META'
municipio_consulta = 'ACACÍAS'
cultivo_consulta = 'Cacao'


"""
limite_consulta = 2 
departamento_consulta = 'HUILA'
municipio_consulta = 'GIGANTE'
cultivo_consulta = 'Aguacate'"""

"""
limite_consulta = 19 
departamento_consulta = 'CUNDINAMARCA'
municipio_consulta = 'FUNZA'
cultivo_consulta = 'Uchuva'
"""





consult_result = obtener_api(departamento_consulta, municipio_consulta, cultivo_consulta, limite_consulta)
consult_dataframe=beautifull_data(consult_result)
print(consult_dataframe)
consul_result_convert=convert_data_values(consult_result)
data_mediana=mediana(consul_result_convert)
#tabla_mediana = tabulate(data_mediana, headers=["Descripción", "Mediana"], tablefmt="psql")
print(data_mediana)"""










