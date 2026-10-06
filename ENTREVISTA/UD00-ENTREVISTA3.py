def numeroPatrones(text):

    text = text.upper()

    contador = 0

    for i in range(len(text)):

        if text[i:i+2] == "00":
            contador += 1

        if text[i:i+3] == "101":
            contador += 1

        if text[i:i+3] == "ABC":
            contador += 1

        if text[i:i+2] == "HO":
            contador += 1

    return contador


texto = input("Introduce una cadena de texto: ")

resultado = numeroPatrones(texto)

print("Número de patrones encontrados:", resultado)