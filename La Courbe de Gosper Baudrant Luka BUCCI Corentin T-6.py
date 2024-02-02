## BAUDRANT Luka et BUCCI Corentin La courbe de Gosper
from turtle import *
import turtle as t

# On donne les informations de base pour la fonction principale
print("\nFonction à lancer: GosperStart(longueur,nombreEtape,couleur1,couleur2)\n\nlongueur : nombre entier entre 1 et 500 \nnombreEtape: nombre entier entre 0 et 5\ncouleur1 et couleur2 : chaînes de caractères servant à nommer le nom des couleurs que l'on souhaite voir apparaître dans la courbe de gosper\nExemple : GosperStart(100,2,'red','black')")

## Fonction qui trace la courbe de gosper
def gosper(longueur,nombreEtape,direction,couleur1,couleur2,nbcouleur) :
    """
    Fonction:Trace la courbe de gosper selon le nombre d'étape que l'on souhaite. La courbe possède deux formats de schéma (A et B) défini par A = -1 et B = 1.Ils sont identifiés par les deux différentes directions, couleur1 et couleur2 : chaînes de caractères servant à nommer le nom des couleurs que l'on souhaite voir apparaître dans la courbe de gosper, nbcouleur (int) servant à changer de couleur entre couleur1 et couleur2
    Entrée: La longueur du segment de base (nb entier) , le nombre d'étapes de la récursivité, et la direction -1 ou 1 pour le schéma A ou B
    Sortie: La courbe de gosper tracée
    """
     # On initialise l'angle par défaut de la courbe de gosper
    angle = 60
    # On entre dans le schéma de la récursivité
    # Si le nombre d'étape est à 0 alors on trace seulement le segment de base avec la longueur donnée -> condition d'arrêt
    if nombreEtape == 0 :
        # Vérifie le nombre affilié à nbcouleur-> sert à changer la couleur du segment une fois sur 2, la couleur change
        if nbcouleur==1:
            # Met la couleur du segment de la couleur numéro 1
            color(couleur1)
        else:
            # Met la couleur du segment de la couleur numéro 2
            color(couleur2)
        return t.forward(longueur)
    # Sinon on exécute la courbe de Gosper
    else :
        # On divise la longueur par le nombre d'Etape sinon la taille est trop grande par rapport à l'écran
        longueur = longueur/nombreEtape
        # On enlève 1 aux nombres d'étapes pour que la récursivité puisse se terminer
        nombreEtape = nombreEtape-1
        #On vérifie le sens de la direction si -1 alors on tracera la courbe de gosper en haut du point de départ sinon à droite, cela permet de changer la direction de la courbe quand cela est nécéssaire
        # Si la direction correspond à -1-> Schéma A
        if direction==-1 :
            # On trace le schéma A de la courbe de gosper
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,1)
            t.right(angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,2)
            t.right(2*angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,1)
            t.left(angle)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,2)
            t.left(2*angle)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,1)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,2)
            t.left(angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,1)
            t.right(angle)
        else :
            # On trace le schéma B de la courbe de gosper
            t.left(angle)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,2)
            t.right(angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,1)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,2)
            t.right(2*angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,1)
            t.right(angle)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,2)
            t.left(2*angle)
            gosper(longueur,nombreEtape,-1,couleur1,couleur2,1)
            t.left(angle)
            gosper(longueur,nombreEtape,1,couleur1,couleur2,2)

## Fonction à lancer pour la courbe de gosper
def GosperStart(longueur,nombreEtape,couleur1,couleur2):
    """
    Fonction : Fonction qui permet le lancement du tracer de la courbe de Gosper
    Entrée : La longueur du segment de base (nb entier) , le nombre d'étapes de la récursivité (nb entier),couleur1 et couleur2 : chaînes de caractères servant à nommer le nom des couleurs que l'on souhaite voir apparaître dans la courbe de gosper
    Sortie : Lance la fonction gosper qui trace ensuite la courbe de Gosper
    """
    # On lève le stylo pour ne pas faire de tracer lorsque l'on place la tortue sur la feuille au début
    t.up()
    # On initialise les coordonnées pour que le dessin soit centré
    # Par défaut la tortue se trouve aux coordonnées 0x;0y
    # On laisse donc les coordonnées à x à 0 car notre dessin doit être centré
    t.setx(0)
    # On baisse la position de base de la tortue en fonction de la longueur car notre dessin se fait vers le haut
    t.sety(1.5*longueur)
    # Initialisation de la direction
    direction=-1
    # Initialisation du compteur servant à changer de couleur
    nbcouleur=1
    # Colore la tortue en bleu
    t.fillcolor("black")
    # On baisse le stylo pour pouvoir commencer à dessiner
    t.down()
    # On met la vitesse de la tortue au maximum
    t.speed(0)
    # Appelle la fonction Gosper
    gosper(longueur,nombreEtape,direction,couleur1,couleur2,nbcouleur)
    # Cache la tortue une fois le travail finit
    t.hideturtle()
    # Pour pouvoir fermer la fenêtre de Python Graphics
    t.mainloop()




