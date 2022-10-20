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
#convertir le fichier en list
list_dictionnaire = dictionnaire.split()
#print(list_dictionnaire)

#choisir un mot aléatoire de la liste
import random
rand_word = random.choice(list_dictionnaire)
print(rand_word)
list_r_word=list(rand_word)
print(list_r_word)
#afficher le mot vide
nb_letter = len(rand_word)
base_carac = "_"
base_word = base_carac*nb_letter
print(base_word)
list_base_word=list(base_word)
print(list_base_word)

#choisir une lettre

def new_letter():
    global count_nb_vie
    letter_choose = input("Choisir une lettre (en minuscule) <  ")
    print("Vous avez choisis la lettre ",letter_choose)
    i=0    
    while i < (nb_letter - 1):
        if list_r_word[i]==letter_choose:
            list_base_word[i]=letter_choose
            count_nb_vie = count_nb_vie + 1
        elif list_base_word[i] !="_":
            list_base_word[i]=list_base_word[i]
        else:
            list_base_word[i]="_"    
        i+=1
    count_nb_vie = count_nb_vie - 1   
    used_letter=[]
    used_letter.append(letter_choose)
    print("Lettres déjà utilisées: ",used_letter)

    print(list_base_word)
    print("Il vous reste "+str(count_nb_vie)+" vies!")
    if count_nb_vie <= 0:
            game_run = False
            print("Vous avez perdu ! Vous êtes nul !")
            return game_run

    


def all_game():
    while game_run == True:
       new_letter() 
    

all_game()

"""
def find_letter():       
    for letter in rand_word: 
        if letter == letter_choose:
            letter_place = rand_word.find(letter_choose)
            letter_place=int(letter_place)
            print("Place de la lettre dans le mot", letter_place)
            s = list(base_word)
            print(s)
            s[letter_place] = letter_choose
            print(s)

        else:
            #count_nb_vie = count_nb_vie - 1
            print(count_nb_vie)

def find_letter_to_replace():         
    for pos,char in enumerate(rand_word):
        if(char == letter_choose):
            places_letter.append(pos)
            display_places_letter = print(places_letter)

places_letter = []

print("Retour de places_letter: ", display_places_letter)

def replace_underscore():    
    space=" "
    for i in rand_word:
        if i in places_letter:
"""


