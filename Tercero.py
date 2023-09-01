def procesar_palabra1(palabra):
    palabra = palabra.title()
    palabra_procesada = palabra.replace(' ', '').replace('-', '').replace('_', '')
    return palabra_procesada

entrada = input("Ingresa una palabra: ")
resultado = procesar_palabra1(entrada)
print(resultado)



