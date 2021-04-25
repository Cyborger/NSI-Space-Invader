# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

if False:
    from lib.Processing3 import *


def nouveau_projectile(jeu):
    """Crée un nouveau projectile au niveau du joueur et l'ajoute dans la liste des projectiles dans la variable
    paramètre jeu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    jeu["projectiles"].append({  # Voir "Propriétés des entités" space_invader.pyde
        "x": jeu["joueur"]["x"],
        "y": jeu["joueur"]["y"] - jeu["joueur"]["largeur"] // 2,
        "longueur": 5,
        "largeur": 5,
        "orientation": -1,
        "vitesse": 1
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
            "vies": 3,
            "est_vivant": True
        }

    image(jeu["images"]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"], jeu["joueur"]["longueur"],
          jeu["joueur"]["largeur"])

    # TODO Animation de mort du joueur
