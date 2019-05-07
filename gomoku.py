# Application de l'algorithme minimax au gomoku
# Fait par Steve MAHOT et Matthieu LOUF

class gomoku:
    def __init__(self):
        self.grille = [[' ' for j in range(15)] for i in range(15)]
        self.grille[7][7]='N'
        self.tour = "B"
        self.hauteur = len(self.grille)
        self.largeur = len(self.grille[0])
        self.tic = 0

        self.distanceJeu = 1

    def display(self):
        intro = '    '
        for i in range(self.hauteur):
            intro += str(i+1)
            if i <=7 :
                intro += '   '
            else:
                intro += '  '
        print(intro)
        for i in range(self.hauteur):
            ligne= str(chr(65+i)+" |")
            for j in range(self.largeur):
                ligne+=' '+self.grille[i][j]+ ' |'
            print(ligne)

    def tourSuivant(self):
        if self.tour == "N":
            self.tour = "B"
        else :
            self.tour = "N"
    
    def gagnant(self):
        res = False
        #lignes :
        for i in range (self.hauteur):
            if res == False:
                res = self.ligne5suite(self.grille[i])

        #colonnes :
        if res == False:
            for i in range (self.largeur):
                if res == False:
                    res = self.ligne5suite(self.grille[j][i] for j in range(self.hauteur))

        #diagonales :
        if res == False:
            for start in range(-self.largeur+1, self.largeur -1):
                if res == False:
                    liste = list()
                    for i in range(self.hauteur - abs(start)):                        
                        liste.append(self.grille[abs(start)+i][i])
                    res = self.ligne5suite(liste)
                if res == False:
                    liste = list()
                    for i in range(abs(start)+1):                        
                        liste.append(self.grille[abs(start)-i][i])
                    res = self.ligne5suite(liste)
        return res

    def matchNul (self):
        res = True
        if self.gagnant() == "N" or self.gagnant() == "B":
            res = False
        for i in range(self.hauteur):
            if " " in self.grille[i]:
                res = False
        return res
    
    def ligne5suite(self, liste):
        liste = list(liste)

        compteur = 1
        signe = ' '
        for i in range(len(liste)):
            if compteur == 5:
                break
            if liste[i] == signe and signe != ' ':
                compteur += 1
            else:
                compteur = 1
                signe = liste[i]
        
        if compteur == 5:
            return signe
        else :
            return False

    def utility (self):
        self.tic += 1
        if self.matchNul():
            return 0
        if self.gagnant() == self.tour:
            return 1
        else:
            return -1
    
    def EstAutour(self,i,j):
        for k in range((2*self.distanceJeu)+1):
                for l in range((2*self.distanceJeu)+1):
                    if (i+k-self.distanceJeu>=0) and (i+k-self.distanceJeu<self.hauteur) and (j+l-self.distanceJeu>=0) and (j+l-self.distanceJeu<self.largeur):
                        if self.grille[i+k-self.distanceJeu][j+l-self.distanceJeu]!=' ':
                            return True
        return False

    def Actions(self):
        acts = []
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if((self.grille[i][j]==' ') and self.EstAutour(i,j)):
                    acts.append([i,j])
        return acts

    def Results(self,position,joueur):
        self.grille[position[0]][position[1]]=joueur

    def MinMax(self):
        actions = list()
        actions.append(self.Actions())
        actions.append(list())
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = self.tour
            min_utility = self.Min_AB(-1,1,1)
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            actions[1].append(min_utility)

        index = actions[1].index(max(actions[1]))
        best = list()
        best.append(actions[0][index])
        best.append(actions[1][index])

        #print("Actions possibles :",actions[0])
        #print("Scores correspondants :",actions[1])
        return best

    def Max_AB(self,alpha,beta,profondeur):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        joueur = self.tour

        max_utility = -2
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            max_utility = max(max_utility,self.Min_AB(alpha,beta,profondeur+1))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            if max_utility >= beta:
                return max_utility
            alpha = max(alpha,max_utility)

        return max_utility

    def Min_AB(self,alpha,beta,profondeur):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        
        if self.tour == 'N':
            joueur = 'B'
        else :
            joueur = 'N'

        min_utility = 2
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            min_utility = min(min_utility,self.Max_AB(alpha,beta,profondeur+1))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            if min_utility<= alpha:
                return min_utility
            beta = min(beta,min_utility)

        return min_utility
