
def fibo(n):
    sm = 2
    ordem = [1, 1]
    for i in range(1, n):
        soma = ordem[i] + ordem[i-1]
        ordem.append(soma)
        sm+=soma
    return ordem, sm


n = int(input("Insira N: "))
lista, soma = fibo(n)

print("Sequência: ", lista)
print("Soma total: ", soma)