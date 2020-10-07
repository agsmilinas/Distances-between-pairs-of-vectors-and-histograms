# -*- coding: utf-8 -*-

import numpy
from prettytable import PrettyTable
import statistics
from matplotlib import pyplot as plt

# Generate a sequence of 100 points, with uniform distribution in [0,1].
secuencia = numpy.random.uniform(low=0.0, high=1.0, size=100)
numpy.savetxt("secuncia.csv", secuencia, delimiter=",")

distancias = []
diagonal = []
t = PrettyTable(['Points', 'Distance'])
suma2 = 0
suma = 0
ceros = []

# Find the “average” distance between two points chosen at random in the interval [0,1].
for numero in range(len(secuencia)):
    for numero2 in range(len(secuencia)):
        fila = str(secuencia[numero])+":"+str(secuencia[numero2])
        distancia = secuencia[numero]-secuencia[numero2]
        #A distance must always be greater than 0
        distancias.append(abs(distancia))
        t.add_row([fila, abs(distancia)])


print(t)
promedio = statistics.mean(distancias)
print("Promedio de distancias considerando todos los datos")
print("El promedio de distancias de este conjunto de datos es de: "+str(promedio))
for j in distancias:
    suma+=j
print("El promedio de distancias de este conjunto es de: "+str((suma/len(distancias))))

print("Promedio de distancias considerando solo una diagonal:")


a = numpy.array(distancias)
distancias_ordenadas =  a.reshape((100,100))
for j in distancias_ordenadas:
    for a in j:
        if a == 0.0:
            break
        else: 
            diagonal.append(a)

for j in diagonal:
    suma2+=j
numpy.savetxt("distancias.csv", distancias_ordenadas, delimiter=",")
print("El promedio de distancias de este conjunto es de: "+str((suma2/5000)))

# Plot the relative frequency of pairs of points located at a distance d.
plt.hist(distancias)
plt.xlabel("D")
plt.ylabel("Número Pares")
plt.title("Histograma de matriz completa de Distancias")
plt.show()



plt.title("Histograma de matriz con una sola diagonal")
plt.hist(diagonal)
plt.show()
