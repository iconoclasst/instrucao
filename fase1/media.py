
def media(array):
    n = len(array)
    sm = 0
    for i in range(n):
        sm+=array[i]
    return sm/n

n = int(input("Insira N: "))
array=[]
for i in range(n):
    array.append(int(input("Insira um valor: ")))

m = media(array)
print(array)
print("A media é {}".format(m))
