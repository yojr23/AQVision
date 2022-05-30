import pandas as pd
import matplotlib.pyplot as plt

#req0 
def cargar_datos(archivo:str)->pd.DataFrame:
    return pd.read_csv(archivo, encoding="UTF-8")

#req1

def diagrama_de_torta_segun_tipo_de_estacion(dataframe):
    dic={"Fija":0,"Indicativa":0}
    estaciones = dataframe[ ['Nombre de la estación','Tipo de estación'] ].drop_duplicates()
    for i in estaciones.index:
        if dataframe["Tipo de estación"][i]!="Tipo de estación":
            dic[dataframe["Tipo de estación"][i]]+=1
    listNumbers=[]
    percentage = [ ]
    listLabels =[]
    for x in dic:
        listLabels.append(x)
        listNumbers.append(dic[x])
    listLabels1 = []
    number = sum(listNumbers)
    for z in listNumbers:
        per = z / number *100
        percentage.append(str(round(per,1)))
    for u in range(len(listLabels)):
        listLabels1.append( listLabels[u] + " "+ percentage[u] +"%")
    plt.figure(figsize=(10,10))
    plt.pie(x=listNumbers, labels=listLabels, autopct='%1.1f%%')
    plt.title("Distribución porcentual segun los tipos de estaciones")
    plt.show()
x=cargar_datos("datos_reducidos")
#req2
def tendencia_medidas_por_rango_de_anios(dataframe,fecha1,fecha2):
    df = dataframe[(dataframe['Anio'] >= fecha1) & (dataframe['Anio'] <= fecha2)]
    df.sort_values(by=["Anio"],inplace=True)
    dic={}
    for i in df.index:
        if df["Anio"][i]!="Anio":
            if df["Anio"][i] not in dic:
                dic[df["Anio"][i]]=0
            dic[df["Anio"][i]]+=1     
    listNumbers=[]
    listLabels =[]
    for x in dic:
        listLabels.append(x)
        listNumbers.append(dic[x])
    plt.plot(listLabels, listNumbers, '-o')
    plt.xticks(list(range(fecha1,fecha2+1)))
    plt.title("Tendencia de numero de medidad en " + str(fecha1) + "y " +str(fecha2))
    plt.ylabel("Numero De Medidas", size = 9)
    plt.xlabel("Año", size = 9)
    plt.show()
    
#req3
def diagrama_de_barras_mediciones_o3_mayores_a(dataframe,valor):
    df=dataframe[(dataframe['Variable'] == "O3") & (dataframe['Concentración'] > valor)]
    dept=df.groupby(["Departamento"]).size()
    dept.sort_values(inplace=True,ascending=True)
    newdf=dept.tail()
    newdf.plot(kind="barh")
    plt.xlabel("Numero de medidas superiores a "+ str(valor),size=9)
    plt.ylabel("Departamentos",size=9)
    plt.title("Top departamentos con mediciones de O^3 superiores a "+str(valor))
    plt.show()

#req4

def caja_y_bigotes_distribucion_concentraciones_CO_por_año(dataframe,año):
    df=dataframe[(dataframe['Anio'] == año) & (dataframe['Tiempo de exposición'] ==8) & (dataframe['Variable'] == "CO")]
    df.boxplot(column="Concentración")
    plt.xlabel(str(año))
    plt.ylabel("Concentración")
    plt.title("Distribucion de medidas de CO por año")
    plt.show()

#req5

def concentraciones_anuales_PM10_por_departamento(dataframe,depto):
    df=dataframe[(dataframe['Departamento'] == depto) & (dataframe['Variable'] =="PM10")]
    del df["Tiempo de exposición"]
    newdf=df.groupby(["Anio"]).mean()
    newdf.plot(kind="bar")
    plt.title("Concentracion promedio del material articulado menor a " + depto,size=9)
    plt.xlabel("Año",size=9)
    plt.ylabel("Concentración",size=9)
    plt.show()







def crear_matriz(datos:pd.DataFrame)-> tuple:
    #Esqueleto diccionarios
    ICAs =sorted(datos["ICA"].unique())
    #Diccionario con el nombre de las columnas (ICA)
    ICAs_dict = dict(list(enumerate(ICAs)))
    deptos = sorted(datos["Departamento"].unique())
    #Diccionario con el nombre de las filas (Deptos)
    dept_dict = dict(list(enumerate(deptos)))
    matrix=[]
    for i in range(len((dept_dict))):
        listaNew=[]
        matrix.append(listaNew)
        for j in range(len((ICAs_dict))):
            listaNew.append(0)
    for z in datos.index:
        deptoEnlista = deptos.index(datos["Departamento"][z])
        IcaEnlista = ICAs.index(datos["ICA"][z])
        matrix[deptoEnlista][IcaEnlista]+=1
    return(matrix,dept_dict,ICAs_dict)
