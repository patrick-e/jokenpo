import random

@classmethod
class play():
  def randorizacao(a):
      
    lista = ["pedra", "papel", "tesoura"]
    b = random.choice(lista)

    if b == a:
       print("empate")
    elif a == "pedra" and b == "papel":
          print("voce perdeu")
    elif a == "papel" and b == "tesoura":
          print("voce perdeu")
    elif a == "tesoura" and b == "pedra":
         print("voce perdeu")
    else: 
        print("voce ganhou")
      
play.randorizacao("pedra")
