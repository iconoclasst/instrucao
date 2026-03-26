
def remover_espacos(palavra):
    aux = ''
    for c in palavra:
        if c == " ":
            aux += ''
        else:
            aux += c
    return aux

palavra = input("Insira uma frase: ")
print("Palavra antes: {}".format(palavra))
a = remover_espacos(palavra)
print("Palavra depois: {}".format(a))
