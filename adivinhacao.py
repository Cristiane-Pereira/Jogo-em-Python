import random

def jogar():
    print("*************************************")
    print("Bem Vindo(a), ao Jogo de Adivinhação.")
    print("*************************************")

    print("######## BOA SORTE!!! ^ _ ^ #########", "\n")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    rodada = 1
    pontos_iniciais = 1000

    #print(numero_secreto)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3


    while(rodada <= total_de_tentativas):
        print('Tentativa:{} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Dígite um número de 1 a 50:'))
        print('Voce digitou:', chute)

        if(chute < 1 or chute > 50):
            print(' ****** Valor inválido, o número precisa ser entre 1 a 50 ******')
            print("#####################################################################################################","\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns!!! 🎉🎉🎉 Voce acertou o número secreto e fez {} pontos.".format(pontos_iniciais), "\n")
            print("#########################################################################################################", "\n")
            break
        else:
            if(maior):
                print("Que Pena!!! Voce chutou um número maior que o número secreto.", "\n")
                print("#####################################################################################################","\n")
            elif(menor):
                print("Que Pena!!! Voce chutou um número menor que o número secreto.", "\n")
                print("#####################################################################################################", "\n")
        pontos_perdidos = abs(numero_secreto - chute) #40 - 20 = - 20 pontos. (abs) siginifica que teremos somente num absolutos sem num negativos.
        pontos_iniciais = pontos_iniciais - pontos_perdidos

        rodada = rodada +1 #incremento de cada rodada

    print('Fim do Jogo...')

if( __name__ == "__main__"):
    jogar()