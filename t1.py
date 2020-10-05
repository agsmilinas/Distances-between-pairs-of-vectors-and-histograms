# -*- coding: utf-8 -*-

import numpy
from prettytable import PrettyTable
import statistics
from matplotlib import pyplot as plt

# Generar una secuencia de 100 puntos, con distribución uniforme en [0,1]. 
secuencia = numpy.random.uniform(low=0.0, high=1.0, size=100)
numpy.savetxt("secuncia.csv", secuencia, delimiter=",")

distancias = []
distancias_sin_abs = []
diagonal = []
t = PrettyTable(['Points', 'Distance'])
suma2 = 0
suma = 0
ceros = []

# Encontrar la distancia “promedio” entre dos puntos escogidos al azar en el intervalo [0,1].
for numero in range(len(secuencia)):
    for numero2 in range(len(secuencia)):
        fila = str(secuencia[numero])+":"+str(secuencia[numero2])
        distancia = secuencia[numero]-secuencia[numero2]
        distancias_sin_abs.append(distancia)
        #Una distancia siempre debe ser mayor a 0
        distancias.append(abs(distancia))
        t.add_row([fila, abs(distancia)])
        if distancia == 0.0:
            ceros.append(distancia)

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

# Graficar la frecuencia relativa de pares de puntos localizados a una distancia d.
plt.hist(distancias)
plt.xlabel("D")
plt.ylabel("Número Pares")
plt.title("Histograma de matriz completa de Distancias")
plt.show()

plt.title("Histograma de matriz sin valor absoluto")
plt.hist(distancias_sin_abs)
plt.show()

plt.title("Histograma de matriz con una sola diagonal")
plt.hist(diagonal)
plt.show()
