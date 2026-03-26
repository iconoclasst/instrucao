
def contar_vogal(palavra):
    vog = ['a','e','i','o','u']
    ctt = 0
    for c in palavra:
        if c.lower() in vog:
            ctt+=1
    return ctt

palavra = input("insira uma palavra: ")

a = contar_vogal(palavra)
print(a)