# euromelhores 5 numeros e duas estrelas
numero = 0
while numero < 1 or numero > 50:
    while True:
        try:
            numero = int(input("coloca um numero "))
            break
        except:
            print("só numeros!!!")
    valor1 = numero
print(valor1)

while True:
    numero = 0
    while numero < 1 or numero > 50:
        while True:
            try:
                numero = int(input("coloca o 2º numero "))
                break
            except:
                print("só numeros!!!")
        valor2 = numero
    print(valor2)
    if valor1 == valor2:
        print("ja usa-te esse numero")
    else:
        break

while True:
    numero = 0
    while numero < 1 or numero > 50:
        while True:
            try:
                numero = int(input("coloca o 3º numero "))
                break
            except:
                print("só numeros!!!")
        valor3 = numero
    print(valor3)
    if valor3 == valor1 or valor3 == valor2:
        print("ja usa-te esse numero")
    else:
        break

while True:
    numero = 0
    while numero < 1 or numero > 50:
        while True:
            try:
                numero = int(input("coloca o 4º numero "))
                break
            except:
                print("só numeros!!!")
        valor4 = numero
    print(valor4)
    if valor4 == valor1 or valor4 == valor2 or valor4 == valor3:
        print("ja usa-te esse numero")
    else:
        break

while True:
    numero = 0
    while numero < 1 or numero > 50:
        while True:
            try:
                numero = int(input("coloca o 5º numero "))
                break
            except:
                print("só numeros!!!")
        valor5 = numero
    print(valor5)
    if valor5 == valor1 or valor5 == valor2 or valor5 == valor3 or valor5 == valor4:
        print("ja usa-te esse numero")
    else:
        break

numero = 0
while numero < 1 or numero > 12:
    while True:
        try:
            numero = int(input("coloca a 1º estrela "))
            break
        except:
            print("só numeros!!!")
    estrela1 = numero
    print(1)

while True:
    numero = 0
    while numero < 1 or numero > 12:
        while True:
            try:
                numero = int(input("coloca a 2ª estrela "))
                break
            except:
                print("só numeros!!!")
        estrela2 = numero
    print(estrela2)
    if estrela2 == estrela1:
        print("ja usa-te esse numero")
    else:
        break

print("a ordem do numero sao: ",valor1,valor2,valor3,valor4,valor5,"e as estrelas sao: ",estrela1,estrela2)