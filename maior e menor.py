men = None
mai = None
while True:
        n = input("coloca um numero,se nao queres colocar mais numeros escreve done ")
        try:
            num = int(n)
        except:
            if n == "done":
                break
            print("error")
            continue
        if men is None:
            men = num
            mai = num
        else:
            if num < men:
                 men = num
            if num > mai:
                mai = num

print(" o maior foi ",mai,"e o menor foi ", men)