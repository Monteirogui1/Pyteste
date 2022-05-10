def soma(maximo, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados

resultado_soma, numeros_somados = soma(100, 1, 2, 50, 30, 14)
print(resultado_soma)
print(numeros_somados)
