 # Reto 0
 #* Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 #* - Múltiplos de 3 por la palabra "fizz".
 #* - Múltiplos de 5 por la palabra "buzz".
 #* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for i in range(1,101):
    if (i%3 ==0  ) and (i%5 ==0):
        print(i, "Fizzbuzz")
    elif(i%3 ==0):
        print(i, "Fizz")
    elif(i%5 ==0):
        print(i, "buzz")
    else:
        print(i)




#reto 4
#Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 #* - La función recibirá por parámetro sólo UN polígono a la vez.
 #* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 #* - Imprime el cálculo del área de un polígono de cada tipo.