# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

if False:
    from lib.Processing3 import *


def afficher(jeu):
    # Arrière-plan
    fill(0)
    rect(0, 0, width, 25)

    # Vies restantes
    fill(*jeu["couleurs"]["terminal"])
    textSize(20)
    textAlign(LEFT)
    text("VIES:", width - 145, 20)

    for i in range(jeu["joueur"]["vies"]):
        image(jeu["images"]["joueur"], width - 65 + 25 * i, 12, 20, 20)

    # Scores
    text("SCORE: " + str(jeu["scores"]["actuel"]), 5, 20)
    textAlign(CENTER)
    text("RECORD: " + str(jeu["scores"]["record"]), width // 2, 20)
