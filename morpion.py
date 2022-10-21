begin=input("Voulez-vous jouer ou voir les score ? (j pour jouer, s pour score) ")
score_player1=0
score_player2=0

if begin == "j":
    joueur1=input("Nom du premier joueur: ")
    joueur2=input("Nom du deuxième joueur: ")
elif begin == "s" and score_player1 !=0 and score_player2 !=0:
    print("Joueur 1: ",score_player1)
    print("Joueur 2: ",score_player2)
else:
    print("Avant de commencer, il faut inscrire les joueurs")
    joueur1=input("Nom du premier joueur: ")
    joueur2=input("Nom du deuxième joueur: ")
    print("Voici les scores pour le moment: ")
    print("Joueur 1 => ",score_player1)
    print("Joueur 2 => ",score_player2)


line1 = ["-","-","-"]
line2 = ["-","-","-"]
line3 = ["-","-","-"]
print(line1)
print(line2)
print(line3)


#définir le choix de la case
def game_is_open_for_player1():
    tour_j1=input("Tour de joueur 1. Rentrez le nunermo de la ligne et de la colonne ou vous voulez jouer comme ceci (exemple première ligne et deuxième colonne : 12)")
    if tour_j1 == "11" and line1[0]=="-":
        line1[0]="X"
    elif tour_j1 == "12" and line1[1]=="-":
        line1[1]="X"
    elif tour_j1 == "13" and line1[2]=="-":
        line1[2]="X"
    elif tour_j1 == "21" and line2[0]=="-":
         line2[0]="X"
    elif tour_j1 == "22" and line2[1]=="-":
        line2[1]="X"
    elif tour_j1 == "23" and line2[2]=="-":
            line2[2]="X"
    elif tour_j1 == "31" and line3[0]=="-":
        line3[0]="X"
    elif tour_j1 == "32" and line3[1]=="-":
        line3[1]="X"
    elif tour_j1 == "33" and line3[2]=="-":
        line3[2]="X"
    else:
        print("Cet emplacement est occupé !")
        game_is_open_for_player1_bis()
    print(line1)
    print(line2)
    print(line3)

#définir le choix de la case (doublon pour continuer le jeu si on sélectionne une case déjà occupée)
def game_is_open_for_player1_bis():
    tour_j1=input("Tour de joueur 1. Rentrez le nunermo de la ligne et de la colonne ou vous voulez jouer comme ceci (exemple première ligne et deuxième colonne : 12)")
    if tour_j1 == "11" and line1[0]=="-":
        line1[0]="X" 
    elif tour_j1 == "12" and line1[1]=="-":
        line1[1]="X"  
    elif tour_j1 == "13" and line1[2]=="-":
        line1[2]="X"
    elif tour_j1 == "21" and line2[0]=="-":
        line2[0]="X"
    elif tour_j1 == "22" and line2[1]=="-":
        line2[1]="X"
    elif tour_j1 == "23" and line2[2]=="-":
        line2[2]="X"
    elif tour_j1 == "31" and line3[0]=="-":
        line3[0]="X"
    elif tour_j1 == "32" and line3[1]=="-":
        line3[1]="X"
    elif tour_j1 == "33" and line3[2]=="-":
        line3[2]="X"
    else:
        print("Cet emplacement est occupé !")
        game_is_open_for_player1()
    print(line1)
    print(line2)
    print(line3)


def game_is_open_for_player2():
    tour_j2=input("Tour de joueur 2. Rentrez le nunermo de la ligne et de la colonne ou vous voulez jouer comme ceci (exemple première ligne et deuxième colonne : 12)")
    if tour_j2 == "11" and line1[0]=="-":
        line1[0]="O" 
    elif tour_j2 == "12" and line1[1]=="-":
        line1[1]="O"
    elif tour_j2 == "13" and line1[2]=="-":
        line1[2]="O"
    elif tour_j2 == "21" and line2[0]=="-":
        line2[0]="O"
    elif tour_j2 == "22" and line2[1]=="-":
        line2[1]="O"
    elif tour_j2 == "23" and line2[2]=="-":
        line2[2]="O"
    elif tour_j2 == "31" and line3[0]=="-":
        line3[0]="O"
    elif tour_j2 == "32" and line3[1]=="-":
        line3[1]="O"
    elif tour_j2 == "33" and line3[2]=="-":
        line3[2]="O"
    else:
        print("Cet emplacement est occupé !")
        game_is_open_for_player2_bis()
    print(line1)
    print(line2)
    print(line3)

def game_is_open_for_player2_bis():
    tour_j2=input(" Tour de joueur2. Rentrez le nunermo de la ligne et de la colonne ou vous voulez jouer comme ceci (exemple première ligne et deuxième colonne : 12)")
    if tour_j2 == "11" and line1[0]=="-":
        line1[0]="O"
    elif tour_j2 == "12" and line1[1]=="-":
        line1[1]="O"
    elif tour_j2 == "13" and line1[2]=="-":
        line1[2]="O"
    elif tour_j2 == "21" and line2[0]=="-":
        line2[0]="O"
    elif tour_j2 == "22" and line2[1]=="-":
        line2[1]="O"
    elif tour_j2 == "23" and line2[2]=="-":
        line2[2]="O"
    elif tour_j2 == "31" and line3[0]=="-":
        line3[0]="O"
    elif tour_j2 == "32" and line3[1]=="-":
        line3[1]="O"
    elif tour_j2 == "33" and line3[2]=="-":
        line3[2]="O"
    else:
        print("Cet emplacement est occupé !")
        game_is_open_for_player2()
    print(line1)
    print(line2)
    print(line3)

#définir condition de victoire
def victory():
    global score_player1
    global score_player2
    #pour joueur1
    if line1[0]=="X" and line1[1]=="X" and line1[2]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line2[0]=="X" and line2[1]=="X" and line2[2]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line3[0]=="X" and line3[1]=="X" and line3[2]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[0]=="X" and line2[0]=="X" and line3[0]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[1]=="X" and line2[1]=="X" and line3[1]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[2]=="X" and line2[2]=="X" and line3[2]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[0]=="X" and line2[1]=="X" and line3[2]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[2]=="X" and line2[1]=="X" and line3[0]=="X":
        print(joueur1," a gagné ! Bravo!")
        score_player1 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    #pour joueur2
    if line1[0]=="O" and line1[1]=="O" and line1[2]=="O":
        print(joueur2," a gagné ! Bravo!")
        score_player2 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line2[0]=="O" and line2[1]=="O" and line2[2]=="O":
        print(joueur2," a gagné ! Bravo!")
        score_player2 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line3[0]=="O" and line3[1]=="O" and line3[2]=="O":
        print(joueur2," a gagné ! Bravo!")
        score_player2 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[0]=="O" and line2[0]=="O" and line3[0]=="O":
        print(joueur2," a gagné ! Bravo!")
        score_player2 +=1
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        reset()
    elif line1[1]=="O" and line2[1]=="O" and line3[1]=="O":
        print(joueur2," a gagné ! Bravo!")
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        score_player2 +=1
        reset()
    elif line1[2]=="O" and line2[2]=="O" and line3[2]=="O":
        print(joueur2," a gagné ! Bravo!")
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        score_player2 +=1
        reset()
    elif line1[0]=="O" and line2[1]=="O" and line3[2]=="O":
        print(joueur2," a gagné ! Bravo!")
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        score_player2 +=1
        reset()
    elif line1[2]=="O" and line2[1]=="O" and line3[0]=="O":
        print(joueur2," a gagné ! Bravo!")
        print("Joueur 1: ",score_player1)
        print("Joueur 2: ",score_player2)
        score_player2 +=1
        reset()

def score():
    print(joueur1,score_player1),print(joueur2,score_player2)

def createFile():
    #créer un fichier 
    file_object = open("score.txt", "w")
    str_score = score()
    #mettre la variable score dedans    
    file_object.write(str_score)
    file_object.close()
def createFile():
    #créer un fichier 
    SP1=str(score_player1)
    SP2=str(score_player2)
    file_object = open("score.txt", "a")
    #mettre la variable score dedans 
    str_score=joueur1+":"+SP1+joueur2+":"+SP2
    print(str_score)
    file_object.write(str_score)
    file_object.close()

#pour reset le jeu
def reset():
    reset=input("Voulez-vous recommencer le morpion ? Si vous quittez, les scores seront enregistrer dans un fichier. Taper oui ou non =>  ")
    global line1
    global line2
    global line3
    line1 = ["-","-","-"]
    line2 = ["-","-","-"]
    line3 = ["-","-","-"]
    if reset == "non":
        print("Ce sera tout pour aujourd'hui. Les score seront inscrit dans le fichier score.txt")
        createFile()   
    elif reset == "oui":
        game()
    else:
        reset=input("Je ne comprends pas, oui ou non ?")
    
#déroulé d'une partie
def game():
    game_is_open_for_player1()
    game_is_open_for_player2()
    game_is_open_for_player1()
    game_is_open_for_player2()
    game_is_open_for_player1()
    #vérifier conditions de victoire
    victory()
    game_is_open_for_player2()
    victory()
    game_is_open_for_player1()
    victory()
    game_is_open_for_player2()
    victory()
    game_is_open_for_player1()
    victory()
    print("Partie nul")
    reset()

game()

