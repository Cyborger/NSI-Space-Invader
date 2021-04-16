# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

def nouveau_projectile(jeu):
    jeu["joueur"]["projectiles"].append({
        "x": jeu["joueur"]["x"],
        "y": jeu["joueur"]["y"] - jeu["joueur"]["largeur"] // 2,
        "longueur": 5,
        "largeur": 5
    })


def projectiles(jeu):
    if "projectiles" not in jeu["joueur"]:
        jeu["joueur"]["projectiles"] = []
    
    for projectile in jeu["joueur"]["projectiles"][:]: # Utilisation du slice afin d'itérer sur une copie de la liste jeu["projectiles"] et de pouvoir supprimer les éléments de la liste originelle
        projectile["y"] -= 5
        
        image(jeu["images"]["projectile"], projectile["x"], projectile["y"], projectile["longueur"], projectile["largeur"])
        
        if projectile["y"] < 0: # Suppression des projectiles non affichés
            jeu["joueur"]["projectiles"].remove(projectile)

def afficher(jeu):
    if "joueur" not in jeu:
        jeu["joueur"] = {
            "x": width // 2,
            "y": height - 80,
            "longueur": 80,
            "largeur": 80,
            "est_vivant": True
        }
    
    image(jeu["images"]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"], jeu["joueur"]["longueur"], jeu["joueur"]["largeur"])
    projectiles(jeu)
