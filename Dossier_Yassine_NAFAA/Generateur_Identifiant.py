"""
Mini projet - générateur d'identifiant

Module de NAFAA Yassine.

"""

prenom = input("Entrez votre prénom: ")
nom = input("Entrez votre nom: ")

longueur_prenom = len(prenom)
longueur_nom = len(nom)

numero_id = 3 * longueur_prenom + 5 * longueur_nom

print(numero_id)
numero_max = 80
numero_id = numero_id % 80

identifiant = prenom[:longueur_prenom//2] + "-" + nom[:longueur_nom//2] + "-" + str(numero_id)


identifiant = identifiant.upper()

print("-"*40 , "\n       GENERATEUR D'IDENTIFIANT\n" , "-"*40)
print(f"Prénom : {prenom} \nNom : {nom}\n\nLongueur du prénom : "
      f"{longueur_prenom}\nLongueur du nom : {longueur_nom}\n\nPartie prénom : "
      f"{prenom[:longueur_prenom//2]}\nPartie nom : {nom[:longueur_nom//2]}\n\nNuméro : {numero_id} ")
print(f"Identifiant :{identifiant}")
print("-"*40)