

def inverter(array):
    n = len(array)
    aux=[]
    for i in range(n-1, -1, -1):
        aux.append(array[i])
    return aux


n = int(input("Insira N: "))
array = []

for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)
aux = inverter(array)
print("O array ordenado fica assim: {}".format(aux))

