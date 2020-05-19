# dizer quais dos numeros sao pares quais sao impares e dizer quanto teve de cada

from builtins import int
lista_par = list()
lista_impar = list()
vezes = int(input("quantos numeros vais inserir? "))
par = 0
impar = 0

while vezes != 0:
    valor  = int(input("qual é o valor que queres?"))
    valorp = valor % 2
    valori = valor % 2
    if valorp == 0:
        par = par + 1
        lista_par.append(int((valor)))
    else:
        if valori !=0:
            impar = impar + 1
            lista_impar.append(int((valor)))
    vezes =vezes -1


print("houve",par,"numeros pares")
if lista_par != [] :
    print("os numeros pares são:")
    print(lista_par)

print("houve",impar,"numeros impares")
if lista_impar != []:
    print("os numeros impares são:")
    print(lista_impar)
