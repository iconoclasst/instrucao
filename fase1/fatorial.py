
def fatorial(n):
    aux=1
    for i in range(n, 1, -1):
        aux *= i

    return aux

n = int(input("Insira N: "))
ml = fatorial(n)
print("O fatorial de {} é {}".format(n, ml))
