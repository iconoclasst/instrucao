# Dado um vetor e um numero k, fazer uma rotação em k vezes.

def shift(array, k):
    # n = len(array)
    pass
    


n = int(input("Insira N: "))

array = [int(input("Insira um valor: ")) for i in range(n)]
k = int(input("Insira o tamanho do shift: "))

for i in range(n):
    if array[i-k] < 0:
        i = n - k
    array[i-k] = array[i]
    

print(array)