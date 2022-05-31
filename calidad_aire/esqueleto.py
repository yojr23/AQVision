import matplotlib.patches as mpatches
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpinmg
from matplotlib.patches import Rectangle

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
x=cargar_datos("datos_reducidos.csv")
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


#req6
def crear_matriz(datos:pd.DataFrame)-> tuple:
    #Esqueleto diccionarios
    ICAs =sorted(datos["ICA"].unique())
    #Diccionario con el nombre de las columnas (ICA)
    ICAs_dict = dict(list(enumerate(ICAs)))
    deptos = sorted(datos["Departamento"].unique())
    #Diccionario con el nombre de las filas (Deptos)
    dept_dict = dict(list(enumerate(deptos)))
    ICAs.insert(0,"-")
    matriz=[ICAs]
    
    for i in deptos:
        lt = [i]
        for j in range (1,len(ICAs)):
            x=datos[(datos["Departamento"]==i) & (datos["ICA"]==ICAs[j])]
            lt.append(len(x))    
        matriz.append(lt)
        
    return (matriz, ICAs_dict, dept_dict)
z=crear_matriz(x)

#req 7
def encontrar_departamento_con_mas_mediciones(matriz, dept_dict):
    mayor=0
    mayorIndex=0
    for i in matriz:
        if sum(i)>mayor:
            mayor=sum(i)
            mayorIndex=matriz.index(i)
    return dept_dict[mayorIndex]

#req8
def contar_cantidad_de_mediciones_con_un_ICA_dado(UserICA,matriz,ICAs_dict):
    ICAiNDEX=(list(ICAs_dict.values()).index(UserICA))    
    contar=0
    for i in matriz:
        contar+=i[ICAiNDEX]
    return contar

#req9
def mayores_mediciones_ICA_y_departamento(matrix, ICAs_dict, dept_dict):
    mayorJotas=0
    mayorIes=0
    mayor=0
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j > mayor:
                mayor=j
                mayorJotas = matrix[i].index(j)
                mayorIes = i
    return (list(dept_dict.values())[mayorIes]),(list(ICAs_dict.values())[mayorJotas])


def cargar_coordenadas(nombre_archivo):
    deptos={}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea)>0:
        linea = linea.strip()
        datos = linea.split(';')
        deptos[datos[0].upper()] = (int(datos[1]), int(datos[2]))
        linea= archivo.readline()
    return deptos
        

def departamentos_mapa(tupla_matriz):
    mapa = mpinmg.imread("mapa.png").tolist()
    plt.imshow(mapa)
    
    matriz, ICAs, deptos = tupla_matriz
        
    mat = matriz.copy()
    dic_ICAs = {}
        
    for i in range(1,len(mat)):
        ICA=""
        valor=0
        for j in range(1,len(mat[0])):
            if mat[i][j]>valor:
                valor=mat[i][j]
                ICA=ICAs[j-1]
            
        dic_ICAs[mat[i][0]] = ICA
    
    colores = {"Buena":[36/255,226/255,41/255],
               "Aceptable":[254/255,253/255,56/255],
               "Dañina a la salud de grupos sensibles":[252/255,102/255,33/255],
               "Dañina a la salud":[252/255,20/255,27/255],
               "Muy dañina a la salud":[127/255,15/255,126/255],
               "Peligrosa":[101/255, 51/255, 8/255]}
    
    legends = []
    for i in range(1,len(matriz[0])):
        legends.append(mpatches.Patch(color = colores[tupla_matriz[1][i-1]], label=tupla_matriz[1][i-1]))
        plt.legend(handles=legends, loc=3, fontsize='x-small')
    
    dic_coord = cargar_coordenadas("coordenadas_corregidas.txt")
        
    for i in deptos.values():
        if dic_ICAs[i]=="Buena":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Buena"]))
        elif dic_ICAs[i]=="Aceptable":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Aceptable"]))
        elif dic_ICAs[i]=="Dañina a la salud de grupos sensibles":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Dañina a la salud de grupos sensibles"]))
        elif dic_ICAs[i]=="Dañina a la salud":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Dañina a la salud"]))
        elif dic_ICAs[i]=="Muy dañina a la salud":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Muy dañina a la salud"]))
        elif dic_ICAs[i]=="Peligrosa":
            plt.gca().add_patch(Rectangle((dic_coord[i][0]-6.5,dic_coord[i][1]-6.5), 13, 13, color=colores["Peligrosa"]))
    
    return plt.show()
    
print(departamentos_mapa(crear_matriz(cargar_datos("datos_reducidos.csv"))))




    
