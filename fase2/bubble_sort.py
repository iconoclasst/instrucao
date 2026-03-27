
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

# versão 2
def bs_v2(array):
    n = len(array)
    for j in range(n):
        for i in range(n - j - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

#n = int(input("Insira N: "))
#array=[]
#for i in range(n):
 #   array.append(int(input("Insira um valor: ")))

#print(array)
#bs(array)
#print(array)

a = [3,5,1,2,3,3,3,7,5,-2,5]
bs_v2(a)
print(a)