# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
from random import randrange


def collision(entite, jeu):
    """Vérifie si l'entité donnée dans le paramètre entite entre en collision avec un des ennemis de la liste
    "ennemis" de la variable jeu.
    
    Paramètres:
        - dict entite: Dictionnaire contenant les propriétés de l'entité.
            (Voir "Propriétés des entités" space_invader.pyde)
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    
    Retourne:
        - dict: Propriétés de l'ennemi de la liste "ennemis" de la variable jeu entrant en collision avec l'entité
            donnée dans le paramètre entite. Dictionnaire vide le cas échéant.
    """
    for ennemi in jeu["ennemis"]:
        if (ennemi["x"] + ennemi["longueur"] // 2 > entite["x"] - entite["longueur"] // 2 and
                ennemi["x"] - ennemi["longueur"] // 2 < entite["x"] + entite["longueur"] // 2 and
                ennemi["y"] + ennemi["largeur"] // 2 > entite["y"] - entite["largeur"] // 2 and
                ennemi["y"] - ennemi["largeur"] // 2 < entite["y"] + entite["largeur"] // 2 and
                entite != ennemi and ennemi["est_vivant"]):
            return ennemi
    return {}


def nouveau_ennemi(jeu):
    """Crée un nouvel ennemi en haut de la fenêtre et l'ajoute à la liste "ennemis" de la variable jeu.
    Possède une position d'abscisse aléatoire dans la fenêtre.
    Possède une taille prédéfinie de 40x38 multipliée à un facteur aléatoire sur [0.8; 1.3[.
    Possède une vitesse aléatoire définie sur [0.5; 1[.
    Possède une orientation aléatoire.

    Cette fonction est récursive et vérifie si l'ennemi crée ne se superpose pas à d'autres ennemis.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    facteur_taille = random(0.8, 1.3)  # Permet de donner une taille différente à chaque ennemi

    ennemi = {
        "x": random(50, width - 50),
        "y": 10,
        "longueur": 40 * facteur_taille,
        "largeur": 38 * facteur_taille,
        "vitesse": 0.8 * jeu["sauvegarde"]["vitesse"],
        "orientation": randrange(-1, 2, 2),  # Défini aléatoirement une orientation positive ou négative (-1 ou 1)
        "est_vivant": True
    }

    if collision(ennemi, jeu):  # Permet d'éviter la superposition des ennemis
        return nouveau_ennemi(jeu)

    jeu["ennemis"].append(ennemi)


def mise_a_jour_ennemi(ennemi, jeu):
    """Vérifie les collisions de l'ennemi donné dans le paramètre ennemi avec les autres ennemis ou s'il touche la
    bordure gauche/droite de la fenêtre afin d'inverser son orientation. Le fait ensuite s'avancer selon sa vitesse
    et son orientation. S'il n'est plus visible en bas de fenêtre, celui-ci sera remplacé par un nouvel ennemi apparu
    en haut de fenêtre."""
    if (collision(ennemi, jeu) or  # Collision avec d'autres ennemis
            ennemi["x"] < ennemi["longueur"] // 2 or  # Collision bordure gauche de la fenêtre
            ennemi["x"] > width - ennemi["longueur"] // 2 or  # Collision avec la bordure droite de la fenêtre
            int(random(500)) == 0):  # Changement d'orientation aléatoire (1 chance sur 500)

        ennemi["orientation"] *= -1  # Inversement de l'orientation

    ennemi["y"] += ennemi["vitesse"]
    ennemi["x"] += ennemi["orientation"]

    if ennemi["y"] > height + 30:  # Retrait des ennemis en bas de fenêtre
        nouveau_ennemi(jeu)  # Évite toute superposition éventuelle non obtenue si simple translation
        jeu["ennemis"].remove(ennemi)


def afficher(jeu):
    """Affiche chacun des ennemis dans la liste "ennemis" de la variable jeu en fonction des propriétés disponibles.
    Initialise cette liste si inexistante.

    Les ennemis apparaissent systématiquement s'ils sont moins de 3 et aléatoirement (1/100 chances par frame) s'ils
        sont moins de 8.
    Les ennemis ne seront mis à jour que si le joueur est vivant.
    Les ennemis ne seront affichés qu'une fois toutes les demis-secondes s'ils sont morts, à tout temps autrement.
    Passé trois secondes après leur mort ou à la mort du joueur, la suppression de l'ennemi a lieu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "ennemis" not in jeu:  # Création des ennemis en début de jeu
        jeu["ennemis"] = []

    if len(jeu["ennemis"]) < jeu["sauvegarde"]["max_ennemis"] and (len(jeu["ennemis"]) < 3 or int(random(100)) == 0):
        nouveau_ennemi(jeu)

    for ennemi in jeu["ennemis"][:]:
        # Mise à jour de l'ennemi si celui-ci ainsi que le joueur sont vivants
        if ennemi["est_vivant"] and jeu["joueur"]["est_vivant"]:
            mise_a_jour_ennemi(ennemi, jeu)

        # Affichage de l'ennemi (en vie ou intervalle périodique de 2 secondes si non vivant pour l'animation)
        if ennemi["est_vivant"] or (frameCount // 15 % 2 == 0 and jeu["joueur"]["est_vivant"]):
            image(jeu["images"][jeu["sauvegarde"]["couleur"]]["ennemi"], ennemi["x"], ennemi["y"], ennemi["longueur"],
                  ennemi["largeur"])

        # Supprime l'ennemi immédiatement si celui-ci ainsi que le joueur sont morts (interrompt l'animation de mort)
        # Supprime l'ennemi après 3 secondes d'animation de clignotement si le joueur est encore vivant
        if ((not ennemi["est_vivant"] and not jeu["joueur"]["est_vivant"]) or
                (not ennemi["est_vivant"] and frameCount > ennemi["frame_mort"] + 90)):
            jeu["ennemis"].remove(ennemi)
