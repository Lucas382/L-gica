#Pergunta 5 números para o  usuario e transforma em um array ordenado (ordem decrescente).

def main():
    arr =[]
    aux = []
    for i in range(5):
        arr.append(int(input(f'Digite o {i+1}º número: ')))

    for item in range(len(arr)):
        maior = max(arr)
        aux.append(maior)
        arr.remove(maior)
    print(aux)


if __name__ == '__main__':
    main()
