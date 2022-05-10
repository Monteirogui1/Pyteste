# def diz_caract(nome):
#     return f'Olá {nome}, Seja Bem Vindo!!'
#
# retorno_1 = diz_caract('Guilherme')
# retorno_2 = diz_caract(nome="Gui")
#
# print(retorno_1)
# print(retorno_2)

# def cadastro(nome, idade, emprego):
#     print(f'Olá! Meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}.')
#
#
# cadastro('Guilherme', 22, 'Desenvolvedor')

def cal_media_mediana(notas):
    media = sum(notas) / len(notas)
    mediana = 0
    if len(notas) % 2 == 0:
        # Número par de elementos
        indice_ponto_central_menor = int(len(notas)/2 - 1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_menor = notas[indice_ponto_central_menor]
        ponto_central_maior = notas[indice_ponto_central_maior]

        mediana = (ponto_central_menor + ponto_central_maior)/2
    else:
        # Número ímpar de elementos
        notas_ordenadas = sorted(notas)
        indice_mediana = int(len(notas)/2)
        mediana = notas_ordenadas[indice_mediana]

    return media, mediana

resultado_media, resultado_mediano = cal_media_mediana([1, 1, 1, 1, 1])
print(resultado_media)
print(resultado_mediano)
