# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#data set
dataset = pd.read_csv('D:\Documentos\MISCURSOS\Proyectos Git Hub\MACHINE-LEARNIG\supervised_Learning\classification\svm\dataset\DataSet_Iris_2_Clases.csv - Hoja 1.csv')

#dataset dataframe
x = dataset.drop('variety',axis=1)
y = dataset['variety']

# dataframe to np.array
xx = np.array(x)
yy = np.array(y)


#graficamos los datos 
cmap = ListedColormap(['red','g','blue'])
plt.scatter(xx[:,0],xx[:,3],c=y,s = 40, cmap=cmap)





# %%

corr_matrix = dataset.corr(numeric_only= True) #correlation matriz only numbers


corr_matrix['sepal.length'].sort_values(ascending=False)


# %%
