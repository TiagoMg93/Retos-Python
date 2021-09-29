#por continente, muestre la evolución del promedio de la
#razón entre el número total de casos de COVID-19 y el número total de camas
#de hospital disponibles a través del tiempo.

#Escriba una función que reciba como parámetro una cadena con la ruta dónde
#se encuentra guardado el archivo, incluyendo la extensión, y lo lea desde
#esta misma. A partir de estos datos, construya un dataframe sobre el cual,
#al utilizar el método df.plot() se obtenga la gráfica esperada.
import pandas as pd
def caso_who(ruta_archivo_csv: str)-> dict:
    if ruta_archivo_csv[-4:] == ".csv":
        try:
            data = pd.read_csv(ruta_archivo_csv)
        except:
            return "Error al leer el archivo de datos."
        data["date"] = pd.to_datetime(data["date"])
        data["total_casos_covid"] = (data['total_cases_per_million']*data['population'])/1000000
        data["total_camas_hospital"] = (data['hospital_beds_per_thousand']*data['population'])/1000
        data ['promedio_camas_paciente_covid'] = data["total_casos_covid"]/data["total_camas_hospital"]
        df_respuesta = data.groupby(['date','continent'])['promedio_camas_paciente_covid'].mean().unstack()
        df_respuesta = df_respuesta.to_dict()
        return (df_respuesta)
    else:
        return "Extensión inválida."
print(caso_who(".//owid-covid-data.csv"))
