#!/usr/bin/env python3.7


class Responses:
    """
    Agent Responses
    """

    ANGRY = ["Stay back!!!", "I will kill the hostage, I swear!", "Back off, now!!", "Do you think this is a game???"]

    IRRITATED = ["Where are my demands?!", "What?!", "How about you start making sense?", "I am losing my patience!"]

    CALM = ["Ok.", "It's useless.", "You give me what I want, everyone walks away.", "Fine."]

    SUBMISSIVE = ["I want to go home.", "You promise not to hurt me?", "I don't really want to do this.", "I'm sorry."]

    SUCCESS = ["You win...", "Don't shoot! I'm coming out!", "I am laying down my weapons.", "I give up!"]

    FAILURE = ["You should've gone for the head.", "This is on you!!!", "*silence*"]

    MOODS = {0: ANGRY, 1: IRRITATED, 2: CALM, 3: SUBMISSIVE, 4: SUCCESS}
