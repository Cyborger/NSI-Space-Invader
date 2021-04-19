# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
from random import randrange

def collision(entite, jeu):
    """Vérifie si l'entité donnée dans le paramètre entite entre en collision avec un des ennemis de la liste "ennemis" de la variable jeu.
    
    Paramètre:
        - dict entite: Dictionnaire contenant les propriétés de l'entité. (Voir "Propriétés des entités" dans space_invader.pyde)
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    
    Retourne:
        - dict: Propriétés de l'ennemi de la liste "ennemis" de la variable jeu entrant en collision avec l'entité donnée dans le paramètre entite.
            Dictionnaire vide le cas échéant.
    """
    for ennemi in jeu["ennemis"]:
        if (ennemi["x"] + ennemi["longueur"] // 2 > entite["x"] - entite["longueur"] // 2 and
            ennemi["x"] - ennemi["longueur"] // 2 < entite["x"] + entite["longueur"] // 2 and
            ennemi["y"] + ennemi["largeur"] // 2 > entite["y"] - entite["largeur"] // 2 and 
            ennemi["y"] - ennemi["largeur"] // 2 < entite["y"] + entite["largeur"] // 2 and
            entite != ennemi):
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
    facteur_taille = random(0.8, 1.3) # Permet de donner une taille différente à chaque ennemi
    
    ennemi = {
        "x": random(50, width - 50),
        "y": 10,
        "longueur": 40 * facteur_taille,
        "largeur": 38 * facteur_taille,
        "vitesse": random(0.5, 1),
        "orientation": randrange(-1, 2, 2), # Permet de définir aléatoirement une orientation positive ou négative (pas de 2 pour éviter zéro)
        "est_vivant": True
    }

    if collision(ennemi, jeu) != {}: # Permet d'éviter la superposition des ennemis
        return nouveau_ennemi(jeu)
    
    jeu["ennemis"].append(ennemi)

def afficher(jeu):
    """Met à jour et affiche chacun des ennemis dans la liste "ennemis" de la variable jeu selon les propriétés disponibles.
    Initialise cette liste si inexistante.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "ennemis" not in jeu: # Création des ennemis en début de jeu
        jeu["ennemis"] = []
        for i in range(8):
            nouveau_ennemi(jeu)
    
    for ennemi in jeu["ennemis"][:]: # Mise à jour des ennemis
        if (collision(ennemi, jeu) != {} or # Collision avec d'autres ennemis
            ennemi["x"] < ennemi["longueur"] // 2 or # Collision avec la bordure gauche de la fenêtre
            ennemi["x"] > width - ennemi["longueur"] // 2 or # Collision avec la bordure droite de la fenêtre
            int(random(500)) == 0): # Changement d'orientation aléatoire (1 chance sur 500)

            ennemi["orientation"] *= -1 # Inversement de l'orientation
        
        if ennemi["y"] > height + 30: # Retrait des ennemis en bas de fenêtre
            nouveau_ennemi(jeu) # Création d'un nouvel ennemi plutôt que d'effectuer une translation afin d'éviter toute superposition éventuelle
            jeu["ennemis"].remove(ennemi)
        
        ennemi["y"] += ennemi["vitesse"]
        ennemi["x"] += ennemi["orientation"]

        image(jeu["images"]["ennemi"], ennemi["x"], ennemi["y"], ennemi["longueur"], ennemi["largeur"])
