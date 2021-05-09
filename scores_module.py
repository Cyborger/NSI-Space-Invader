# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

if False:
    from lib.Processing3 import *


def afficher(jeu):
    # Arrière-plan
    fill(0)
    rect(0, 0, width, 25)

    # Vies restantes
    fill(*jeu["couleurs"][jeu["sauvegarde"]["couleur"]])
    textSize(20)
    textAlign(LEFT)
    text("VIES:", width - 145, 20)

    for i in range(jeu["joueur"]["vies"]):
        image(jeu["images"][jeu["sauvegarde"]["couleur"]]["joueur"], width - 65 + 25 * i, 12, 20, 20)

    if "score" not in jeu:  # Initialise la variable score
        jeu["score"] = 0

    # Scores
    text("SCORE: " + str(jeu["score"]), 5, 20)
    textAlign(CENTER)
    text("RECORD: " + str(jeu["sauvegarde"]["record"]), width // 2, 20)
