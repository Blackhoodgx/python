print("caluladora")
while True:
     try:
         valor1 = float(input("qual é o 1º valor "))
         break
     except:
         print("só numeros!!!")

while True:
    op = input("qual é a operaçao ")
    if op == "*" or op == "+" or op == "-" or op == "/":
        break
    else:
        print(" so operaçoes (+,-,*,/)")
        continue

while True:
    try:
        valor2 = float(input("qual é o 2º valor "))
        if op == "/" and valor2 == 0:
            print("nao é possivel dividir por 0!!!!")
            continue
        break
    except:
        print("só numeros!!!")

def calula(op):
    if op == "+":
        op = valor1 + valor2
        return op
    else:
        if op == "-":
            op = valor1 - valor2
            return op
        else:
            if op == "*":
                op = valor1 * valor2
                return op
            else:
                if op == "/":
                    op = valor1 / valor2
                    return op

resultado = calula(op)
print("o total é", resultado)
