# 2026-seance-string-part-002

# 🐍 Mini-projet – Générateur d'identifiant

## Manipulation des variables, chaînes de caractères et modulo

---

## 🎯 Objectif

Ce mini-projet permet de réinvestir les notions étudiées dans les séances précédentes et de réaliser un premier **module Python** avec l'éditeur **PYCHARM**.

L'objectif est de créer un programme capable de générer automatiquement un identifiant à partir du **prénom** et du **nom** d'une personne.

Le projet mobilise notamment :

* les variables ;
* les chaînes de caractères ;
* `len()` ;
* l'indexation et le slicing ;
* `upper()` ;
* les opérations arithmétiques ;
* le modulo `%` ;
* la concaténation ;
* la conversion avec `str()` ;
* l'affichage avec `print()`.

> 💡 **Important :** le projet doit être réalisé avec les notions étudiées jusqu'à présent. Aucune fonction ni structure conditionnelle `if` n'est nécessaire.

---

# 📋 1. Principe du générateur

Le programme utilise deux informations :

```python
prenom = "Codeurix"
nom = "Bugman"
```

L'identifiant est composé de trois parties :

```text
[50 % du prénom]-[50 % du nom]-[numéro]
```

Pour l'exemple :

```text
CODE-BUG-54
```

---

# 🔤 2. Partie prénom

Le programme conserve **50 % des lettres du prénom**.

Exemple :

```text
Codeurix
```

Le prénom contient :

```text
8 lettres
```

50 % de 8 correspond à :

```text
4 lettres
```

La partie conservée est donc :

```text
CODE
```

Le résultat doit être converti en majuscules.

---

# 🔠 3. Partie nom

Le programme conserve également **50 % des lettres du nom**.

Exemple :

```text
Bugman
```

Le nom contient :

```text
6 lettres
```

50 % de 6 correspond à :

```text
3 lettres
```

La partie conservée est donc :

```text
BUG
```

---

# 🔢 4. Calcul du numéro

Le numéro est calculé à partir de la longueur du prénom et du nom.

La formule est :

```text
(3 × longueur du prénom) + (5 × longueur du nom)
```

Avec :

```text
Prénom = 8 lettres
Nom     = 6 lettres
```

le calcul est :

```text
(3 × 8) + (5 × 6)
= 24 + 30
= 54
```

Le numéro obtenu est donc :

```text
54
```

---

# 🚧 5. Limite du numéro

Le numéro ne doit pas dépasser :

```text
80
```

Le projet demande donc de réfléchir à la manière de respecter cette contrainte.

Le **modulo `%`** devra être étudié dans cette partie.

Tester notamment :

```python
numero % 80
```

avec différentes valeurs.

> 🧠 **Attention :** le modulo donne le reste d'une division entière. Il ne constitue pas automatiquement une limitation de valeur à `80`.

À ce stade du projet, aucune instruction `if` n'est nécessaire.

---

# 🖥️ 6. Résultat attendu

Pour :

```python
prenom = "Codeurix"
nom = "Bugman"
```

le programme doit produire un affichage similaire à :

```text
----------------------------------------
       GENERATEUR D'IDENTIFIANT
----------------------------------------

Prénom : Codeurix
Nom : Bugman

Longueur du prénom : 8
Longueur du nom : 6

Partie prénom : CODE
Partie nom : BUG

Numéro : 54

Identifiant : CODE-BUG-54
----------------------------------------
```

---

# 🛠️ 7. Création du module Python

Lancer **IDLE** puis créer un nouveau fichier :

```text
File → New File
```

Enregistrer le fichier sous :

```text
identifiant.py
```

Le fichier `identifiant.py` constitue votre premier **module Python**.

---

# 🧩 8. Étapes de réalisation

## Étape 1 – Créer les variables

Créer :

```python
prenom = "Codeurix"
nom = "Bugman"
```

Afficher les valeurs avec `print()`.

Afficher également leur type :

```python
print(type(prenom))
print(type(nom))
```

### Questions

* Quel est le type de `prenom` ?
* Quel est le type de `nom` ?

---

## Étape 2 – Calculer les longueurs

Utiliser `len()` pour déterminer :

* la longueur du prénom ;
* la longueur du nom.

Créer les variables :

```text
longueur_prenom
longueur_nom
```

afin de conserver les résultats.

---

## Étape 3 – Construire la partie prénom

Créer :

```text
partie_prenom
```

Cette variable doit contenir **50 % du prénom**.

Pour :

```text
Codeurix
```

le résultat attendu est :

```text
CODE
```

Utiliser :

* `len()` ;
* une variable numérique ;
* l'indexation ou le slicing ;
* `upper()`.

Afficher :

```python
print("Partie prénom :", partie_prenom)
```

### Question

Comment déterminer le nombre de caractères correspondant à 50 % du prénom ?

---

## Étape 4 – Construire la partie nom

Créer :

```text
partie_nom
```

Pour :

```text
Bugman
```

le résultat attendu est :

```text
BUG
```

Afficher :

```python
print("Partie nom :", partie_nom)
```

---

## Étape 5 – Calculer le numéro

Créer :

```text
numero
```

Utiliser la formule :

```text
3 × longueur du prénom + 5 × longueur du nom
```

Afficher le résultat.

---

## Étape 6 – Étudier le modulo

Tester :

```python
numero % 2
numero % 5
numero % 10
numero % 80
```

Observer les résultats.

### Questions

1. Que représente le résultat d'une opération modulo ?
2. Que signifie un résultat égal à `0` ?
3. Que représente `numero % 2` ?
4. Que représente `numero % 5` ?
5. Que représente `numero % 10` ?
6. Le modulo `% 80` permet-il à lui seul de garantir un numéro inférieur ou égal à `80` ?

---

## Étape 7 – Construire l'identifiant

Créer :

```text
identifiant
```

L'identifiant doit être composé de :

```text
partie_prenom
+
"-"
+
partie_nom
+
"-"
+
numero
```

Le numéro étant une valeur numérique, utiliser `str()` pour pouvoir le concaténer avec les chaînes de caractères.

Résultat attendu :

```text
CODE-BUG-54
```

---

# 🧪 9. Tests

Modifier les valeurs de `prenom` et `nom` afin de vérifier que le programme fonctionne avec différentes personnes.

### Test 1

```python
prenom = "Alice"
nom = "Martin"
```

Déterminer :

* la longueur du prénom ;
* la longueur du nom ;
* la partie prénom ;
* la partie nom ;
* le numéro ;
* l'identifiant.

---

### Test 2

```python
prenom = "Thomas"
nom = "Durand"
```

Effectuer les mêmes vérifications.

---

### Test 3

Utiliser votre propre prénom et votre propre nom.

Vérifier que l'identifiant est correctement généré.

---

# ⭐ 10. Challenge

Trouver un prénom et un nom suffisamment longs pour que le calcul :

```python
numero = longueur_prenom * 3 + longueur_nom * 5
```

produise une valeur supérieure à :

```text
80
```

Observer le résultat puis rechercher, avec les notions étudiées, une solution permettant de respecter la règle :

```text
numéro maximum = 80
```

### Question

Pourquoi est-il intéressant d'imposer une taille maximale au numéro ?

---

# 📦 11. Livrable

Le projet doit contenir au minimum :

```text
identifiant.py
```

Le fichier doit permettre de modifier facilement :

```python
prenom = "..."
nom = "..."
```

et de générer automatiquement un nouvel identifiant.

Pour l'exemple initial, le programme doit notamment produire :

```text
Prénom : Codeurix
Nom : Bugman
Longueur du prénom : 8
Longueur du nom : 6
Partie prénom : CODE
Partie nom : BUG
Numéro : 54
Identifiant : CODE-BUG-54
```

---

# 🧠 12. Compétences mobilisées

À l'issue du mini-projet, vous devez être capable d'expliquer :

* comment créer et utiliser une variable ;
* comment déterminer la longueur d'une chaîne avec `len()` ;
* comment accéder à une partie d'une chaîne ;
* la différence entre indexation et slicing ;
* comment convertir une chaîne en majuscules avec `upper()` ;
* comment effectuer des calculs à partir de longueurs de chaînes ;
* ce que représente le modulo `%` ;
* pourquoi `str()` est nécessaire pour concaténer un nombre avec une chaîne ;
* comment construire un premier module Python avec IDLE ;
* comment tester un programme avec différentes données.

---

# 🚀 Pour aller plus loin

Une fois le programme fonctionnel, plusieurs améliorations pourront être envisagées dans de prochaines séances :

* demander le prénom à l'utilisateur ;
* demander le nom à l'utilisateur ;
* gérer différents formats de saisie ;
* améliorer l'affichage ;
* transformer certaines opérations en fonctions ;
* séparer les différentes responsabilités du programme ;
* ajouter des contrôles sur les données saisies.

> Ces améliorations seront abordées progressivement au cours de la formation.
