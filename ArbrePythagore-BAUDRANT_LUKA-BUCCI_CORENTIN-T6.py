##BAUDRANT LUKA CORENTIN BUCCI
import turtle as t
from math import*

## FONCTION DE TRACAGE DE CARRE
def carre(longueur, color):
    """
    Fonction: Creer un carré de côté= longueur et colorie l'intérieur
    Entrée: La longueur des côtés du carré et la couleur qui sera à l'intérieur
    Sortie: Un carré de côté = longueur tracé dans le Pyhton Turtle Graphic
    """
    # Colorie l'intérieur du carré
    t.fillcolor(color)
    # Commence à colorier l'intérieur du carré qui va être creer
    t.begin_fill()
    # Creer le carré
    for i in range(4):
        t.forward(longueur)
        t.right(90)
    # Arrête de colorier
    t.end_fill()

## FONCTION QUI TRACE L'ARBRE DE PYTHAGORE
def PythagoreTracee(nombreEtape,longueur):
    """
    Fonction: Trace l'arbre de Pythagore
    Entrée: Le nombre d'Etapes : un nombre entier (int) et une longueur
    Sortie: L'arbre de pythagore tracé dans le Pyhton Turtle Graphic
    """
    # Colorie l'intérieur de rouge, de bleu et de jaune une fois sur 3
    # Ses couleurs ont été choisi par pur hasard, et on les trouvait belles
    if nombreEtape%3==0:
        color='red'
    if nombreEtape%3==1:
        color='blue'
    if nombreEtape%3==2:
        color='yellow'
    # Cas d'arrêt
    if nombreEtape==0:
        # Trace un carré en cas d'arrêt
        carre(longueur,color)
    else:
        # Trace un carré de côté=longueur
        carre(longueur, color)
        # Permet la création de l'arbre de pythagore
        # Creer ou repasse sur le carré principale ou 2 autre plus petit carrés seront crées
        # Permet de se placer dans l'angle en haut à droite pour tracé le carré
        t.forward(longueur)
        #On se place pour faire le premier petit carré
        t.left(45)
        # Appel récursif pour les petits carrés
        # On rappel la fonction 2 fois dans la fonction car il y a deux carrés
        # On rappel la fonction avec une longueur de longueur/√2 car c'est le rapport de grandissement entre les 2 petits carrés et leur carré principale
        PythagoreTracee(nombreEtape-1,longueur/sqrt(2))
        # On vient se replacer pour faire le deuxième carré
        # C'est un triangle rectangle donc on tourne de 90°
        t.right(90)
        # On avance de la longueur du petit carré
        t.forward(longueur/sqrt(2))
        # Appel récursif pour les petits carrés
        # On rappel la fonction avec une longueur de longueur/√2 car c'est le rapport de grandissement entre les 2 petits carrés et leur carré principale
        PythagoreTracee(nombreEtape-1,longueur/sqrt(2))
        # On se replace soit pour aller sur un autre carré principale où il faudra creer 2 autres petits carrés soit pour se replacer au début du 1er carré
        t.back(longueur/sqrt(2))
        t.left(45)
        t.back(longueur)

## FONCTION DE DEPART
def ArbrePythagoreStart(nombreEtape,longueur,vitesse):
    """
    Fonction: Lance le programme pour tracé l'Arbre de Pythagore, Fonction de lancement
    Entrée: Le nombre d'Etape de la récursivité en nombre entier(int), la longueur et la vitesse de tracé de la tortue
    Sortie: L'arbre de Pythagore tracé
    """
    # Lève le stylo pour éviter d'avoir un trait lors du déplacement pour l'initialisation des coordonnées
    t.up()
    # On centre la figure
    t.setx(-0.5*longueur)
    t.sety(-1*longueur)
    # Repose le stylo une fois le travail finit
    t.down()
    # Choisi la vitesse pour tracé l'arbre de Pythagore
    t.speed(vitesse)
    # Tourne de 90° pour que l'arbre se fasse vers le haut, en dehors de la récursivité pour que l'action se fasse qu'une seul fois
    t.left(90)
    # Lance la fonction de traçage
    PythagoreTracee(nombreEtape,longueur)
    # Cache la tortue une fois le travail finit
    t.hideturtle()
    t.mainloop()
ArbrePythagoreStart(6,200,400)