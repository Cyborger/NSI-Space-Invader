# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

if False:
    from lib.Processing3 import *


def nouveau_projectile(jeu):
    """Crée un nouveau projectile au niveau du joueur et l'ajoute dans la liste des projectiles dans la variable
    paramètre jeu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if not frameCount > jeu["joueur"]["frame_projectile"] + 30:
        return

    jeu["joueur"]["frame_projectile"] = frameCount
    jeu["projectiles"].append({  # Voir "Propriétés des entités" space_invader.pyde
        "x": jeu["joueur"]["x"],
        "y": jeu["joueur"]["y"] - jeu["joueur"]["largeur"] // 2,
        "longueur": 5,
        "largeur": 5,
        "orientation": -1,
        "vitesse": jeu["sauvegarde"]["vitesse"]
    })


def afficher(jeu):
    """Affiche le joueur selon les propriétés disponibles dans la variable jeu. Initialise celles-ci le cas échéant.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "joueur" not in jeu:
        jeu["joueur"] = {
            "x": width // 2,
            "y": height - 80,
            "longueur": 80,
            "largeur": 80,
            "vies": jeu["sauvegarde"]["vies"],
            "frame_projectile": 0,
            "est_vivant": True
        }

    if jeu["joueur"]["est_vivant"] or (not jeu["joueur"]["est_vivant"] and frameCount // 15 % 2 == 0):
        image(jeu["images"][jeu["sauvegarde"]["couleur"]]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"],
              jeu["joueur"]["longueur"], jeu["joueur"]["largeur"])
