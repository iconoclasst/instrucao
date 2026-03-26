
def busca(array, t):
    n = len(array)
    res = (None, None)
    for i in range(n):
        if array[i] == t:
           res = (i, array[i])
    return res

n = int(input("Insira N: "))

array = []
for i in range(n):
    array.append(int(input("Insira um valor: ")))
t = int(input("Insira o alvo: "))

print(array)
a = busca(array, t)
if a[0] == None:
    print("O valor não estava no array")
else:
    print("O valor {} foi achado no incide {}".format(a[1], a[0]))
