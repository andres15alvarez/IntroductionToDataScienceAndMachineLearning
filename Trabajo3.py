import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error
from scipy.stats import zscore
train = pd.read_csv('C:/Users/Eloy/Documents/Andres/Estadistica/train.csv')


pd.options.display.max_columns = None
train.corr()


train.MasVnrArea = train.MasVnrArea.fillna(0.0) #Tiene valores nulos, aqui que colocamos un 0 para eliminar los valores nulos
#train80 = train.sample(frac=0.8, random_state=15)#Escogemos un 80% para el entrenamiento
features = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd', 'GarageCars','GarageArea','Fireplaces','MasVnrArea']
X = train[features]
y = train.SalePrice.values
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=44)
model = LinearRegression()
model.fit(XTrain, yTrain)


predict = model.predict(XTest)
mae = mean_absolute_error(y_true=yTest,y_pred=predict)
mse = mean_squared_error(y_true=yTest,y_pred=predict)
rmse = np.sqrt(mse)
print("Error absoluto medio: ", str(mae))
print("Error Cuadratico Medio: ", str(mse))
print("Raiz del Error Cuadratico Medio: ", str(rmse))


#Escogemos las columnas de feature y el target para quitarles los valores atipicos
columns = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd', 'GarageCars','GarageArea','Fireplaces','MasVnrArea', 'SalePrice']
df = train[columns] #df sera nuestro DataFrame auxiliar
z_scores = zscore(df)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
train = df[filtered_entries]


#Ya tenemos el nuevo dataframe para el entrenamiento, asi que repetimos el proceso
train.OverallQual = np.power(train.OverallQual,2) #Realizamos una transformacion
X = train[features]
y = train.SalePrice.values
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=44)
model = LinearRegression()
model.fit(XTrain, yTrain)


predict = model.predict(XTest)
mae = mean_absolute_error(y_true=yTest,y_pred=predict)
mse = mean_squared_error(y_true=yTest,y_pred=predict)
rmse = np.sqrt(mse)
r2 = model.score(XTrain,yTrain)
print("Error absoluto medio: ", str(mae))
print("Error Cuadratico Medio: ", str(mse))
print("Raiz del Error Cuadratico Medio: ", str(rmse))
print("Coeficiente de determinacion: ", str(r2))
