# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
    
def scores(jeu):
    pass

def joueur(jeu):
    if "joueur" not in jeu:
        jeu["joueur"] = {
            "x": width // 2,
            "y": height - 80,
            "est_vivant": True
        }
    
    imageMode(CENTER)
    image(jeu["images"]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"])

def afficher(jeu):
    background(0)
    
    joueur(jeu)
    scores(jeu)

def clavier(jeu):
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50:
        jeu["joueur"]["x"] += 10
    elif keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
