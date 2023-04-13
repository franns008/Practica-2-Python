nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
           'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica',
           'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
           'JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa',
           'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo',
           'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina']
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
           74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
           39, 15, 74, 33, 57, 10]
#Item A
estudiante_notas=dict(zip (nombres,(zip(notas_1,notas_2))))
#item B
promedio_notas=dict(map(lambda x:(x[0],sum(x[1])/2),estudiante_notas.items()))
for e in promedio_notas:
    print(e,promedio_notas[e])
#item C
promedio_general=sum(promedio_notas.values())/len(promedio_notas)
print(f"Promedio de notas del curso: ",promedio_general)
#item D
promedio_alto=max(promedio_notas.items(),key=lambda alto: alto[1])
print(f"El promedio mas alto es el de ",promedio_alto[0],"con un promedio de:",promedio_alto[1])
#item E
nota_minima=min(map(lambda minimo:(minimo[0],min(minimo[1])),estudiante_notas.items()),key=lambda minimo:minimo[1])
print(f"la nota minima es de",nota_minima[0],"siendo esta",nota_minima[1])