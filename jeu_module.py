# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import joueur_module
import ennemi_module
    
def scores(jeu):
    pass
            
def afficher(jeu):
    background(0)
    imageMode(CENTER)
    
    joueur_module.afficher(jeu)
    ennemi_module.afficher(jeu)
    
    scores(jeu)

def clavier(jeu):
    # Mouvement du joueur
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50: # Pour que le joueur ne dépasse pas la fenêtre
        jeu["joueur"]["x"] += 10
    if keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
    # Tir de projectiles par le joueur
    if keyCode == UP or key == " ":
        joueur_module.nouveau_projectile(jeu)
