from api import datos_abiertos
from ui import interfaz

# Coordinar el flujo del programa.
def ejecutar_programa():
    # Obtener el límite de registros y el departamento a consultar.
    limite_registros, nombre_departamento = interfaz.menu_principal()

    # Enviar los parámetros al módulo encargado de consultar la API.
    datos_consultados = datos_abiertos.consultar_casos(
        limite_registros,
        nombre_departamento
    )

    # Filtrar las columnas necesarias para mostrar los resultados.
    datos_filtrados = datos_abiertos.filtrar_datos(datos_consultados)

    # Mostrar los datos filtrados en la interfaz.
    interfaz.mostrar_datos(datos_filtrados)


# Ejecutar el programa solo cuando este archivo sea ejecutado directamente.
if __name__ == "__main__":
    ejecutar_programa()