from itertools import product

#Função para obter a palavra do usuario
def PerguntarPalavra():
    print("Escreva um anagrama:")
    return input()

#Função para decodificar e achar os anagramas da palavra fornecida
def PalavrasAchadas(palavraAnagrama):
    # Ler um arquivo de texto com uma lista de palavras em português
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavrasLista = arquivo.read().splitlines()

    # Criando a matriz
    matriz = []

    palavrasListaTemp = []

    for letra in palavraAnagrama:
        tamanhoAnagrama = len(palavraAnagrama) * [letra];
        matriz.append(tamanhoAnagrama)

    # Imprimindo a matriz
    for linha in matriz:
        print(linha)
    print(matriz[0][1])

    tamanhoDaPalavraAnagrama = len(palavraAnagrama)

    for x in range(tamanhoDaPalavraAnagrama):
        palavrasArrayTemp = []
        for y in range(tamanhoDaPalavraAnagrama):
            while len(palavrasArrayTemp) < tamanhoDaPalavraAnagrama:
                if (y <= tamanhoDaPalavraAnagrama-1) and y != 0:
                    print(y)
                    palavrasArrayTemp.append(matriz[y-1][x])
                    print(f'{y-1},{x},{palavrasArrayTemp}')
                else:
                    palavrasArrayTemp.append(matriz[y-tamanhoDaPalavraAnagrama][x-tamanhoDaPalavraAnagrama])
                    print(f'{x},{y},{palavrasArrayTemp}')

        palavrasListaTemp.append(''.join(palavrasArrayTemp))

    print(palavrasListaTemp)
    print("Número total de palavras:", len(palavrasListaTemp))
    print("Algumas das palavras possíveis:", palavrasListaTemp[:5])  # Exibindo as primeiras 10 palavras como exemplo

# Inicia o script
if __name__ == '__main__':
    obterPalavra = PerguntarPalavra()
    PalavrasAchadas(obterPalavra)


