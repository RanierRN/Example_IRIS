import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv("iris.csv")
print(iris.groupby('species').size())

fig = iris[iris.species == 'setosa'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='blue', label='Setosa')
iris[iris.species == 'versicolor'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='green', label='Versicolor', ax=fig)
iris[iris.species == 'virginica'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='red', label='Virginica', ax=fig)

fig.set_xlabel('Sépalo - Longitud')
fig.set_ylabel('Sépalo - Ancho')
fig.set_title('Sépalo - Longitud vs Ancho')
plt.show()