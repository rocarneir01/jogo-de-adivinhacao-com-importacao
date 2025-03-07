import random 
def jogar ():
    print(**********)
    print("Bem-vindos ao jogo de Adivinhação!")
    print(**********)

    numero_secreto = random( random.random(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual o nivel de dificuldade")
    print("(1) Facil(2) Médio(3) Dificil")

    nivel = int(input("Defina o nivel:"))

    if(nivel ==):
        total_de_tentativas = 20
        elif(nivel ==2):
            total_de_tentativas = 10
    else(nivel==3):
                total_de_tentativas = 5
            for rodada in range(1, total_de_tentativas + 1):
                print("Tentativa {} de {}". Format(rodada, total_de_tentativas))
                #Entrada do usuario
                chute_str = input ("Digite um numero entre 1 a 100")
                print("Voce digitou", chute_str)
                chute = int(chute_str)

                #Validação de entrada 
                if (chute < 1 or > 100):
                    print("Voce deve digitar um numero entre um 1 e 100!")
                    continue 
                    acertou = chute == numero_secreto
                    maior = chute > numero_secreto
                    menor = chute < numero_secreto

                    if (acertou)
                        print("Voce acertou e fez {} pontos".format(pontos))
                        break
                    else