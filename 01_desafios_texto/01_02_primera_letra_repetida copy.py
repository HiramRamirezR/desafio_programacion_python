def primera_letra_repetida(texto):

    texto_minusculas =  texto.lower()
    texto_sin_espacios = texto_minusculas.replace(" ", "")
    lista_de_letras = []

    for letra in texto_sin_espacios:
        if letra in lista_de_letras:
            return letra
        else:
            lista_de_letras.append(letra)

    return None



print(primera_letra_repetida("saltar"))  # a
print(primera_letra_repetida("hola mundo"))   # None
