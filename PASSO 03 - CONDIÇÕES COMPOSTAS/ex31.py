import random
import time


# ----- Variável game --------
i = str("s")
pontosEu = int(0)
pontosMaquina = int(0)
suaJogada = str(" ")
verPlacar = str("n")
numero = random.randrange(1,3)
maquinaJogada = " "

while(i == "s" or i == "sim"):
    
    if (numero == 1):
        maquinaJogada = "Pedra"
    elif (numero == 2):
        maquinaJogada = "Papel"
    else:
        maquinaJogada = "Tesoura"
    maquinaJogada = maquinaJogada.lower()
    
    print(
    """
-----------------------    
        JoKenPo
-----------------------
    Pedra 
    Papel 
    Tesoura 
-----------------------
    """
    )
    time.sleep(0.2)
    suaJogada = str(input("Qual vai ser sua jogada: "))
    suaJogada = suaJogada.lower()
    
    while((suaJogada != "pedra") and (suaJogada != "papel") and (suaJogada != "tesoura")):
        print("Ops, você deve ter escrito errado, por favor sua jogada!! (Pedra-Papel-Tesoura)")
        suaJogada = None
        suaJogada = str(input("Qual vai ser sua jogada: "))
    
    time.sleep(1)
    print("Jo")
    time.sleep(1)
    print("Ken")
    time.sleep(1)
    print("Po")
    time.sleep(1)
    
    print(" ")
    print("-----------------------")
    
    if (suaJogada == maquinaJogada):
        print(f"Você jogou: {suaJogada}, Maquina jogou: {maquinaJogada}")
        time.sleep(1)
        print("----- IMPATE -----")
    elif ((suaJogada == "pedra") and (maquinaJogada == "tesoura")):
        print(f"Você jogou: {suaJogada}, Maquina jogou: {maquinaJogada}")
        time.sleep(1)
        print("----- VOCÊ GANHOU -----")
        pontosEu = pontosEu+1
    elif ((suaJogada == "papel") and (maquinaJogada == "pedra")):
        print(f"Você jogou: {suaJogada}, Maquina jogou: {maquinaJogada}")
        time.sleep(1)
        print("----- VOCÊ GANHOU -----")
        pontosEu = pontosEu+1
    elif ((suaJogada == "tesoura") and (maquinaJogada == "papel")):
        print(f"Você jogou: {suaJogada}, Maquina jogou: {maquinaJogada}")
        time.sleep(1)
        print("----- VOCÊ GANHOU -----")
        pontosEu = pontosEu+1
    else:
        print(f"Você jogou: {suaJogada}, Maquina jogou: {maquinaJogada}")
        time.sleep(1)
        print("----- VOCÊ PERDEU -----")
        pontosMaquina = pontosMaquina+1
    
    # tempo
    time.sleep(1)
    
    print("-"*22)
    
    verPlacar = str(input("Deseja ver o placar? [s,n]: "))
    verPlacar = verPlacar.lower()
    while( (verPlacar != "s" and verPlacar != "sim") and (verPlacar != "n" and verPlacar !="não") ):
        print("Ops, você deve ter escrito errado, por favor diga se vai querer o Placar de pontos, s = sim, n = não")
        verPlacar = str(input("Deseja ver o placar? [s,n]: "))
    if (verPlacar == "sim" or verPlacar == "s"):
        time.sleep(1)
        print("-"*22)
        print(f"Quantidade de pontos:")
        print(f"Eu: {pontosEu}")
        print(f"Maquina: {pontosMaquina}")
    print("-"*22)    
    
    i = str(input("Deseja jogar Novamente: [s,n]: "))
    while( (i != "s" and i != "sim") and (i != "n" and i !="não") ):
        print("Ops, você deve ter escrito errado, por favor diga se vai querer o Placar de pontos, s = sim, n = não")
        verPlacar = str(input("Deseja ver o placar? [s,n]: "))
    time.sleep(1)
    if (i == "n" or i == "não"):
        print("Obrigado por jogar!")
        print("-"*22)
    
    
