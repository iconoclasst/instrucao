# problema: ver se duas palavras são anagramas

def anag(w1, w2):
    dic1 = {}
    dic2 = {}

    for c in w1:
        if c not in dic1:
            dic1[c] = 1
        else:
            dic1[c] += 1
    
    for c in w2:
        if c not in dic2:
            dic2[c] = 1
        else:
            dic2[c] += 1

    if dic1 == dic2:
        return 1

    # return dic1, dic2

    return 0

    # if len(w1) != len(w2):
    #     return 0

    # for c in w2:
    #     if c not in w1:
    #         return 0

    # return 1 

w1 = input("Primeira palavra: ")
w2 = input("Segunda palavra: ")

# a, b = anag(w1,w2)

# print(a, b)

print("{} e {} {} anagramas".format(w1, w2, "são" if anag(w1, w2) == 1 else "não são"))