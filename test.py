#Fichier des tests de fonctions
from gomoku import gomoku

g = gomoku()
g.grille = [[' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','N','B',' ',' ',' '],
            [' ',' ','B','B','B',' ',' ',' '],
            [' ',' ','N',' ',' ',' ',' ',' '],
            [' ',' ','N',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']]
g.largeur = 8
g.hauteur = g.largeur
g.tour = 'N'
g.limite = 4
g.position_precedente = [3,5]

'''
total = list()
total.append(list())
total.append(list())
for i in range(g.tailleGagnante-2):
    total[0].append([0,0])
    total[1].append([0,0])
'''
# Test ligneXsuite_libre # OK
#==================#
liste1 = [' ', 'B', 'B', 'B', ' ', 'B', 'N', 'N', 'N', ' ', ' ', 'N', 'N', 'N', 'N'] # N
liste2 = ['N', 'B', 'N', 'N', 'N', 'N', 'B', 'N', 'B', ' ', 'N', 'N', 'B', 'N', 'N'] # F
liste3 = [' ', ' ', 'B', 'N', 'N', ' ', 'N', 'N', 'B', ' ', 'N', 'B', 'N', 'N', 'N'] # F
liste4 = [' ', 'B', 'B', 'B', 'B', 'N', 'N', 'N', 'B', ' ', 'N', 'N', 'N', 'N', 'N'] # B
liste5 = [' ', ' ', 'N', ' ', ' ', 'B', 'B', 'B', 'B', ' ', 'N', 'B', ' ', ' ', 'N'] # B
'''
print(g.ligneXsuite_libre(liste1))
print(g.ligneXsuite_libre(liste2))
print(g.ligneXsuite_libre(liste3))
print(g.ligneXsuite_libre(liste4))
print(g.ligneXsuite_libre(liste5))
#résultats OK :

[[[0, 0], [0, 1], [0, 0]], [[0, 0], [1, 0], [1, 0]]]
[[[0, 0], [0, 0], [0, 0]], [[1, 0], [0, 0], [0, 0]]]
[[[0, 0], [0, 0], [0, 0]], [[2, 0], [0, 0], [0, 0]]]
[[[0, 0], [0, 0], [1, 0]], [[0, 0], [0, 0], [1, 0]]]
[[[0, 0], [0, 0], [0, 1]], [[0, 0], [0, 0], [0, 0]]]
'''

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
