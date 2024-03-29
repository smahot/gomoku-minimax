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
        self.limite = 3
        self.position_precedente = [7,7]
        self.maxAction = 8

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
                res = self.ligneXsuite(5, self.grille[i])
        
        #colonnes :
        if res == False:
            for i in range (self.largeur):
                if res == False:
                    liste = list()
                    for j in range(self.hauteur):
                        liste.append(self.grille[j][i])
                    res = self.ligneXsuite(5, liste)

        #diagonales :
        if res == False:
            for start in range(-self.largeur+1, self.largeur -1):
                if res == False:
                    liste = list()
                    for i in range(self.hauteur - abs(start)):                        
                        liste.append(self.grille[abs(start)+i][i])
                    res = self.ligneXsuite(5, liste)
                if res == False:
                    liste = list()
                    for i in range(abs(start)+1):                        
                        liste.append(self.grille[abs(start)-i][i])
                    res = self.ligneXsuite(5, liste)
        return res

    def matchNul (self):
        res = True
        if self.gagnant() == "N" or self.gagnant() == "B":
            res = False
        for i in range(self.hauteur):
            if " " in self.grille[i]:
                res = False
        return res
    
    def ligneXsuite(self, nb, liste):
        liste = list(liste)

        compteur = 1
        signe = ' '
        for i in range(len(liste)):
            if compteur == nb:
                break
            if liste[i] == signe and signe != ' ':
                compteur += 1
            else:
                compteur = 1
                signe = liste[i]
        
        if compteur == nb:
            return signe
        else :
            return False
        
    def ligneXsuite_libre(self, nb, liste):
        liste = list(liste)

        case_libre = False
        compteur = 1
        signe = ' '
        i = 0
        for i in range(len(liste)):
            if compteur == nb:
                break
            if liste[i] == signe and signe != ' ':
                signe = liste[i]
                compteur += 1
            elif liste[i] == signe and signe == ' ':
                compteur = 0
                case_libre = True
            elif liste[i] != signe and signe != ' ':
                case_libre = False
                compteur = 1
                signe = liste[i]                
            else: # liste[i] != signe and signe == ' ':
                case_libre = True
                compteur = 1
                signe = liste[i] 
        
        if compteur == nb:
            if case_libre:
                return signe
            elif i < len(liste) and liste[i] == " ":
                return signe
            else :
                return False
        else :
            return False

    def utility (self):
        if self.matchNul():
            return 0
        joueur1 = self.tour
        joueur2 = "B"
        if joueur1 == "B":
            joueur2 = "N"
        if self.gagnant() == joueur1:
            return 10000
        elif self.gagnant() == joueur2:
            return -10000
        else:
            total = 0
            total += self.nb_Xsuite(4, joueur1)*20
            total -= self.nb_Xsuite(4, joueur2)*20
            total += self.nb_Xsuite(3, joueur1)*5
            total -= self.nb_Xsuite(3, joueur2)*5
            return total

    def nb_Xsuite(self, nb, joueur):
        total = 0
        #lignes :
        for i in range (self.hauteur):
            if joueur == self.ligneXsuite_libre(nb, self.grille[i]):
                total += 1

        #colonnes :
            for i in range (self.largeur):
                if joueur == self.ligneXsuite_libre(nb, (self.grille[j][i] for j in range(self.hauteur))):
                    total += 1

        #diagonales :
            for start in range(-self.largeur+1, self.largeur -1):
                liste = list()
                for i in range(self.hauteur - abs(start)):
                    liste.append(self.grille[abs(start)+i][i])
                if joueur == self.ligneXsuite_libre(4, liste):
                    total += 1

                liste = list()
                for i in range(abs(start)+1):                        
                    liste.append(self.grille[abs(start)-i][i])
                if joueur == self.ligneXsuite_libre(4, liste):
                    total += 1
        return total


    def EstAutour(self,i,j):
        for k in range((2*self.distanceJeu)+1):
                for l in range((2*self.distanceJeu)+1):
                    if (i+k-self.distanceJeu>=0) and (i+k-self.distanceJeu<self.hauteur) and (j+l-self.distanceJeu>=0) and (j+l-self.distanceJeu<self.largeur):
                        if self.grille[i+k-self.distanceJeu][j+l-self.distanceJeu]!=' ':
                            return True
        return False

    def Actions(self, taille):
        acts = []
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if((self.grille[i][j]==' ') and self.EstAutour(i,j)):
                    acts.append([i,j])
        for i in range(len(acts)):
            acts[i].append(abs((acts[i][0]-self.position_precedente[0])**2+(acts[i][1]-self.position_precedente[1])**2))

        
        acts.sort(key=lambda x : x[2])
        best_acts = list()
        length = min(taille, len(acts))
        for i in range(length):
            best_acts.append(list())
            best_acts[i].append(acts[i][0])
            best_acts[i].append(acts[i][1])
        return best_acts

    def Results(self,position,joueur):
        self.grille[position[0]][position[1]]=joueur

    def MinMax(self):
        actions = list()
        actions.append(self.Actions(self.maxAction))
        actions.append(list())
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = self.tour
            position_temp = self.position_precedente
            self.position_precedente = [actions[0][i][0],actions[0][i][1]]
            min_utility = self.Min_AB(-10000,10000,1)
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            self.position_precedente = position_temp
            actions[1].append(min_utility)

        index = actions[1].index(max(actions[1]))
        print(actions)
        best = list()
        best.append(actions[0][index])
        best.append(actions[1][index])

        print("Actions possibles :",actions[0])
        print("Scores correspondants :",actions[1])
        return best

    def Max_AB(self,alpha,beta,profondeur):
        if self.gagnant() != False or self.matchNul():
            return self.utility()
        if profondeur > self.limite:
            return self.utility()

        actions = list()
        actions.append(self.Actions(self.maxAction-profondeur))
        joueur = self.tour

        max_utility = -10000
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            position_temp = self.position_precedente
            self.position_precedente = [actions[0][i][0],actions[0][i][1]]
            max_utility = max(max_utility,self.Min_AB(alpha,beta,profondeur+1))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            self.position_precedente = position_temp
            if max_utility >= beta:
                return max_utility
            alpha = max(alpha,max_utility)

        return max_utility

    def Min_AB(self,alpha,beta,profondeur):
        if self.gagnant() != False or self.matchNul():
            return self.utility()
        if profondeur > self.limite:
            return self.utility()

        actions = list()
        actions.append(self.Actions(self.maxAction-profondeur))
        
        if self.tour == 'N':
            joueur = 'B'
        else :
            joueur = 'N'

        min_utility = 10000
        for i in range(len(actions[0])):
            self.grille[actions[0][i][0]][actions[0][i][1]] = joueur
            position_temp = self.position_precedente
            self.position_precedente = [actions[0][i][0],actions[0][i][1]]
            min_utility = min(min_utility,self.Max_AB(alpha,beta,profondeur+1))
            self.grille[actions[0][i][0]][actions[0][i][1]] = " "
            self.position_precedente = position_temp
            if min_utility<= alpha:
                return min_utility
            beta = min(beta,min_utility)

        return min_utility
