# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
from random import randrange

def collision(entite, jeu):
    for autre_ennemi in jeu["ennemi"]:
        if (autre_ennemi["x"] + autre_ennemi["longueur"] // 2 > entite["x"] - entite["longueur"] // 2 and
            autre_ennemi["x"] - autre_ennemi["longueur"] // 2 < entite["x"] + entite["longueur"] // 2 and
            autre_ennemi["y"] + autre_ennemi["largeur"] // 2 > entite["y"] - entite["largeur"] // 2 and 
            autre_ennemi["y"] - autre_ennemi["largeur"] // 2 < entite["y"] + entite["largeur"] // 2 and
            entite != autre_ennemi):
            return True
    return False

def nouveau_ennemi(jeu):
    facteur_taille = random(0.8, 1.3)
    
    ennemi = {
        "x": random(50, width - 50),
        "y": 10,
        "longueur": 40 * facteur_taille,
        "largeur": 38 * facteur_taille,
        "vitesse": random(0.5, 1),
        "orientation": randrange(-1, 1, 2),
        "est_vivant": True
    }

    if collision(ennemi, jeu): # Permet d'éviter la superposition des ennemis
        return nouveau_ennemi(jeu)
    
    jeu["ennemi"].append(ennemi)

def afficher(jeu):
    if "ennemi" not in jeu:
        jeu["ennemi"] = []
        for i in range(8):
            nouveau_ennemi(jeu)
    
    for ennemi in jeu["ennemi"][:]:                
        if collision(ennemi, jeu) or ennemi["x"] < ennemi["longueur"] // 2 or ennemi["x"] > width - ennemi["longueur"] // 2 or int(random(500)) == 0: # Collision avec les autres ennemis OU Collision avec les bords de la fenêtre OU changement d'orientation aléatoire 
            ennemi["orientation"] *= -1
        
        if ennemi["y"] > height + 30: # Retrait des ennemis en bas de fenêtre
            nouveau_ennemi(jeu)
            jeu["ennemi"].remove(ennemi)
        
        ennemi["y"] += ennemi["vitesse"]
        ennemi["x"] += ennemi["orientation"]
        image(jeu["images"]["ennemi"], ennemi["x"], ennemi["y"], ennemi["longueur"], ennemi["largeur"])
