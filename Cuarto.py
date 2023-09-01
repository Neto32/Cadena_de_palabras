def procesar_frase2(palabra):
    palabras = palabra.split()
    resultado = ""

    for i, palabra in enumerate(palabras):
        if i == 0:
            resultado += palabra
        elif i % 1 == 0:
            resultado += palabra.title()
        else:
            resultado += palabra.lower()

    palabra_sin_caracteres = resultado.replace(' ', '').replace('-', '').replace('_', '')
    return palabra_sin_caracteres

entrada = input("Ingresa una palabra: ")
resultado_frase = procesar_frase2(entrada)
print(resultado_frase)
