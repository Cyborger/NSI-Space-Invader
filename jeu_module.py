# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
    
def scores(jeu):
    pass

def nouveau_projectile(jeu):    
    jeu["projectiles"].append({
        "x": jeu["joueur"]["x"],
        "y": jeu["joueur"]["y"] - 45
    })

def joueur(jeu):
    if "joueur" not in jeu:
        jeu["joueur"] = {
            "x": width // 2,
            "y": height - 80,
            "est_vivant": True
        }
    
    image(jeu["images"]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"])

def projectiles(jeu):
    if "projectiles" not in jeu:
        jeu["projectiles"] = []
    
    for projectile in jeu["projectiles"][:]: # Utilisation du slice afin d'itérer sur une copie de la liste jeu["projectiles"] et de pouvoir supprimer les éléments de la liste originelle
        projectile["y"] -= 5
        
        image(jeu["images"]["projectile"], projectile["x"], projectile["y"], 5, 5)
        
        if projectile["y"] < 0: # Suppression des projectiles non affichés
            jeu["projectiles"].remove(projectile)
            
def afficher(jeu):
    background(0)
    imageMode(CENTER)
    
    joueur(jeu)
    projectiles(jeu)
    scores(jeu)

def clavier(jeu):
    # Mouvement du joueur
    if keyCode == RIGHT and jeu["joueur"]["x"] < width - 50: # Pour que le joueur ne dépasse pas la fenêtre
        jeu["joueur"]["x"] += 10
    if keyCode == LEFT and jeu["joueur"]["x"] > 50:
        jeu["joueur"]["x"] -= 10
    # Tir de projectiles
    if keyCode == UP or key == " ":
        nouveau_projectile(jeu)
        
