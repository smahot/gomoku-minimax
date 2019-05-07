#Fichier des tests de fonctions
from gomoku import gomoku

g = gomoku()
g.grille = [['1','2','3','4','5','6'],
            ['7','8','9','10','11','12'],
            ['13','14','15','16','17','18'],
            ['19','20','21','22','23','24'],
            ['25','26','27','28','29','30'],
            ['31','32','33','34','35','36']]
g.largeur = 6
g.hauteur = g.largeur

# Test ligne5suite # OK
#==================#
liste1 = [' ', ' ', 'B', 'N', 'N', 'B', 'N', 'N', 'B', ' ', 'N', 'N', 'N', 'N', 'N'] #droite5
liste2 = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ' ', 'N', 'N', 'B', 'N', 'N'] #gauche5+
liste3 = [' ', ' ', 'B', 'N', 'N', 'N', 'N', 'N', 'B', ' ', 'N', 'B', 'N', 'N', 'N'] #centre5
liste4 = [' ', 'B', 'B', 'B', 'B', 'B', 'N', 'N', 'B', ' ', 'N', 'N', 'N', 'N', 'N'] #double5BN
liste5 = [' ', ' ', 'N', ' ', ' ', 'B', 'B', 'B', 'B', ' ', 'N', 'B', ' ', ' ', 'N'] #centre4
liste6 = [' ', ' ', ' ', ' ', ' ', 'B', 'N', 'N', 'B', ' ', 'N', 'B', ' ', ' ', 'N'] #vide5

print(g.ligne5suite(liste1))
print(g.ligne5suite(liste2))
print(g.ligne5suite(liste3))
print(g.ligne5suite(liste4))
print(g.ligne5suite(liste5))
print(g.ligne5suite(liste6))

g.display()
# Resultat N N N B False False
# Test Reussi

g.gagnant()
