
def bs(array):
    n = len(array)
    aux=0
    for j in range(n):
        for i in range(n):
            if i+1 != n:
                if array[i] < array[i+1]:
                    aux=array[i]
                    array[i] = array[i+1]
                    array[i+1] = aux


n = int(input("Insira N: "))
array=[]
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)
bs(array)
print(array)
