import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('C:/Users/Eloy/Documents/Andres/Estadistica/train.csv')

#Para responder la interrogante de la cantidad de variables cualitativas, tomaremos
#como variables cualitativas las que no sean de tipo numerico (int, float...)
#es decir, tipo object. Para ello se tiene las siguientes sentencias

rows = len(train.dtypes.values)
i = 0
count = 0 #Almacenara la cantidad de datos tipo objeto, es decir las variables cualitativas
for i in range(rows):
    if(train.dtypes.values[i] == 'O'):
        count += 1
    i += 1
print("La cantidad de variables cualitativas es: " + str(count))

#La cantidad total de columnas es de
print("La cantidad de columnas es: " + str(len(train.columns)))
#Como el id no es una variable, se tienen 80 variables
#Ahora bien, si de esas 80 variables, 43 son cualitativas, entonces, 37 son cuantitativas

#La cantidad de mediciones, es igual a la cantidad de registros, es decir rows

#Para obtener la cantidad de observaciones no nulas
notnulos = train.notnull().sum()
cantnotnull = notnulos.sum()
cantotal = cantnotnull - train.Id.count()
print(cantotal)

#Realice un histograma de frecuencia relativa para cualquiera de las variables
#Ejercicios 1.16 1.17 y 1.18 

#Grafica de barras para la variable categorica RoofStyle
counts = train['RoofStyle'].value_counts()
with plt.style.context('dark_background'):
    counts.plot(kind='bar', color='steelblue')
    plt.ylabel("Frecuency of Roof Styles")
    plt.title("Bar Chart of Roof Styles")

#Grafica de pastel para la variable categorica RoofStyle
counts = train['RoofStyle'].value_counts()
porct =counts/1460*100
label = []
for i in range(len(counts)):
    label.append(counts.index[i] + " "+ '{0:.2f}%'.format(porct[i]))
sizes = [1141, 286, 13, 11, 7, 2]  
colors = ['steelblue', 'skyblue', 'navy', 'blue', 'red', 'green']
with plt.style.context('dark_background'):
	fig, ax = plt.subplots()
	ax.pie(sizes, colors=colors, shadow=False, startangle=0)
	ax.axis('equal') 
	ax.legend(label, shadow=True) 
	plt.title("Pie Chart of the Roof Styles")
	plt.show()

#Grafica de barras para la variable cuantitativa FullBath
countsb = train['FullBath'].value_counts()
countsb = countsb.sort_index()
with plt.style.context('dark_background'):
    countsb.plot(kind='bar', color='steelblue')
    plt.ylabel("Frecuency of Full Bathrooms")
    plt.title("Bar Chart of Full Bathrooms")

#Grafica de pastel para la variable cuantitativa FullBath
porct = countsb/1460*100
labels = []
for i in range(len(countsb)):
    labels.append(str(countsb.index[i])+" FullBaths "+'{0:.2f}%'.format(porct[i]))
sizes = [9, 650, 768, 33]
colors = ['navy', 'skyblue', 'steelblue', 'blue']
with plt.style.context('dark_background'):
	fig, ax = plt.subplots()
	ax.pie(sizes, colors=colors, shadow=False, startangle=0)
	ax.axis('equal')
	ax.legend(labels, shadow=True)
	plt.title("Pie Chart of the Full Bathrooms in the Basement")
	plt.show()

#Grafica de linea para YrSold
Yearsold = train.YrSold.value_counts().sort_index()
index = np.array(Yearsold.index, dtype=str)
with plt.style.context('dark_background'):
    plt.subplots()
    plt.plot(index, Yearsold, color='steelblue')
    plt.title("Year Sold")
    
#Grafica de puntos para YrSold
year = np.array(train.YrSold.values)
year.sort()
yearsold = np.array(year, dtype=str)
aux = train.YrSold.unique()
aux.sort()
aux2 = train.YrSold.value_counts()
aux2.sort_index()
lista = []
for i in aux:
    lista.append(np.arange(1,aux2[i]+1))
frecuencia = np.concatenate(lista)
with plt.style.context('dark_background'):
    plt.subplots()
    plt.scatter(yearsold, frecuencia, c='steelblue', marker='o')
    plt.title("Point Chart of Year Sold")

#Para graficas las dos variables juntas
SumSalePrice=train.groupby('YrSold')['SalePrice'].sum().reset_index().SalePrice
YrSold=train.groupby('YrSold')['SalePrice'].sum().reset_index().YrSold.astype(str) #para evitar que en el eje x los años tengan decimales
#GRAFICO DE LINEA ACERCA DEL PRECIO TOTAL VENDIDO DE LOS EDIFICIOS POR ANNIOS
with plt.style.context('dark_background'):
	plt.subplots()
	plt.plot(YrSold,SumSalePrice/10**6, color='steelblue')
	plt.rcParams.update({'font.size':9,'font.family':'serif'})
	plt.title("Total sales of the residential homes in Ames, lowa")
	plt.ylabel("Sale Prices of buildings in millions of dollars")
	plt.xlabel("Years Sold")

#Histograma de frecuencia relativa para 1stFlrSF
datahist = train['1stFlrSF']
weights = np.ones_like(datahist)/float(len(datahist))
with plt.style.context('dark_background'):
    plt.subplots()
    datahist.hist(color='steelblue', weights=weights)
    plt.title('Relative Frecuency Histrogram of Superficie of the first floor')
    plt.show()
