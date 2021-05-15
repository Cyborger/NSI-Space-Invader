# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import joueur_module
import ennemi_module
import scores_module
import sauvegarde_module


def remise_a_zero(jeu):
    """Permet de rendre les valeurs initiales aux clés ennemis; projectiles; joueur['x'] et joueur['est_vivant'] du
    dictionnaire jeu. Utile lorsque le jeu doit être remis à zéro sans changer de statut de jeu à la mort du joueur.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    jeu["ennemis"] = []
    jeu["projectiles"] = []
    jeu["joueur"]["x"] = width // 2
    jeu["joueur"]["est_vivant"] = True


def game_over(jeu):
    """Permet le passage 'fluide' au menu Game Over en assurant l'enregistrement du score dans le fichier de sauvegarde.
    Supprime les clés 'joueur'; 'ennemis'; 'projectiles' du paramètre jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["score"] > jeu["sauvegarde"]["record"]:
        sauvegarde = jeu["sauvegarde"].copy()  # Pour seulement enregistrer le score dans le fichier

        sauvegarde["record"] = jeu["score"]

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
    imageMode(CENTER)

    joueur_module.afficher(jeu)
    ennemi_module.afficher(jeu)

    if jeu["joueur"]["est_vivant"]:  # Évite la gestion des projectiles à la mort du joueur
        joueur_module.projectiles(jeu)

    scores_module.afficher(jeu)

    # Vérifie les collisions entre le joueur et les ennemis
    ennemi_collision = ennemi_module.collision(jeu["joueur"], jeu)
    if ennemi_collision and jeu["joueur"]["est_vivant"]:
        jeu["joueur"]["est_vivant"] = False  # Enclenche l'animation de mort
        jeu["joueur"]["frame_mort"] = frameCount

    # 3 secondes après la mort du joueur, remise à zéro du plateau de jeu ou passage au Game Over
    if not jeu["joueur"]["est_vivant"] and frameCount > jeu["joueur"]["frame_mort"] + 90:
        if jeu["joueur"]["vies"] == 1:  # Fin du jeu
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
