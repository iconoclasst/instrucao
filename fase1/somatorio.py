
# somar numeros de 1 até n

def somatorio(n):
    sm = 0
    for i in range(n+1):
        sm += i
    return sm


n = int(input("Insira N: ")) #Receber N
sm = somatorio(n)
print("A soma de 1 até {} é {}".format(n, sm))


