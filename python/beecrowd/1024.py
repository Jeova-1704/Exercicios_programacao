def Criptografar(texto):
    primeira_criptografia = ""
    for caractere in texto:
        if caractere.isalpha():
            letra_ascii = ord(caractere)
            if caractere.islower():
                letra_cript = chr((letra_ascii - ord('a') + 3) % 26 + ord('a'))
            else:
                letra_cript = chr((letra_ascii - ord('A') + 3) % 26 + ord('A'))
        else:
            letra_cript = caractere
        primeira_criptografia += letra_cript

    segunda_criptografia = primeira_criptografia[::-1]
    metade = len(segunda_criptografia) // 2
    terceira_criptografia = ""
    for i in range(len(segunda_criptografia)):
        if i >= metade:
            terceira_criptografia += chr(ord(segunda_criptografia[i]) - 1)
        else:
            terceira_criptografia += segunda_criptografia[i]

    return terceira_criptografia

casos = int(input())
for _ in range(casos):
    texto = input()
    print(Criptografar(texto))
