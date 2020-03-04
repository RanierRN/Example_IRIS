import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv("iris.csv")
print(iris.groupby('species').size())

fig = iris[iris.species == 'setosa'].plot(kind='scatter', x='petal_length', y='petal_width', color='blue', label='Setosa')
iris[iris.species == 'versicolor'].plot(kind='scatter', x='petal_length', y='petal_width', color='green', label='Versicolor', ax=fig)
iris[iris.species == 'virginica'].plot(kind='scatter', x='petal_length', y='petal_width', color='red', label='Virginica', ax=fig)

fig.set_xlabel('Pétalo - Longitud')
fig.set_ylabel('Pétalo - Ancho')
fig.set_title('Pétalo Longitud vs Ancho')
plt.show()