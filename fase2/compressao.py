# problema: Dado uma string com n caracteres, gerar uma string com cada caractere seguido da quantidade de vezes que ele aparece
# Exemplo: "aaabbc" = "a3b2c"

def compressao(texto):
    n = len(texto)
    mp = {}
    for i in range(n):
        if texto[i] in mp:
            mp[texto[i]] += 1
        else:
            mp[texto[i]] = 1

    string_comprimida = ""
    for i in mp:
        if mp[i] != 1:
            string_comprimida += i
            string_comprimida += str(mp[i])
        else:
            string_comprimida += i
    return string_comprimida


string = input("Insira uma string: ")

print("String antes: ", string)

print("String depois: ", compressao(string))
# a = compressao(string)
# print(a)


