
def palindromo(palavra):
    n = len(palavra)
    pal = ''
    for c in range(n-1, -1, -1):
        pal += palavra[c]
    if palavra == pal:
        return 1
    return 0

palavra = input("insira uma palavra: ")

print("É palindromo!" if palindromo(palavra) == 1 else "Não é palíndromo")