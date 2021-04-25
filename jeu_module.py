# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import joueur_module
import ennemi_module
import scores_module

if False:
    from lib.Processing3 import *


def projectiles(jeu):
    """Met à jour chacun des projectiles disponibles selon leurs propriétés disponibles dans la variable jeu.
    Initialise une liste pour les contenir le cas échéant.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "projectiles" not in jeu:
        jeu["projectiles"] = []

    for projectile in jeu["projectiles"][:]:  # Itère sur copie de jeu["projectiles"] afin de supprimer ses éléments
        projectile["y"] += 5 * projectile["orientation"] * projectile["vitesse"]  # Mouvement projectile

        image(jeu["images"]["projectile"], projectile["x"], projectile["y"], projectile["longueur"],
              projectile["largeur"])

        if projectile["y"] < 0:  # Suppression projectiles non affichés par soucis de performances
            jeu["projectiles"].remove(projectile)

        collision = ennemi_module.collision(projectile, jeu)
        if collision:
            collision["est_vivant"] = False
            jeu["scores"]["actuel"] += 10
            jeu["projectiles"].remove(projectile)


def afficher(jeu):
    """Permet d'afficher et de mettre à jour les éléments du jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    imageMode(CENTER)  # Centre les images

    projectiles(jeu)
    joueur_module.afficher(jeu)
    ennemi_module.afficher(jeu)
    scores_module.afficher(jeu)

    ennemi_collision = ennemi_module.collision(jeu["joueur"], jeu)
    if ennemi_collision:
        if jeu["joueur"]["vies"] == 0:
            jeu["joueur"]["est_vivant"] = False  # Enclenche l'animation de mort

            jeu["statut"] = 2

            if jeu["scores"]["actuel"] > jeu["scores"]["record"]:
                jeu["scores"]["record"] = jeu["scores"]["actuel"]

                fichier_record = open("data/record.txt", "w")
                fichier_record.write(str(jeu["scores"]["record"]))
                fichier_record.close()

            jeu["scores"]["actuel"] = 0

            jeu.pop("joueur")
            jeu.pop("ennemis")
            jeu.pop("projectiles")
        else:
            ennemi_collision["est_vivant"] = False
            jeu["joueur"]["vies"] -= 1


def clavier(jeu):
    """Permet au joueur d'intéragir avec son clavier durant le jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    # Mouvement du joueur
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50:  # Le joueur ne dépasse pas la fenêtre
        jeu["joueur"]["x"] += 10
    elif keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
    # Tir de projectiles par le joueur
    elif keyCode == UP or key == " ":
        joueur_module.nouveau_projectile(jeu)
