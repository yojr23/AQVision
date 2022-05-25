import esqueleto as mod
import pandas as pd


def ejecutar_cargar_datos() -> pd.DataFrame:
    ruta = input("Ingrese el nombre del archivo: ")
    resultados = mod.cargar_datos(ruta)
    print("Datos cargados exitosamente")
    return resultados


def ejecutar_diagrama_de_torta_segun_tipo_de_estacion(datos: pd.DataFrame) -> None:
    mod.diagrama_de_torta_segun_tipo_de_estacion(datos)

# Probar con 100


def ejecutar_diagrama_de_barras_mediciones_o3_mayores_a(datos: pd.DataFrame) -> None:
    cota = float(input("Ingrese la cota inferior de O3: "))
    mod.diagrama_de_barras_mediciones_o3_mayores_a(datos, cota)

# Probar con 2018


def ejecutar_caja_y_bigotes_distribucion_concentraciones_CO_por_año(datos: pd.DataFrame) -> None:
    anio = int(input("Ingrese el año de búsqueda: "))
    mod.caja_y_bigotes_distribucion_concentraciones_CO_por_año(datos, anio)

# Probar con "Antioquia"


def ejecutar_concentraciones_anuales_PM10_por_departamento(datos: pd.DataFrame) -> None:
    dpto = input("Ingrese el departamento a buscar: ")
    mod.concentraciones_anuales_PM10_por_departamento(datos, dpto)

# Probar de 2014 a 2018


def ejecutar_tendencia_medidas_por_rango_de_anios(datos: pd.DataFrame) -> None:
    anio_inf = int(input("Ingrese el año de cota inferior: "))
    anio_sup = int(input("Ingrese el año de cota superior: "))
    mod.tendencia_medidas_por_rango_de_anios(datos, anio_inf, anio_sup)


def ejecutar_crear_matriz(datos: pd.DataFrame) -> None:
    return mod.crear_matriz(datos)


def ejecutar_dar_departamento_con_mas_mediciones(info_matriz: tuple) -> None:
    print(
        f"El departamento con más mediciones es {mod.dar_departamento_con_mas_mediciones(info_matriz)}")

# Probar con 'Peligrosa'


def ejecutar_contar_numero_de_mediciones_por_ica_dado(info_matriz: tuple) -> None:
    ica_a_buscar = input("Ingrese el ICA a buscar: ")
    print(
        f"Hay {mod.contar_numero_de_mediciones_por_ica_dado(info_matriz, ica_a_buscar)} mediciones")


def ejecutar_mayores_mediciones_ica_y_departamento(info_matriz: tuple) -> None:
    t = mod.mayores_mediciones_ica_y_departamento(info_matriz)
    print(
        f"El departamento y el ICA con mayores mediciones es: {t[0]} y {t[1]}")


def ejecutar_departamentos_mapa(info_matriz: tuple) -> None:
    mod.departamentos_mapa(info_matriz)


def mostrar_menu() -> None:
    print("\nMenú de opciones:")
    print("1. Cargar datos calidad del aire")
    print("2. Ver diagrama de torta según tipo de estación")
    print("3. Ver diagrama de barras mediciones de O^3 mayores a una concentración")
    print("4. Ver diagrama de caja y bigotes de distribución de concentraciones de CO por año")
    print("5. Ver concentraciones anuales de PM10 por departamento")
    print("6. Ver tendencia número de medidas por rango de años")
    print("7. Crear matriz de departamento vs ICA")
    print("8. Consultar el departamento con más mediciones")
    print("9. Consultar el número de mediciones según ICA dado")
    print("10. Consultar el departamento e ICA con mayor cantidad de mediciones")
    print("11. Generar mapa de ICA por departamento")
    print("12. Salir")


def iniciar_aplicacion() -> None:
    datos = None
    tupla_matriz = None
    continuar = True

    while continuar:
        mostrar_menu()

        opcion = int(input("Ingrese la opción que desea ejecutar: "))
        if opcion == 1:
            datos = ejecutar_cargar_datos()
        elif opcion == 2:
            ejecutar_diagrama_de_torta_segun_tipo_de_estacion(datos)
        elif opcion == 3:
            ejecutar_diagrama_de_barras_mediciones_o3_mayores_a(datos)
        elif opcion == 4:
            ejecutar_caja_y_bigotes_distribucion_concentraciones_CO_por_año(
                datos)
        elif opcion == 5:
            ejecutar_concentraciones_anuales_PM10_por_departamento(datos)
        elif opcion == 6:
            ejecutar_tendencia_medidas_por_rango_de_anios(datos)
        elif opcion == 7:
            tupla_matriz = ejecutar_crear_matriz(datos)
        elif opcion == 8:
            ejecutar_dar_departamento_con_mas_mediciones(tupla_matriz)
        elif opcion == 9:
            ejecutar_contar_numero_de_mediciones_por_ica_dado(tupla_matriz)
        elif opcion == 10:
            ejecutar_mayores_mediciones_ica_y_departamento(tupla_matriz)
        elif opcion == 11:
            ejecutar_departamentos_mapa(tupla_matriz)
        elif opcion == 12:
            continuar = False
        else:
            print(
                "Ingresó una opción no válida, por favor elija una de las opciones del menú")


iniciar_aplicacion()
