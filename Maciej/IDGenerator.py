prenom = "Codeurix"
nom = "Bugman"
longueur_prenom = len(prenom)
longueur_nom = len(nom)
moitie_prenom = (longueur_prenom)//2
partie_prenom = prenom[:moitie_prenom]
partie_prenom = partie_prenom.upper()
moitie_nom = (longueur_nom)//2
partie_nom = nom[:moitie_nom]
partie_nom = partie_nom.upper()
numero = (3*longueur_prenom)+(5*longueur_nom)

"""
Création programme
"""

identifiant = partie_prenom + "-" + partie_nom + "-" + str(numero)

print ("-"*58)
print ("              GENERATEUR D'IDENTIFIANT")
print ("-"*58)

print("Prénom :",prenom)
print("Nom :", nom)

print("Longueur prénom :", longueur_prenom)
print("Longueur nom :", longueur_nom)

print("Partie prénom :", partie_prenom)
print("Partie nom :", partie_nom)

print("Numéro :", numero)

print("Identifiant :", identifiant)

print("-"*58)
