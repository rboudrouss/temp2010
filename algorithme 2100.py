
"""
[input]  la 1er année, la dernière année,  température ces 10 dernières années
[output] température en 2100
"""
from math import *
from sys import exit
from time import sleep
from os import system
# declare les variables
tableau = {}

valeur = []
ecart = []

type2 = ""

var = 0
ecarttype = 0
somme = 0
sommecart = 0
temp2100 = 0
v = 0
nb = 0


# definis la fonction qui verifie si une variable est un nombre decimal
def isfloat(var):
    try:
        float(var)
    except ValueError:
        return False
    return True
# demande à l'utilisateur ce qu'il veut calculer:


print()
print("-----------")
print()
print("Merci d'avoir utiliser ce programme.")
sleep(.300)
print("Ce programme permet de calculer approximativement les données en 2100.")
sleep(.300)
print("Ces données sont à prendre avec des pincettes, en effet le programme calcule les données dans le cas plus pessimiste,")
sleep(.300)
print("c'est à dire dans le cas où l'humanité ne réagit pas contre le réchauffement climatique.")
sleep(.300)
print()
print("-----------")
print()
sleep(.300)
print("Le programme peut calculer les précipitation, la température et la probabilité de vents forts")
print()
sleep(.300)

type1 = input(
    'Veuillez entrer "p" pour précipitation, "t" pour température ou "v" pour la probabilité de vents forts : ')

# récupère la date de départ
print()
debut = input("entrez la 1er année :")

# cas ou l'utilisateur ne rentre pas un nombre entier
if not debut.isdigit():
    print()
    print("Erreur")
    print("Vous n'avez pas entré un nombre entier")
    exit()

# récupère la dernière date:
print()
end = input("entrez la dernière année :")

# cas ou l'utilisateur ne rentre pas un nombre entier
if not end.isdigit():
    print()
    print("Erreur")
    print("Vous n'avez pas entré un nombre entier")
    exit()

# convertit les variables de chaine de texte à un nombre entier
debut = int(debut)
end = int(end)

# cas ou la dernière date est plus petite que la 1er
if end < debut:
    print()
    print("Erreur")
    print("la dernière année est plus petite que la 1er année")
    exit()

# cas ou les deux dates sont les mêmes
if end == debut:
    print()
    print("Erreur")
    print("il faut au minimum 2 valeurs")
    exit()

# cas ou il y a BEAUCOUP trop de valeurs à entrer
if end - debut > 250:
    print()
    print("Erreur")
    print("Beaucoup trop de valeurs sont nécessité pour la bonne execution du programme : {0} valeurs".format(
        end - debut))
    exit()

# cas ou il y a trop de valeurs à entrer
elif end - debut > 30:
    print()
    print("Attention !")
    print("Le programme vous demandera d'entrer {} valeurs".format(end - debut))
    cont = input("Êtes-vous sûr de vouloir continuer ? o/n ")
    if cont == "o":
        pass
    else:
        print()
        print("Vous avez choisis de quitter le programme.")
        exit()

# récupère toute les valeurs et les classe dans un "dictionnaire"(un tableau à deux entrées)
for i in range(debut, end + 1):
    if type1 == "t":
        print()
        var = input("Entrez température il y avait en " + str(i) + " : ")
        if isfloat(var):
            tableau[i] = float(var)
        else:
            print()
            print("Erreur")
            print("Vous n'avez pas entrer un nombre")
            exit()

    elif type1 == "v":
        print()
        var = input(
            "Entrez la fréquence de vent fort en % par mois qu'il y avait en " + str(i) + " :")
        #<!> A UTILISER ICI----------------------------------
        if isfloat(var):
            tableau[i] = float(var)
        else:
            print()
            print("Erreur")
            print("Vous n'avez pas entrer un nombre")
            exit()
    elif type1 == "p":
        print()
        var = input(
            "Entrez la moyenne du taux de précipitation en mm qu'il y avait en " + str(i) + " : ")
        #<!> A UTILISER ICI------------------------------------
        if isfloat(var):
            tableau[i] = float(var)
        else:
            print()
            print("Erreur")
            print("Vous n'avez pas entrer un nombre")
            exit()


# convertie le dictionnaire en liste de valeur
for i in range(debut, end + 1):
    valeur.append(tableau[i])

# calcul de la somme de toute les valeurs
for i in range(len(valeur)):
    somme += valeur[i]

# calcul de la moyenne
moyenne = somme / len(valeur)

# calcul de l'écart-type
for i in range(len(valeur)):
    v += ((valeur[i] - moyenne)**2) / len(valeur)
ecarttype = sqrt(v)


# tant que l'intervalle [moyenne - ecartype;moyenne+ecartype] contient moins de 95% des valeurs, l'écartype(marge d'erreur) est multuplié par 2
ecarttype2 = ecarttype
while nb < 0.95:
    for i in range(len(valeur)):
        if valeur[i] < moyenne + ecarttype2 and valeur[i] > moyenne - ecarttype2:
            nb += 1
    nb = nb / len(valeur)

    if nb < 0.95:
        ecarttype2 += ecarttype


"""
si l'ecartype est plus petit que 1 et que l'on calcule la température alors :
	la machine calcul l'ecart entre chaque année, établie une moyenne de cet écart
	et calcule avec ma température en 2100 en prenant la 1er valeur entreé dans le code
	et en calculant la différence entre 2100 et multuplie la moyenne des ecarts par cette valeurs
	et rajoute à celle-ci la température en cet année la
sinon la moyenne devient la température approximative en 2100 et l'écartype la marge d'érreur
"""
if ecarttype < 1 and type1 == "t":
    for i in range(1, len(valeur)):
        ecart.append(valeur[i] - valeur[i - 1])

    for i in range(len(ecart)):
        sommecart += ecart[i]

    moyennecart = sommecart / len(ecart)

    temp2100 = moyennecart * (2100 - debut) + tableau[debut]

    print()
    print("Voici les valeurs que vous avez entrez :")

    for i in range(debut, end + 1):
        print("Il faisait {0}°C en moyenne en {1}".format(tableau[i], i))

    print()
    print("La température en 2100 sera de {0}°C ! avec une marge d'erreur de {1}°C".format(
        ceil(temp2100), ceil(ecarttype)))

else:
    if type1 == "t":

        print()
        print("Voici les valeurs que vous avez entrez :")

        for i in range(debut, end + 1):
            print("Il faisait {0}°C en moyenne en {1}".format(tableau[i], i))

        print()

        print("La température en 2100 sera de {0}°C avec une marge d'erreur de {1}°C".format(
            ceil(moyenne), ceil(ecarttype2)))

    elif type1 == "v":

        print()
        print("Voici les valeurs que vous avez entrez :")

        for i in range(debut, end + 1):
            print("Il y avait {0}% de vent fort en {1}".format(tableau[i], i))

        print()

        print("La fréquence de vent forts en 2100 sera de {0}% de chance par mois avec une marge d'erreur de {1}%".format(
            ceil(moyenne), ceil(ecarttype2)))

    elif type1 == "p":

        print()
        print("Voici les valeurs que vous avez entrez :")

        for i in range(debut, end + 1):
            print("Il a plus {0} mm en moyenne en {1}".format(tableau[i], i))

        print()

        print("Le taux de précipitation en 2100 sera de {0} mm avec une marge d'erreur de {1} mm".format(
            ceil(moyenne), ceil(ecarttype2)))

os.system("pause")
