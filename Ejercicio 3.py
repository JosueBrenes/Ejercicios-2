# = Solicitamos la medida de un lado del cuadrado
print("Digite la medida de un lado del cuadrado: ")
lado = input()
lado = int(lado)

# = Ahora se calcula la el perimetro
perimetro = 4 * lado

# = Imprimimos el resultado del perimetro
print("El perimetro del cuadrado es: " + str(perimetro))

# = Ahora se calcula el area
area = lado ** 2

# = Imprimimos el resultado del area
print("El area del cuadrado es: " + str(area))