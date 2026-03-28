import random
# problema: recebe dois arrays e mostra a intersecção entre eles (elementos comuns nos dois)

def inter(ar1, ar2):
    n1 = len(ar1)
    n2 = len(ar1)
    aux = {}
    nar = []
    for i in range(n1):
        aux[ar1[i]] = i
    
    for i in range(n2):
        if ar2[i] in aux and ar2[i] not in nar:
            nar.append(ar2[i])

    return nar

# Gerar arrays
n = int(input("Insira N: "))

ar1 = random.sample(range(1,n), n-1)
ar2 = random.sample(range(1,n), n-1)

print("Array 1:",ar1)
print("Array 2:",ar2)

print("A intersecção é", inter(ar1, ar2))