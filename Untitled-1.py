
############################
#        Import            #
############################
 
import random
 
############################
#       Exercice 1         #
############################
 
 
def exercice_1():
    list_notes = []
    # On ouvre le fichier
    notes = open("notes.txt", "r")
    while(True):
        # On lit les lignes
        new_line = notes.readline()
        # Si on lit une ligne vide, o arrette
        if(new_line == ""):
            break
        # on split la ligne dans une liste
        splitted_line = new_line.split()
        sum_notes = 0
        # on fait la somme
        for i in range(1, len(splitted_line)):
            sum_notes += int((splitted_line[i]))
        # on fait la moyenne
        mean_notes = sum_notes / (i)
        # on ajoute la moyenne à la fin de notre ligne
        splitted_line.append(mean_notes)
        # on ajoute cette liste à notre liste de listes
        list_notes.append(splitted_line)
    # On pense bien à fermer le fichier
    notes.close()
    # On ré-écrit nos notes dans le fichier
    ecrire_notes = open("moyennes.txt", "w")
    for listes in list_notes:
        for elem in listes:
            # On re-écrit les éléements de notre liste
            ecrire_notes.write(f"{elem} ")
        # On oublie pas le retour à la ligne
        ecrire_notes.write("\n")
    ecrire_notes.close()