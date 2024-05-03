"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Leer el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    # Eliminar filas con valores nulos
    df.dropna(inplace=True)
    
    # Eliminar caracteres especiales y convertir texto a minúsculas
    df = df.apply(lambda x: x.astype(str).str.lower())
    
    # Reemplazar caracteres específicos por espacio en blanco
    df = df.apply(lambda x: x.str.replace("-", " "))
    df = df.apply(lambda x: x.str.replace("_", " "))
    df = df.apply(lambda x: x.str.replace("¿", ""))
    df = df.apply(lambda x: x.str.replace(",", ""))
    # Eliminar símbolo de pesos y comas de la columna 'monto_del_credito'
    #df['monto_del_credito'] = df['monto_del_credito'].str.replace("[$,]", "").astype(float)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("[$,]", "", regex=True).astype(float)

    # Convertir la columna 'fecha_de_beneficio' a formato datetime
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, errors='coerce')
    
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    return df


#print(clean_data())
#print(clean_data().sexo.value_counts().to_list())
#print(clean_data().tipo_de_emprendimiento.value_counts().to_list())
#print(clean_data().idea_negocio.value_counts().to_list())
#print(clean_data().barrio.value_counts().to_list())
#print(clean_data().estrato.value_counts().to_list())
#print(clean_data().comuna_ciudadano.value_counts().to_list())
#print(clean_data().fecha_de_beneficio.value_counts().to_list())
#print(clean_data().monto_del_credito.value_counts().to_list())
#print(clean_data().línea_credito.value_counts().to_list())