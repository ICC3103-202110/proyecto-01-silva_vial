# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:03:22 2021

@author: nicol
"""

import random

class Players:
    def __init__(self,name,cards=2):
        self.name=name
        self.cards= cards


    def Player_cards(self):
        Player_deck=[]
        random.shuffle(Deck)
        for value in range(self.cards):
            Player_deck.append(Deck[0])
            Deck.pop(0)
        return Player_deck
    
    def Return_deck(self):
        return Deck

    

           
Deck=['duke','duke','duke','assasin','assasin','assasin','captain','captain',
'captain','ambassador','ambassador','ambassador','countess','countess',
'countess']

