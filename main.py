from itertools import product

def CriarListaArray(tamanhoDaPalavra, palavraAnagrama):
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

    # Criar uma lista vazia
    tamanhoX = []

    # Adicionar elementos à lista
    for i in range(tamanhoDaPalavra):
        tamanhoX.append(i)

    print(tamanhoX)
    x = 0
    while len(palavrasListaTemp) < tamanhoDaPalavra:
        y = 0
        palavrasArrayTemp = []

        palavrasArrayTemp.append(matriz[y][tamanhoX[x]])
        print(f'{y},{tamanhoX[x]},{palavrasArrayTemp}')

        if(len(palavrasArrayTemp) >= tamanhoDaPalavra):
            palavrasListaTemp.append(''.join(palavrasArrayTemp))

        #Se todos os numeros da array forem o tamanho
        if( tamanhoX[x] > tamanhoDaPalavra):
            x = x + 1

        tamanhoX[x] = tamanhoX[x] + 1
        y = y + 1

    print(palavrasListaTemp)
    print("Número total de palavras:", len(palavrasListaTemp))
    print("Algumas das palavras possíveis:", palavrasListaTemp[:5])  # Exibindo as primeiras 10 palavras como exemplo
    return palavrasListaTemp

#Função para obter a palavra do usuario
def PerguntarPalavra():
    print("Escreva um anagrama:")
    return input()

#Função para decodificar e achar os anagramas da palavra fornecida
def PalavrasAchadas(palavraAnagrama):
    # Ler um arquivo de texto com uma lista de palavras em português
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavrasLista = arquivo.read().splitlines()

    tamanhoDaPalavraAnagrama = len(palavraAnagrama)

    ListaDePalavras = CriarListaArray(tamanhoDaPalavraAnagrama, palavraAnagrama)


# Inicia o script
if __name__ == '__main__':
    obterPalavra = PerguntarPalavra()
    PalavrasAchadas(obterPalavra)


