#calcula o tamanho de um edificio baseado no numero de andares
#e a altura de cada andar.

def main():
    try:
        #Variaveis para guardar recebimento de dados
        numero_andar = int(input("Qual número de andares possui o edificio? "))
        altura_andar = int(input("Qual a altura de cada andar? "))

        #função para calcular andar
        def calcula_altura(altura, num_andar):
            return altura * num_andar

        #impressão da informação calculada na tela
        print(f'O edificio possui {calcula_altura(numero_andar,altura_andar)} metros de altura')

    #tratamento de erro caso seja informado uma letra
    except ValueError as err:
        print("Apenas numeros devem ser informado")
        return err

if __name__ == '__main__':
    main()
