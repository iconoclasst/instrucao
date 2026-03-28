# problema: Achar o segundo maior número

# Formas de resolver:
# 1- Achar primeiro o maior, fazer outra busca pelo maior e desconsiderar o primeiro maior
# 2- Ordenar o array e pegar o índice 2 

#versão 1
def segundo_maior_v1(array):
    n = len(array)
    maior = array[0]
    imaior=0
    for i in range(n):
        if maior < array[i]:
            maior = array[i]
            imaior=i 

    seg_maior = array[0]
    for i in range(n):
        if seg_maior < array[i] and i != imaior:
            seg_maior = array[i]

    return maior, seg_maior

#versão 2
def segundo_maior_v2(array):
    n = len(array)
    aux = []
    for i in range(n):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[0], array[1]

n = int(input("Insira N: "))
array=[]
for i in range(n):
    array.append(int(input("Insira um valor: ")))

print(array)

# maior, seg_maior = segundo_maior_v2(array)

# print("O maior e o segundo maior são {} e {}".format(maior, seg_maior))

maior1, seg_maior1 = segundo_maior_v1(array)
print("O maior e o segundo maior são {} e {}".format(maior1, seg_maior1))

