# Application de l'algorithme minimax au gomoku
# Fait par Steve MAHOT et Matthieu LOUF

class gomoku:

    def __init__(self):
        self.grille = [[' ' for j in range(3)] for i in range(3)]
        self.tour = "X"

    def display(self):
        print('    0   1   2')
        print("  -------------")
        for i in range(3):
            ligne= str(i)+" |"
            for j in range(3):
                ligne+=' '+self.grille[i][j]+ ' |'
            print(ligne,"\n  -------------")

    def tourSuivant(self):
        if self.tour == "X":
            self.tour = "O"
        else :
            self.tour = "X"
    
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
        if self.gagnant() == "X" or self.gagnant() == "O":
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

    def utility (self):
        if self.matchNul():
            return 0
        if self.gagnant() == self.tour:
            return 1
        else:
            return -1
    
    def Actions(self):
        acts = []
        for i in range(3):
            for j in range(3):
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
            min_utility = self.Min()
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


    def Min(self):
        if self.gagnant() != False or self.matchNul():
            return self.utility()

        actions = list()
        actions.append(self.Actions())
        actions.append(list())
        
        if self.tour == 'X':
            joueur = 'O'
        else :
            joueur = 'X'

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
