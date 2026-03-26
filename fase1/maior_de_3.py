
def verificar_maior(array):
    maior = array[0]
    for i in range(1, len(array)):
        if array[i] > maior:
            maior=array[i]
    return maior

numeros = []
for i in range(3):
    numeros.append(int(input("Insira um numero: ")))

print(numeros)
m = verificar_maior(numeros)
print("O maior é {}".format(m))
