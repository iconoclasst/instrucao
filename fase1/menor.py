
def menor(array):
    n = len(array)
    m = array[0]
    for i in range(n):
        if array[i] <= m:
            m = array[i]
    return m

n = int(input("Insira N: "))

array = []
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)
m = menor(array)
print("O menor valor é {}".format(m))
