prenom = "jean philippe"
nom = "dos santos"

MAX_NUM_ID = 80

print (nom)
print (prenom)

print (type (nom))
print (type (prenom))

#le type des variables prénom et nom sont des chaines de caracteres "str"

#information sur la longueur de la chaine de caractere
longueur_prenom = len(prenom)

longueur_nom=   len(nom)

print(longueur_nom , longueur_prenom)

# extraction de 50% dee la chaine de caracteres + toute les lettres en majuscule
partie_prenom= prenom[ : longueur_prenom//2].upper()
partie_nom= nom [ : longueur_nom//2].upper()

#calculer le numero

numero = 3 * longueur_prenom + 5 * longueur_nom

# print(numero % 2)
# # %2 signifie si le nombre est pair
#
# print(numero % 5)
# #le %5 renvoie la valeur du chiffre des unitées % 5
#
# print(numero % 10)
# # le %10 affiche le chiffre des unités
#
# print(numero % 80)

numero %= MAX_NUM_ID

print( partie_prenom + "-" + partie_nom + "-" + str(numero) )




