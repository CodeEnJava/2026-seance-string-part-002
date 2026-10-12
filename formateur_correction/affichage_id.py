# La responsabilité de ced module est d'afficher vers la console
# la fiche qui fait un rec sur un ID


"""
Voici la correction du mini projet

pas maintenant...
La correction sera réalisée le lundi 12 octobre
test GitHub
"""
from formateur_correction.generateur_id import (len_prenom,
                                                len_nom,
                                                partie_prenom,
                                                partie_nom,
                                                numero,
                                                identifiant)

from formateur_correction.input import prenom, nom


# la partie AFFICHAGE DES INFORMATIONS
print("----------------------------------------")
print("       GENERATEUR D'IDENTIFIANT")
print("----------------------------------------")

print("Prénom : ",prenom)
print("Nom : ",nom)

print("Longueur du prénom : ",len_prenom)
print("Longueur du nom :",len_nom)

print("Partie prénom :", partie_prenom)
print("Partie nom :", partie_nom)

print("Numéro : ", numero)

print("Identifiant : ",identifiant)
print("----------------------------------------")