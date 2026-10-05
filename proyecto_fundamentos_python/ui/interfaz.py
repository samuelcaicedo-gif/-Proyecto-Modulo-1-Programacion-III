from prettytable import PrettyTable


# Mostrar el encabezado inicial de la aplicación y no retornar valores.
def mostrar_mensaje_bienvenida():
    print("""
            +--------------------------------------------------------------+
            |      SISTEMA DE CONSULTA DE CASOS COVID-19 EN COLOMBIA      |
            +--------------------------------------------------------------+
            """)


# Solicitar el límite y el departamento para la consulta y retornar ambos valores.
def menu_principal():
    # Solicitar los datos necesarios para realizar la consulta.
    mostrar_mensaje_bienvenida()

    # Entrada de datos usuario
    limite_registros = int(input("Digite el limite de registros: "))
    nombre_departamento = input("Digite el departamento: ").strip().upper()

    return limite_registros, nombre_departamento


# Mostrar los resultados en una tabla y no retornar valores.
def mostrar_datos(datos_df):
    # Crear la tabla de resultados con PrettyTable.
    pretty = PrettyTable()

    # Definir los encabezados visibles de la tabla con PrettyTable.
    pretty.field_names = [
        "Ubicacion",
        "NombreDepartamento",
        "Edad",
        "TipoRecuperacion",
        "Estado",        
        "PaisProcedencia"
    ]

    for registro in range(len(datos_df)):
        # Usar loc de pandas para acceder a cada dato por índice y columna.
        pretty.add_row([
            datos_df.loc[registro, "ciudad_municipio_nom"],
            datos_df.loc[registro, "departamento_nom"],
            datos_df.loc[registro, "edad"],
            datos_df.loc[registro, "tipo_recuperacion"],
            datos_df.loc[registro, "estado"],            
            datos_df.loc[registro, "pais_viajo_1_nom"]
        ])

    # Mostrar la tabla con el formato generado por PrettyTable.
    print(pretty)
