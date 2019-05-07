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


def humain_vs_ia():
    m = gomoku()

    rnd.seed()
    type_joueur =['joueur','ia']
    joueur_actuel = rnd.randint(0,1)

    print("Début de la partie : \n")
    tour=2
    while not (m.gagnant() or m.matchNul()) :
        print("Au tour de ",type_joueur[joueur_actuel]," \'",m.tour,"\' :")
        m.display()
        if(type_joueur[joueur_actuel]=='joueur'):
            ligne =  input("Jouer à la coordonnée Ligne = ").upper()
            ligne=ord(ligne)-65
            colonne = int(input("                      Colonne = "))
            if tour==3:
                while ligne<=6:
                    ligne =  input("Ligne trop près du centre (minimum 7) : ").upper()
                    ligne=ord(ligne)-65
                while colonne<=6:
                    colonne = int(input("Colonne trop près du centre (minimum 7) : "))        
            m.Results([ligne,colonne],m.tour)
        
        else :
            print("-> Calcul des actions possibles (peut durer 10s)\n")
            choix_ia=m.MinMax()
            if tour==3:
                while choix_ia[0]<=6 or choix_ia[1]<=6:
                    choix_ia=m.MinMax()
            m.Results([choix_ia[0][0],choix_ia[0][1]],m.tour)
        
        m.tourSuivant()
        joueur_actuel+=1
        if joueur_actuel==2:
            joueur_actuel=0

        cls()
        print("\n")
        tour+=1

    m.display()
    gagnant=m.gagnant()
    if gagnant==False:
        print("Match nul :/\n")
    else:
        print("Le gagnant est \'",m.gagnant(),"\'! :D\n")

def menu():
    print("\n Appuyer sur une touche pour commencer \n")

    raw_input()
    humain_vs_ia()

#------------ Lancement du menu -------------#
menu()