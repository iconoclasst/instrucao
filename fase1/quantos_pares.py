

def quantos(array):
    n = len(array)
    ctt = 0
    for i in range(n):
        if array[i] % 2 == 0:
            ctt+=1
    return ctt

n = int(input("Insira N: "))
array = []
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)
ctt=quantos(array)
if ctt==0:
    print("O array não tem pares")
if n>1:
    print("O array tem {} pares".format(ctt))
elif n <=1 and ctt==1:
    print("O array tem {} par".format(ctt))
    
