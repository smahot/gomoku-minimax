#Fichier des tests de fonctions
from gomoku import gomoku

g = gomoku()
g.grille = [[' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','N','B',' '],
            [' ',' ',' ','B','B',' '],
            [' ',' ','N',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ']]
g.largeur = 6
g.hauteur = g.largeur

# Test ligneXsuite_libre # OK
#==================#
liste1 = [' ', ' ', 'B', 'N', 'N', 'B', 'N', 'N', 'B', ' ', ' ', 'N', 'N', 'N', 'N'] # N
liste2 = ['N', 'B', 'N', 'N', 'N', 'N', 'B', 'N', 'B', ' ', 'N', 'N', 'B', 'N', 'N'] # F
liste3 = [' ', ' ', 'B', 'N', 'N', ' ', 'N', 'N', 'B', ' ', 'N', 'B', 'N', 'N', 'N'] # F
liste4 = [' ', 'B', 'B', 'B', 'B', 'N', 'N', 'N', 'B', ' ', 'N', 'N', 'N', 'N', 'N'] # B
liste5 = [' ', ' ', 'N', ' ', ' ', 'B', 'B', 'B', 'B', ' ', 'N', 'B', ' ', ' ', 'N'] # B

print(g.ligneXsuite_libre(4, liste1))
print(g.ligneXsuite_libre(4, liste2))
print(g.ligneXsuite_libre(4, liste3))
print(g.ligneXsuite_libre(4, liste4))
print(g.ligneXsuite_libre(4, liste5))

g.display()
# Resultat NFFBB
# Test Reussi

print(g.MinMax())

print("fin")

#test EstAutour
"""g.largeur = 4
g.hauteur = g.largeur
g.grille = [[' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ','N',' '],
            [' ',' ',' ',' '],]
g.display()
g.Actions()"""
