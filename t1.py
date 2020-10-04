# -*- coding: utf-8 -*-

import numpy
from prettytable import PrettyTable
import statistics
from matplotlib import pyplot as plt

# Generar una secuencia de 100 puntos, con distribución uniforme en [0,1]. 
secuencia = numpy.random.uniform(low=0.0, high=1.0, size=100)
numpy.savetxt("secuncia.csv", secuencia, delimiter=",")

distancias = []
t = PrettyTable(['Points', 'Distance'])

# Encontrar la distancia “promedio” entre dos puntos escogidos al azar en el intervalo [0,1].
for numero in range(len(secuencia)):
    for numero2 in range(len(secuencia)):
        fila = str(secuencia[numero])+":"+str(secuencia[numero2])
        distancia = secuencia[numero]-secuencia[numero2]
        distancias.append(distancia)
        t.add_row([fila, distancia])

print(t)
promedio = statistics.mean(distancias)  
print("El promedio de distancias de este conjunto de datos es de: "+str(promedio))
suma = 0
for j in distancias:
    suma+=j
print("El promedio de distancias de este conjunto es de: "+str((suma/len(distancias))))

l_100 = []
a = numpy.array(distancias)
distancias_ordenadas =  a.reshape((100,100))
numpy.savetxt("distancias.csv", distancias_ordenadas, delimiter=",")



# Graficar la frecuencia relativa de pares de puntos localizados a una distancia d.
plt.hist(distancias)
plt.show()
