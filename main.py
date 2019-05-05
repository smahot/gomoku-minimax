# Application de l'algorithme minimax au gomoku
# Fait par Steve MAHOT et Matthieu LOUF

#------------ IMPORTATION MODULES -------------#
import random as rnd
import os
#classe du gomoku dans le fichier gomoku.py
from gomoku import gomoku

#------------ DEFINITION FONCTIONS -------------#

#fonction pour nettoyer la console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def humain_vs_humain():
    m = gomoku()

    print("Début de la partie : \n")

    while not (m.gagnant() or m.matchNul()) :
        
        print("Au tour du joueur \'",m.tour,"\' :")
        m.display()

        print("-> Calcul des actions possibles (peut durer 10s)\n")
        print("Coordonnée conseillée :",m.MinMax(),"\n")
        x = int(input("Jouer à la coordonnée x = "))
        y = int(input("                      y = "))

        m.Results([x,y],m.tour)
        m.tourSuivant()

        cls()
        print("\n")

    m.display()
    gagnant=m.gagnant()
    if gagnant==False:
        print("Match nul :/\n")
    else:
        print("Le gagnant est le joueur \'",m.gagnant(),"\'! :D\n")

def humain_vs_ia():
    m = gomoku()

    rnd.seed()
    type_joueur =['joueur','ia']
    joueur_actuel = rnd.randint(0,1)

    print("Début de la partie : \n")

    while not (m.gagnant() or m.matchNul()) :

        print("Au tour de ",type_joueur[joueur_actuel]," \'",m.tour,"\' :")
        m.display()

        if(type_joueur[joueur_actuel]=='joueur'):
            x = int(input("Jouer à la coordonnée x = "))
            y = int(input("                      y = "))
            m.Results([x,y],m.tour)
        
        else :
            print("-> Calcul des actions possibles (peut durer 10s)\n")
            choix_ia=m.MinMax()
            m.Results([choix_ia[0][0],choix_ia[0][1]],m.tour)
        
        m.tourSuivant()
        joueur_actuel+=1
        if joueur_actuel==2:
            joueur_actuel=0

        cls()
        print("\n")

    m.display()
    gagnant=m.gagnant()
    if gagnant==False:
        print("Match nul :/\n")
    else:
        print("Le gagnant est \'",m.gagnant(),"\'! :D\n")

def menu():
    print("\n 1 : Humain vs Humain assisté par ordinateur\n 2 : Humain vs IA\n")
    choix = int(input("Mode de jeu : "))

    if choix==1:
        humain_vs_humain()
    if choix==2:
        humain_vs_ia()

#------------ Lancement du menu -------------#
menu()