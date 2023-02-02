# = Solicitamos el nombre de la persona A
print("Digite el nombre de la persona A: ")
nombreA = input()

# = solicitamos el nombre de la persona B
print("Digite el nombre de la persona B: ")
nombreB = input()

# = Solicitamos la edad de la persona A
print("Digite la edad de " + str(nombreA))
edadA = input()
edadA = float(edadA)

# = Solicitamos la edad de la persona B
print("Digite la edad de " + str(nombreB))
edadB = input()
edadB = float(edadB)

# = Operacion de intercambio
edadIntercambio = edadA
edadA = edadB
edadB = edadIntercambio

# = Imprimimos los resultados 
print(nombreA + " tiene " + str(edadA))
print(nombreB + " tiene " + str(edadB))