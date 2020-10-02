 
from sklearn.preprocessing import StandardScaler 
import pandas 
import numpy 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
dataframe = pandas.read_csv(url, names=names) 
array = dataframe.values 

# separate array into input and output components 
X = array[:,0:8] 
Y = array[:,8] 
scaler = StandardScaler().fit(X) 
rescaledX = scaler.transform(X) 

# summarize transformed data 
numpy.set_printoptions(precision=3) 
print(rescaledX[0:5,:]) 
