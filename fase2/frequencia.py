# problema: Dado um array, contar quantas vezes cada elemento aparece

def contar(array):
    n = len(array)
    aux = {}
    for i in range(n):
        if array[i] not in aux:
            aux[array[i]] = 1
        else:
            aux[array[i]] += 1
    
    return aux

n = int(input("Insira N: "))
array = []
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)

print("Contagem de cada valor no array:")

ctt = contar(array)

for i in ctt:
    print("O valor {} aparece {} vezes no array".format(i, ctt[i]))
    