import pandas as pd
from sodapy import Socrata


# Crear el cliente para conectarse a la API pública de Datos Abiertos.
cliente = Socrata("www.datos.gov.co", None)


# Consultar los casos según los parámetros recibidos y retornar un DataFrame.
def consultar_casos(limite_registros, nombre_departamento):
    resultados = cliente.get(
        # Usar get() de sodapy para consultar el conjunto de datos y aplicar filtros.
        "gt2j-8ykr",
        limit=limite_registros,
        departamento_nom=nombre_departamento
    )

    # Usar from_records() de pandas para convertir los resultados en un DataFrame.
    return pd.DataFrame.from_records(resultados)


# Validar una columna y completar datos faltantes; para presentación.
def validar_datos(datos_consultados, nombre_columna):
    if nombre_columna not in datos_consultados.columns:
        datos_consultados[nombre_columna] = "No registrado"
    else:
        # Usar fillna() de pandas para reemplazar los valores faltantes.
        datos_consultados[nombre_columna] = (
            datos_consultados[nombre_columna].fillna("No registrado")
        )


# Filtrar las columnas requeridas y retornar un DataFrame organizado.
def filtrar_datos(datos_consultados):
    columnas_requeridas = [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "estado",
        "tipo_recuperacion",
        "pais_viajo_1_nom"
    ]

    # Valida cada columna antes de construir el resultado final (para la presentación al usuario).
    for columna in columnas_requeridas:
        validar_datos(datos_consultados, columna)

    # Usar reindex() de pandas para seleccionar y ordenar las columnas indicadas.
    return datos_consultados.reindex(columns=columnas_requeridas)