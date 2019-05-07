# Application de l'algorithme minimax au gomoku
# Fait par Steve MAHOT et Matthieu LOUF

class gomoku:
    def __init__(self):
        self.grille = [[' ' for j in range(15)] for i in range(15)]
        self.tour = "N"
        self.hauteur = len(self.grille)
        self.largeur = len(self.grille[0])

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
        #3 lignes :
        for i in range (3):
            if res == False and self.identiqueList(self.grille[i]):
                res = self.grille[i][0]

        #3 colonnes :
        if res == False:
            for i in range (3):
                if res == False and self.identiqueList(self.grille[j][i] for j in range(3)):
                    res = self.grille[0][i]

        #2 diagonales :
        if res == False and self.identiqueList(self.grille[i][i] for i in range(3)):
            res = self.grille[0][0]
        if res == False and self.identiqueList(self.grille[i][2-i] for i in range(3)):
            res = self.grille[0][2]
        return res

    def matchNul (self):
        res = True
        if self.gagnant() == "N" or self.gagnant() == "B":
            res = False
        for i in range(3):
            if " " in self.grille[i]:
                res = False
        return res
        
    def identiqueList(self, liste):
        liste = list(liste)
        res = True

        if liste[0] == ' ': #exception
            return False

        for i in liste:
            if i != liste[0]:
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
        if self.matchNul():
            return 0
        if self.gagnant() == self.tour:
            return 1
        else:
            return -1
    
    def Actions(self):
        acts = []
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if(self.grille[i][j]==' '):
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
            min_utility = self.Min_AB(alpha,beta)
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            actions[1].append(min_utility)

        index = actions[1].index(max(actions[1]))
        best = list()
        best.append(actions[0][index])
        best.append(actions[1][index])

        print("Actions possibles :",actions[0])
        print("Scores correspondants :",actions[1])
        return best
    
    def Max(self):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        actions.append(list())
        joueur = self.tour
        if len(actions[0]) == 1:
            self.grille[actions[0][0][0]][actions[0][0][1]] = joueur
            utility = self.utility()
            self.grille[actions[0][0][0]][actions[0][0][1]] = " "
            return utility
        
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            min_utility = self.Min()
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            actions[1].append(min_utility)
        
        max_utility = max(actions[1])
        return max_utility

    def Max_AB(self,alpha,beta):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        joueur = self.tour

        #if len(actions[0]) == 1:
        #    self.grille[actions[0][0][0]][actions[0][0][1]] = joueur
        #    utility = self.utility()
        #    self.grille[actions[0][0][0]][actions[0][0][1]] = " "
        #    return utility
        
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            max_utility = max(max_utility,self.Min_AB(alpha,beta))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            if max_utility >= beta:
                return max_utility
            alpha = max(alpha,max_utility)

        return max_utility

    def Min(self):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        actions.append(list())
        
        if self.tour == 'N':
            joueur = 'B'
        else :
            joueur = 'N'

        if len(actions[0]) == 1:
            self.grille[actions[0][0][0]][actions[0][0][1]] = joueur
            utility = self.utility()
            self.grille[actions[0][0][0]][actions[0][0][1]] = " "
            return utility
        
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            max_utility = self.Max()
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            actions[1].append(max_utility)
        
        min_utility = min(actions[1])
        return min_utility

        def Min_AB(self,alpha,beta):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        
        if self.tour == 'N':
            joueur = 'B'
        else :
            joueur = 'N'

        #if len(actions[0]) == 1:
        #    self.grille[actions[0][0][0]][actions[0][0][1]] = joueur
        #    utility = self.utility()
        #    self.grille[actions[0][0][0]][actions[0][0][1]] = " "
        #    return utility
        
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            min_utility = min(min_utility,self.Max_AB(alpha,beta)))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            if min_utility<= alpha:
                return min_utility
            beta = min(beta,min_utility)

        return min_utility
