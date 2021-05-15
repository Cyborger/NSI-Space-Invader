# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import ennemi_module


def projectiles(jeu):
    """Met à jour chacun des projectiles disponibles selon leurs propriétés disponibles dans la variable jeu.
    Initialise une liste pour les contenir le cas échéant.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "projectiles" not in jeu:  # Initialisation de la liste des projectiles
        jeu["projectiles"] = []

    for projectile in jeu["projectiles"][:]:  # Itère sur copie de jeu["projectiles"] afin de supprimer ses éléments
        projectile["y"] += -5 * projectile["vitesse"]  # Mouvement projectile

        image(jeu["images"][jeu["sauvegarde"]["couleur"]]["projectile"], projectile["x"], projectile["y"],
              projectile["longueur"], projectile["largeur"])

        if projectile["y"] < 0:  # Suppression projectiles non affichés par soucis de performances
            jeu["projectiles"].remove(projectile)

        collision = ennemi_module.collision(projectile, jeu)
        if collision:
            jeu["projectiles"].remove(projectile)
            jeu["score"] += 10
            collision["frame_mort"] = frameCount  # Permet le fonctionnement de l'animation de l'entité touché
            collision["est_vivant"] = False


def nouveau_projectile(jeu):
    """Crée un nouveau projectile au niveau du joueur et l'ajoute dans la liste des projectiles dans la variable
    paramètre jeu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if not frameCount > jeu["joueur"]["frame_projectile"] + 30:
        return

    jeu["joueur"]["frame_projectile"] = frameCount
    jeu["projectiles"].append({  # Initialisation d'un projectile
        "x": jeu["joueur"]["x"],
        "y": jeu["joueur"]["y"] - jeu["joueur"]["largeur"] // 2,
        "longueur": 5,
        "largeur": 5,
        "vitesse": jeu["sauvegarde"]["vitesse"]
    })


def afficher(jeu):
    """Affiche le joueur selon les propriétés disponibles dans la variable jeu. Initialise celles-ci le cas échéant.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "joueur" not in jeu:  # Initialisation du joueur
        jeu["joueur"] = {
            "x": width // 2,
            "y": height - 80,
            "longueur": 80,
            "largeur": 80,
            "vies": jeu["sauvegarde"]["vies"],
            "frame_projectile": 0,
            "est_vivant": True
        }

    # Affichage du joueur (en vie ou intervalle périodique de 2 secondes si non vivant pour l'animation)
    if jeu["joueur"]["est_vivant"] or (not jeu["joueur"]["est_vivant"] and frameCount // 15 % 2 == 0):
        image(jeu["images"][jeu["sauvegarde"]["couleur"]]["joueur"], jeu["joueur"]["x"], jeu["joueur"]["y"],
              jeu["joueur"]["longueur"], jeu["joueur"]["largeur"])
