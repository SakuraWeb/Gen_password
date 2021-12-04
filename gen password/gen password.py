import random
from os import name, system

from pycenter import center
from pystyle import Colorate, Colors


def clear():
	system("cls" if name == 'nt' else "clear")


if name =='nt':
	system("title RandomPw & mode 190, 40 ")




banner = """\n
 ▄▄ • ▄▄▄ . ▐ ▄      ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄  
▐█ ▀ ▪▀▄.▀·•█▌▐█    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█▪     ▀▄ █·██▪ ██ 
▄█ ▀█▄▐▀▀▪▄▐█▐▐▌     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌
▐█▄▪▐█▐█▄▄▌██▐█▌    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ 
·▀▀▀▀  ▀▀▀ ▀▀ █▪    .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀• 
     BY S A K U R A
"""


print(Colorate.Vertical(Colors.blue_to_cyan, center(banner, space=60 ), stop=20))

#caractere
lettre = "ABCDEFGHIJKLMNOP"
nombre = "123456789"
symboles = "§£$%@#{}[]()"
caractere = lettre + lettre.lower() + nombre + symboles
caractere_no_symbols = lettre + lettre.lower() + nombre

while True:
    longueurmdp = int(input("Entrez la longueur du mot de passe :"))
    nombredemdp = int(input("Entrez le nombre de mot de passe a gen : "))
    caractere_speciaux_ask = str(input("Voulez-vous des caracteres speciaux ? : "))
    if caractere_speciaux_ask == "y":
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range (0,longueurmdp):
                cmdp = random.choice(caractere)
                mdp = mdp + cmdp
            print('Votre mot de passe est:', mdp)

    elif caractere_speciaux_ask == 'n':
        for i in range(0,nombredemdp):
          mdp = ""  
          for i in range(0,longueurmdp):
              cmdp = random.choice(caractere_no_symbols)
              mdp = mdp + cmdp 
    
        print("Votre mot de passe est:", mdp)
    elif caractere_speciaux_ask !='oui' or 'non':
        print("ERREUR")
