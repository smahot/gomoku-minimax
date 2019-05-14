# Application de l'algorithme minimax au gomoku
# Fait par Steve MAHOT, Matthieu LOUF et Edwin RAQUIN

#------------ IMPORTATION MODULES -------------#
import random as rnd
import os
#classe du gomoku dans le fichier gomoku.py
from gomoku import gomoku

#------------ DEFINITION FONCTIONS -------------#

#fonction pour nettoyer la console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def demanderInt(min,max):
    result = -1
    try:
        result=int(input())
    except:
        print("Ce ne n'est pas un int")

    while (result<min) or (result>max):
        print("Une valeur entre ", min," et ", max)
        try:
            result = int(input())
        except:
            print("Ce ne n'est pas un int")
        
    return result

def demanderChar():
    ligne =  input().upper()
    while len(ligne)!=1:
        ligne =  input("Trop de caractères : ").upper()
    return ligne

def demander_coordonnées(tour):
    print("Jouer à la coordonnée Ligne = ")
    ligne =  demanderChar()
    ligne=ord(ligne)-65
    print("Colonne = ")
    colonne = demanderInt(1,15)
    
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
    print("Qui commence ? 0-joueur 1-ia")
    joueur_actuel = demanderInt(0,1)
    print("Quel couleur de pion commence ? N ou B")
    pion_actuel = demanderChar()
    print(pion_actuel)
    m.grille[7][7]= pion_actuel
    m.tour = pion_actuel
    m.tourSuivant()
    
    joueur_actuel+=1
    if joueur_actuel==2:
        joueur_actuel=0

    print("Début de la partie : \n")
    tour=2

    while not (m.gagnant() or m.matchNul()) :
        print("Au tour de ",type_joueur[joueur_actuel]," \'",m.tour,"\' :")
        m.display()

        if(type_joueur[joueur_actuel]=='joueur'):
            ligne,colonne = demander_coordonnées(tour)
            m.Results([ligne,colonne-1],m.tour)
            m.position_precedente = [ligne,colonne-1]

        else :
            print("-> Calcul des actions possibles (peut durer 10s)\n")
            choix_ia=m.MinMax()
            if tour==3:
                choix_ia=[[0,7]]
                while (choix_ia[0][0]>1 and choix_ia[0][0]<14) and (choix_ia[0][1]>1 and choix_ia[0][1]<14):
                    choix_ia=m.MinMax()
            m.Results([choix_ia[0][0],choix_ia[0][1]],m.tour)
            m.position_precedente = [choix_ia[0][0],choix_ia[0][1]]
            '''Pour l'affichage de toutes les possibilités
            print("\n Appuyer sur une entrée pour continuer \n")
            input()
            '''
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