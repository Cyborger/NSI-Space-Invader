# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import joueur_module
import ennemi_module
import scores_module
import sauvegarde_module

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
            jeu["projectiles"].remove(projectile)
            jeu["scores"]["actuel"] += 10
            collision["frame_mort"] = frameCount  # Permet le fonctionnement de l'animation de l'entité touché
            collision["est_vivant"] = False


def remise_a_zero(jeu):
    """Permet de rendre les valeurs initiales aux clés ennemis; projectiles; joueur['x'] et joueur['est_vivant'].
    Utile lorsque le jeu doit être remis à zéro sans changer de statut de jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    jeu["ennemis"] = []
    jeu["projectiles"] = []
    jeu["joueur"]["x"] = width // 2
    jeu["joueur"]["est_vivant"] = True


def game_over(jeu):
    """Permet le passage 'fluide' au menu Game Over. Assure l'enregistrement du score dans le fichier data/record.txt.
    Supprime les clés 'joueur'; 'ennemis'; 'projectiles' du paramètre jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["scores"]["actuel"] > jeu["scores"]["record"]:
        sauvegarde = sauvegarde_module.charger()

        sauvegarde["record"] = jeu["scores"]["actuel"]

        sauvegarde_module.sauvegarder(sauvegarde)

    jeu.pop("joueur")
    jeu.pop("ennemis")
    jeu.pop("projectiles")

    jeu["statut"] = 2


def afficher(jeu):
    """Permet d'afficher et de mettre à jour les éléments du jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    imageMode(CENTER)  # Centre les images

    joueur_module.afficher(jeu)
    ennemi_module.afficher(jeu)

    if jeu["joueur"]["est_vivant"]:
        projectiles(jeu)

    scores_module.afficher(jeu)

    ennemi_collision = ennemi_module.collision(jeu["joueur"], jeu)
    if ennemi_collision and jeu["joueur"]["est_vivant"]:
        jeu["joueur"]["est_vivant"] = False  # Enclenche l'animation de mort
        jeu["joueur"]["frame_mort"] = frameCount

    if not jeu["joueur"]["est_vivant"] and frameCount > jeu["joueur"]["frame_mort"] + 90:
        if jeu["joueur"]["vies"] == 0:
            game_over(jeu)
        else:
            jeu["joueur"]["vies"] -= 1
            remise_a_zero(jeu)


def clavier(jeu):
    """Permet au joueur d'intéragir avec son clavier durant le jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if not jeu["joueur"]["est_vivant"]:  # Empêche le mouvement du joueur s'il est mort
        return

    # Mouvement du joueur
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50:  # Le joueur ne dépasse pas la fenêtre
        jeu["joueur"]["x"] += 10
    elif keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
    # Tir de projectiles par le joueur
    elif keyCode == UP or key == " ":
        joueur_module.nouveau_projectile(jeu)
