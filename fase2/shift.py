# Dado um vetor e um numero k, fazer uma rotação em k vezes.

def shift(array, k):
    n = len(array)
    aux = 0
    for i in range(n):
        if i+k > n:
            
            aux[i] = array[(i+k)%n]
    return aux

n = int(input("Insira N: "))

array = [int(input("Insira um valor: ")) for i in range(n)]
k = int(input("Insira o tamanho do shift: "))

print(array)

aux = shift(array, k)

print(aux)