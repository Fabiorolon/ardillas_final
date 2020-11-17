
# Realize un programa que calcule cuantas nueces se comen 3 adillas y que el residuo total no sea < 0.

# En un arbol existen X cantidad de nueces, realizar un programa que determine 
# cuantas nueces se comen tres ardillas, si la primera se come 1/3 + 1; 
# luego la segunda ardilla se como 1/3 + 1 y la tercera se come luego 1/3 + 1


if __name__ == '__main__':
	nueces = float()
	variable1 = float()
	variable2 = float()
	variable3 = float()
	total = float()
	print("Ingrese la cantidad de nueces ")
	x = float(input())
	
	while x<=7.2:
		print("error, el numero debe ser > 7.2, para que el residuo no sea negativo")
		print("ingrese la cantidad de nueces")
		x = float(input())
	variable1 = x/3+1
	residuo1 = x-variable1
	variable2 = residuo1/3+1
	residuo2 = residuo1-variable2
	variable3 = residuo2/3+1
	residuo3 = residuo2-variable3
	total = variable1+variable2+variable3
	resto = x-total
	print("Cuantas nueces tomo la primera ardilla: ",variable1)
	print("El residuo 1 es: ",residuo1)
	print("Cuuantas nueces tomo la segunda ardilla: ",variable2)
	print("El residuo 2 es: ",residuo2)
	print("Cuantas nueces tomo la tercera ardilla: ",variable3)
	print("El residuo 3 es:",residuo3)
	print("Cuantas nueces tomaron en total las ardillas: ",total)
	print("Cuantas nueces quedan en el arbol:",resto)
	if x<=7.2:
		print("Valor no permitido, residuo < 0")
	else:
		print("El residuo es >= que 0")

# Teniendo en cuenta que cada ardilla tomo 1/3 +1 de nueces, para calcular cuantas nueces toma cada ardilla, 
# se realiza una operación de divison X/3 (siendo x la cantidad de nueces que hay en el arbol), 
# a el resultado se le suma 1; el resultado es la cantidad que tomo la primera ardilla.
# Luego se calcula el residuo 1 para determinar cuantas nueces quedan en el arbol,
# posteriormente para calcular cuantas nueces toma la adilla 2 se reemplaza X por el residuo 1 y se divide en 3
# a ese resultado se le suma 1, se vuelve a calcular el residuo 2 y se realiza la misma operacion para 
# calcular cuantas nueces tomo la ardilla 3, 
# finalmente a la variable X se le resta el total de la suma de las variables 1,2,3 y el residuo que queda
# es la cantidad de nueces que quedan.
