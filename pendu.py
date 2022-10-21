#nombre de vies
game_run=True
level=input("Choisir un niveau de difficulté : d pour débutant, i pour intermédiaire ou e pour expert =>")

#initialiser le nombre de vie au départ
if level == "e":
    nb_vie = 4
elif level == "i":
    nb_vie = 7
elif level == "d":
    nb_vie = 10
else:
    print("Ecrire d, i ou e")

print("Nombre de vie de départ",nb_vie) 

#compteur du restant du nombre de vie
count_nb_vie = int(nb_vie)
print("Nombre de vie restante:",count_nb_vie)

#ouvrir le fichier, mettre le chemin si pas dans le même dossier
file_reading = open("dico_france.txt", "r")
dictionnaire = file_reading.read()    #dictionnaire est la variable qui contiendra le contenu (str) du fichier
#print(dictionnaire)
file_reading.close()


chars = "éèêë"
for c in chars:
    dictionnaire = dictionnaire.replace(c, "e")
dictionnaire = dictionnaire.replace(" de", "")
ah = "àâä"
for c in ah:
    dicitonnaire = dictionnaire.replace(c, "a")

#convertir le fichier en list
list_dictionnaire = dictionnaire.split()
#print(list_dictionnaire)

#choisir un mot aléatoire de la liste
import random
rand_word = random.choice(list_dictionnaire)
#print(rand_word)
list_r_word=list(rand_word)
#print(list_r_word)
#afficher le mot vide
nb_letter = len(rand_word)
base_carac = "_"
base_word = base_carac*nb_letter
print(base_word)
list_base_word=list(base_word)
print(list_base_word)

#faire une liste des lettres utilisées
used_letter=[]

#choisir une lettre et vérifier qu'elle est dans le mot
def new_letter():
    global count_nb_vie
    global letter_choose
    letter_choose = input("Choisir une lettre (en minuscule) <  ")
    print("Vous avez choisis la lettre ",letter_choose)
    list_used_letter()
    i=0    
    if letter_choose not in list_r_word:
            count_nb_vie = count_nb_vie - 1 
    while i < (nb_letter):    # <= la boucle while sert à trouver si la lettre choisie est présente,  
        if list_r_word[i]==letter_choose: # <= à quelle emplacement dans le mot
            list_base_word[i]=letter_choose # <= à remplacer l'underscore du mot vide au même emplacement
        elif list_base_word[i] !="_":
            list_base_word[i]=list_base_word[i]    
        else:
           list_base_word[i]="_"
        i+=1
    print(list_base_word)
    print("Il vous reste "+str(count_nb_vie)+" vies!")
    game_loose()
    game_win()
    
def list_used_letter():
    used_letter.append(letter_choose)
    print("Lettres déjà utilisées: ",used_letter)

def all_game():
    while game_run == True:
       new_letter() 

def game_loose():
    global game_run
    if count_nb_vie <= 0:
            game_run = False
            print("Vous avez perdu ! Vous êtes nul ! Le mot était ",rand_word)

def game_win():
    base_carac = "_"
    if base_carac not in list_base_word:
        print("Et c'est un win ! ")
        quit()
all_game()

