# Problema: remover duplicados do array

def remove(array):
    n = len(array)
    aux = {}
    for i in range(n):
        if array[i] in aux:
            array.remove(array[i])
        else:
            aux[array[i]] = i
            
    # print("funcionou" if 50 in aux else "Não")
    # print(array)
    # print(aux)


n = int(input("Insira N: "))
array=[]
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print("Array inicial: ", array)

remove(array)
print("Array após remoção: ", array)