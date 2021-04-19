# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import joueur_module
import ennemi_module

def projectiles(jeu):
    """Met à jour chacun des projectiles disponibles selon leurs propriétés disponibles dans la variable jeu.
    Initialise une liste pour les contenir le cas échéant.
    """
    if "projectiles" not in jeu:
        jeu["projectiles"] = []
    
    for projectile in jeu["projectiles"][:]: # Utilisation du slice afin d'itérer sur une copie de la liste jeu["projectiles"] et de pouvoir supprimer les éléments de la liste originelle
        projectile["y"] += 5  * projectile["orientation"] * projectile["vitesse"] # Pour le mouvement du projectile
        
        image(jeu["images"]["projectile"], projectile["x"], projectile["y"], projectile["longueur"], projectile["largeur"])
        
        if projectile["y"] < 0: # Suppression des projectiles non affichés par soucis de performances
            jeu["projectiles"].remove(projectile)

def afficher(jeu):
    """Permet d'afficher et de mettre à jour les éléments du jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    imageMode(CENTER) # Permet de centrer les images
    
    projectiles(jeu)
    joueur_module.afficher(jeu)
    ennemi_module.afficher(jeu)

def clavier(jeu):
    """Permet au joueur d'intéragir avec son clavier durant le jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    # Mouvement du joueur
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50: # Pour que le joueur ne dépasse pas la fenêtre
        jeu["joueur"]["x"] += 10
    elif keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
    
    # Tir de projectiles par le joueur
    elif keyCode == UP or key == " ":
        joueur_module.nouveau_projectile(jeu)
