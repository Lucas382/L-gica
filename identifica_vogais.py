#recebe do usuario uma string e conta vogais contidas nela.
def main():
    print("Digite um texto para que possa ser identificado o número de vogais: ")
    vogais = ['a', 'e', 'i', 'o', 'u']
    texto = input()

    #conta a quantidade de vogais utilizando list comprehension
    contador = len([letra for letra in texto.lower() if letra in vogais])

    print(f'O numero de vogais neste texto é de: {contador}')

if __name__ == '__main__':
    main()
