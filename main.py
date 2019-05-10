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

def demander_coordonnées(tour):
    ligne =  input("Jouer à la coordonnée Ligne = ").upper()
    while len(ligne)!=1:
        ligne =  input("Trop de caractères : ").upper()
    ligne=ord(ligne)-65
    colonne = int(input("                      Colonne = "))
    #while len(colonne)!=1:
    #    colonne =  int(input("Trop de caractères : "))
    if tour==3:
        while (ligne>1 and ligne<14) and (colonne>1 and colonne<14):
            print(ligne,' ',colonne)
            ligne =  input("Ligne trop près du centre (minimum 7) : ").upper()
            while len(ligne)!=1:
                ligne =  input("Trop de caractères : ").upper()
            ligne=ord(ligne)-64
            colonne = int(input("Colonne trop près du centre (minimum 7) : "))
            
    return ligne,colonne

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
            ligne,colonne = demander_coordonnées(tour)
            m.Results([ligne,colonne-1],m.tour)
            self.position_precedente = [ligne,colonne-1]

        else :
            print("-> Calcul des actions possibles (peut durer 10s)\n")
            choix_ia=m.MinMax()
            if tour==3:
                choix_ia=[[0,7]]
                while (choix_ia[0][0]>1 and choix_ia[0][0]<14) and (choix_ia[0][1]>1 and choix_ia[0][1]<14):
                    choix_ia=m.MinMax()
            m.Results([choix_ia[0][0],choix_ia[0][1]],m.tour)
            self.position_precedente = [choix_ia[0][0],choix_ia[0][1]]
        
        m.tourSuivant()

        joueur_actuel+=1
        if joueur_actuel==2:
            joueur_actuel=0
        tour+=1

        cls()
        print("\n")

    m.display()
    gagnant=m.gagnant()
    if gagnant==False:
        print("Match nul :/\n")
    else:
        print("Le gagnant est \'",m.gagnant(),"\'! :D\n")

def menu():
    print("\n Appuyer sur une entrée pour commencer \n")
    input()
    humain_vs_ia()

#------------ Lancement du menu -------------#
menu()