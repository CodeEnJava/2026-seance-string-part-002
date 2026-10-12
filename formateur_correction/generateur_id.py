# la responsabilité de ce module, c'est de générer l'identifiant

from formateur_correction.constantes import (POIDS_PRENOM,
                                             POIDS_NOM,
                                             MAX_NUMERO_ID,
                                             COEF_NOM,
                                             COEF_PRENOM)

from formateur_correction.input import (prenom,
                                        nom)

# -----------------------------------
# Le traitement : la logique métier
# -----------------------------------
# [50 % du prénom]-[50 % du nom]-[numéro]

len_prenom = len(prenom)
len_nom = len(nom)

#(3 × longueur du prénom) + (5 × longueur du nom)
numero = (POIDS_PRENOM * len_prenom + POIDS_NOM * len_nom) % MAX_NUMERO_ID
# chaine de caractères
partie_nom =  nom[:int(COEF_NOM * len_nom)].upper()
partie_prenom = prenom[:int(COEF_PRENOM*len_prenom)].upper()

identifiant =  ( partie_prenom+
       "-" + partie_nom +
       "-" + str(numero))