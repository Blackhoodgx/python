''' conversor de temperatura
celsius
para kelvin
k = graus + 273.15

para fahrenheit
f = (1.8*graus)+32
................................................
................................................
Fahrenheit

para celsius
c = ((graus-32)*5)/9

para kelvin
k = (((graus-32)*5)/9)+273.15
.................................................
.................................................
kelvin
para celsius
c = graus -273.15

para fahrenheit

f = (graus-273.15)*1.8+32

'''


#conversor de temperatura
c=0
k=0
f=0
a=0
while a == 0:
    while True:
            usar =input("qual é medida de temperatura quere converter: Celsius, Fahrenheit ou Kelvin? ")
            if usar =="Celsius" or usar == "celsius":
                break
            else:
                if usar == "Fahrenheit" or usar == "fahrenheit":
                    break
                else:
                    if usar =="Kelvin" or usar == "kelvin" :
                        break
                    else:
                        print("dados invalido escolha uma medida de temperatura valida!!!!")
                        continue

    while True:
        try:
            graus = float(input("introduza os graus a converter? "))
        except:
            print("só numeros!!!!!!!!")
            continue
        if usar =="Kelvin" or usar == "kelvin"  and graus<0:
            print("kelvin nao tem graus negativos!!!!")
            continue
        else:
            break

    while True:
        para =input("queres converter para que medidas: Celsius, Fahrenheit ou Kelvin? ")
        if (para !="Celsius" and para !="celsius") and (para != "Fahrenheit" and para != "fahrenheit") and (para!="kelvin" and para!="Kelvin"):
            print("dados invalido escolha uma medida de temperatura valida!!!!")
            continue
        else:
            pass
        if (para =="kelvin" or para =="Kelvin") and (usar =="Kelvin" or usar =="kelvin"):
            print(graus,"º ",usar," para ",para," ainda são ",graus,"º Kelvin!!!!!!!")
            continue
        else:
            pass
        if (para =="Celsius" or para =="celsius") and (usar =="Celsius" or usar =="celsius"):
            print(graus,"º ",usar," para ",para," ainda são ",graus,"º Celsius!!!!!!!")
            continue
        else:
            pass

        if (para == "Fahrenheit" or para == "fahrenheit") and (usar == "Fahrenheit" or usar == "fahrenheit"):
            print(graus,"º ",usar," para ",para," ainda são ",graus,"º Fahrenheit!!!!!!!")
            continue
        else:
            pass
        break

    if (usar =="Celsius" or usar =="celsius") and (para =="Kelvin" or para =="kelvin"):
        k = graus + 273.15
        print(graus,"º",usar," sao",k,"º ",para)
    elif (usar =="Celsius" or usar =="celsius") and (para == "Fahrenheit" or para == "fahrenheit"):
        f = (1.8*graus)+32
        print(graus,"º",usar," sao",f,"º ",para)


    if (usar == "Fahrenheit" or usar == "fahrenheit") and (para =="Celsius" or para =="celsius"):
        c = ((graus-32)*5)/9
        print(graus,"º",usar," sao",c,"º ",para)
    elif (usar == "Fahrenheit" or usar == "fahrenheit") and (para =="Kelvin" or para =="kelvin"):
        k = (((graus-32)*5)/9)+273.15
        print(graus,"º",usar," sao",k,"º ",para)


    if (usar =="Kelvin" or usar =="kelvin") and (para =="Celsius" or para =="celsius"):
        c = graus -273.15
        print(graus,"º",usar," sao",c,"º ",para)
    elif (usar =="Kelvin" or usar =="kelvin") and (para == "Fahrenheit" or para == "fahrenheit"):
        f = (graus-273.15)*1.8+32
        print(graus,"º",usar," sao",f,"º ",para)
        print("ola")
    pass

    b =0
    while b==0:
        print("queres fazer outra coverçao? sim ou nao ")
        repetir = input()
        if repetir !="sim" and repetir !="nao":
            print(" escreve sim ou nao!!!!")
            continue
        else:
            if repetir== "sim":
                a=0
                b=1
            elif repetir=="nao":
                a=1
                b=1

print("adeus")

