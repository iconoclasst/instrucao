

def par_impar(n):
    if(n%2 == 0):
        return 1
    return 0

n = int(input("Insira N: "))

print("Par" if par_impar(n)==1 else "Impar")
