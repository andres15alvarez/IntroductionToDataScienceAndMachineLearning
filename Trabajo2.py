import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('C:/Users/Eloy/Documents/Andres/Estadistica/train.csv')
rows=len(train.dtypes.values) 
numericVariables=[]
for i in range(rows):
    if train.dtypes.values[i] != 'O':
        numericVariables.append(train.dtypes.index[i])
numericVariables.pop(0)

medias = np.array(train[numericVariables].mean().values)
medianas = np.array(train[numericVariables].median().values)
modas = np.array(train[numericVariables].mode().values[0])
varianzas = np.array(train[numericVariables].var().values)
dvestandar = np.array(train[numericVariables].std().values)
curtosis = np.array(train[numericVariables].kurtosis().values)
sesgo = np.array(train[numericVariables].skew().values)
tabla = pd.DataFrame({'Media':medias,'Mediana':medianas,'Moda':modas,
                      'varianza':varianzas,'Desviacion estandar':dvestandar,
                      'Curtosis':curtosis,'Sesgo':sesgo}, index=numericVariables)
print(tabla)

for i in range(len(numericVariables)):
    plt.boxplot(train[numericVariables[i]], vert=False)

