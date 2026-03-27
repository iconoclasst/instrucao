
def segundo_maior(array):
    n=len(array)
    maior=array[0]

    for i in range(n):
        if maior <= array[i]:
            maior=array[i]
    sm=array[0]
    for i in range(n):
        if sm <= array[i] and array[i] <=maior:
            sm=array[i]
    return sm

n = int(input("Insira N: "))
array=[]
for i in range(n):
    array.append(int(input("Insira um valor: ")))

sm = segundo_maior(array)
print(array)
print("O segundo maior é ", sm)