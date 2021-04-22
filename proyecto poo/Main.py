# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:07:02 2021

@author: nicol
"""

#importing clases
from Player import Players
from Game import Game

#importing libraries
import random

def main():
    
    #asking main parameters
    print("\n#### WELCOME TO COUPE ####")
    n_players=input("Please insert the number of players 3-4: ")
    
    while n_players !="3" :
        if n_players !="4":
            n_players=input("Yoy must give a valid number: ")
        else:
            break    
    n_players=int(n_players)
    
    player=[]
    game=[]
    count=0
    while count<n_players:
        game.append(Game(2,[],[]))
        name=input("Please insert the "+str(count+1)+" name in the clockwise direction: ")
        player.append(Players(name))
        count+=1

  
    
    #gaming
    kill=0 #if this is 1, the game is over
    play=1
    player_turn=1
    
    turned_cards=[] #cards that have been turned
    breaker=0
    while breaker<n_players:
        turned_cards.append(["X","X"])
        breaker+=1
   
    
    #setting cards and mazes
    counter=0
    while counter<len(player):
        game[counter].cards=player[0].Player_cards()
        counter+=1
    for value in game:
        value.maze=player[game.index(value)].Return_deck()
        
   
    
    while kill!=1:
        if player_turn==n_players+1:
            player_turn=1
        if player[player_turn-1].cards>0:    
        
            print("\n|__-< COUPE >-__|\n")
            print("\nPlay N° ",play)
            print(str(player[player_turn-1].name)+" is playing")
            
             #turned cards
            print("\nThe turned cards of players are: ")
            countdown=0
            while countdown <len(player):
                print(player[countdown].name+str(": ")+str(turned_cards[countdown])+" - Coins: ", game[countdown].coins)
                countdown+=1
            
            
            Card_watcher=input('\nWould you like to see your cards (yes/no): ')
            while Card_watcher!= "yes" and Card_watcher!="no":
                Card_watcher=input('\nYou must give a valid answer to see your cards(yes/no): ')
            if Card_watcher == "yes":
                print('Your cards are '+str(game[player_turn-1].cards)) 
                
            other_players=[]
            for value in player:
                if value.name != player[player_turn-1].name:
                    if value.cards>0:
                        other_players.append(value.name)
    
            #automatic coup
            legality=1
            if game[player_turn-1].coins>=10:
                print('You have to performe coup')
                action="coup"
                    
            else:
                #asking actions to the playing player
                print("\nActions= income, foreign aid, coup, taxes, murder, extorsion, change")
                action=input("What action are you going to performe: ")
                while action!="income" and action!="foreign aid" and action!="coup" and action!="taxes" and action!="murder" and action!="extorsion" and action!="change":
                    print("Actions= income, foreign aid, coup, taxes, murder, extorsion, change")
                    action=input("You must give a valid action: ")
            
                
                #counterattack and challenges
                if action=="foreign aid" or action=="murder" or action=="extorsion" or action=="change":
                    counterattacks=[]
                    challenges=[]
                    for value in other_players:
                        answer=input(value+", you can: challenge, counterattack or pass: ")
                        while answer != "challenge" and answer!= "counterattack" and answer!="pass":
                            print("you can: challenge, counterattack or pass: ")
                            answer=input(value+ ", you must give a valid input: ")
                        print("")
                        if answer=="challenge":
                            challenges.append(value)
                        elif answer=="counterattack":
                            counterattacks.append(value)
                    
                    
                    if len(counterattacks)>1:
                        index1=random.randint(0,len(counterattacks)-1)
                        counterattacker=counterattacks[index1]
                    elif len(counterattacks)==1:
                        counterattacker=counterattacks[0]
                    else:
                        counterattacker=0 #no counterattacker
                    
                        
                  
                    if len(challenges)>1:
                        index2=random.randint(0,len(challenges)-1)
                        challenger=challenges[index2]
                    elif len(challenges)==1:
                        challenger=challenges[0]
                    else:
                        challenger=0 #no challenger
                    
                    if  len(counterattacks)>1:
                       print("The final counterattacker is "+counterattacker)
                    if  len(challenges)>1:
                       print("The final challenger is "+challenger)
                    
                
                    #challenging
                    if challenger!=0:
                        #useful parameters
                        action_influence=game[player_turn-1].Influence(action)
                        player_name=player[player_turn-1].name
                        player_cards=game[player_turn-1].cards
                        challenger_cards=[]
                        value=0
                        while value <len(player):
                            if player[value].name==challenger:
                                for element in game[value].cards:
                                    challenger_cards.append(element)
                                challenger_name=player[value].name
                            value+=1
                        
                        
                        #challenge
                        print(player_name+", you have been challenged by "+challenger_name)
                        if action_influence not in player_cards:
                                card_to_turn=game[player_turn-1].Solution(player_name,player_cards)
                                
                                #player looses card
                                player[player_turn-1].cards-=1
                                turned_cards[player_turn-1].append(card_to_turn)
                                turned_cards[player_turn-1].pop(0)
                                for value in game:
                                    if card_to_turn in value.cards:
                                        index=value.cards.index(card_to_turn)
                                        value.cards.pop(index)
                                legality=0
                                
                        else:
                                card_to_turn=game[player_turn-1].Solution(challenger_name,challenger_cards)
                                
                                #challenger looses card
                                counter_index=0
                                for value in player:
                                    if value.name==challenger_name:
                                        value.cards-=1
                                        challenger_index=counter_index
                                    counter_index+=1
                                    
                                turned_cards[challenger_index].append(card_to_turn)
                                turned_cards[challenger_index].pop(0)
                                for value in game:
                                    if card_to_turn in value.cards:
                                        index=value.cards.index(card_to_turn)
                                        value.cards.pop(index)
                                        
                                #player changes his card
                                new=game[player_turn-1].Refresh(action_influence)
                                index_to_change=game[player_turn-1].cards.index(action_influence)
                               
                                game[player_turn-1].cards.pop(index_to_change)
                                game[player_turn-1].cards.append(new)
                                
                                        
                    #counter attacks                        
                    elif counterattacker!=0:
                        if action=="foreign aid" or action=="murder" or action=="extorsion":
                    
                            
                            #useful parameters
                            action_influence=game[player_turn-1].Influence(action)
                            counteraction_influence=game[player_turn-1].CounterInfluence(action)
                            player_name=player[player_turn-1].name
                            player_cards=game[player_turn-1].cards
                            counterattacker_cards=[]
                            value=0
                            while value <len(player):
                                if player[value].name==counterattacker:
                                    for element in game[value].cards:
                                        counterattacker_cards.append(element)
                                    counterattacker_name=player[value].name
                                value+=1
                            
                         
                            
                            #counterattack
                            print(player_name+", you have been counterattacked by "+counterattacker_name)
                            defense=input("Would you like to challenge him (yes/no): ")
                            while defense !="yes" and defense !="no":
                                 defense=input("You must give a valid input (yes/no): ")
                                 
                            #player accepts the counterattacl     
                            if defense=="no":
                                if action_influence not in player_cards:
                                    card_to_turn=game[player_turn-1].Solution(player_name,player_cards)
                                    
                                    #player looses card
                                    player[player_turn-1].cards-=1
                                    turned_cards[player_turn-1].append(card_to_turn)
                                    turned_cards[player_turn-1].pop(0)
                                    for value in game:
                                        if card_to_turn in value.cards:
                                            index=value.cards.index(card_to_turn)
                                            value.cards.pop(index)
                                    legality=0
                                    if action=="murder":
                                        game[player_turn-1].coins-=3
                                
                                    
                                else:
                                    card_to_turn=game[player_turn-1].Solution(counterattacker_name,counterattacker_cards)
                                    
                                    #counterattacker looses card
                                    counter_index=0
                                    for value in player:
                                        if value.name==counterattacker_name:
                                            value.cards-=1
                                            challenger_index=counter_index
                                        counter_index+=1
                                        
                                    
                                        
                                    turned_cards[challenger_index].append(card_to_turn)
                                    turned_cards[challenger_index].pop(0)
                                    for value in game:
                                        if card_to_turn in value.cards:
                                            index=value.cards.index(card_to_turn)
                                            value.cards.pop(index)
                                        
                                    #player changes his card
                                    new=game[player_turn-1].Refresh(action_influence)
                                    index_to_change=game[player_turn-1].cards.index(action_influence)
                                   
                                    game[player_turn-1].cards.pop(index_to_change)
                                    game[player_turn-1].cards.append(new)
                                    
                                    
                                    
                                    
                                    
                             
                            #player challenges counterattack    
                            else:
                                print(counterattacker_name+", you have been counter challenged by " +player_name)
                                if  counteraction_influence not in counterattacker_cards:
                                    card_to_turn=game[player_turn-1].Solution(counterattacker_name,counterattacker_cards)
                                    
                                    #counterattacker looses card
                                    counter_index=0
                                    for value in player:
                                        if value.name==counterattacker_name:
                                            value.cards-=1
                                            challenger_index=counter_index
                                        counter_index+=1
                                        
                                    
                                        
                                    turned_cards[challenger_index].append(card_to_turn)
                                    turned_cards[challenger_index].pop(0)
                                    for value in game:
                                        if card_to_turn in value.cards:
                                            index=value.cards.index(card_to_turn)
                                            value.cards.pop(index)
                                            
                                            
                                    #player changes his card
                                    new=game[player_turn-1].Refresh(action_influence)
                                    index_to_change=game[player_turn-1].cards.index(action_influence)
                                   
                                    game[player_turn-1].cards.pop(index_to_change)
                                    game[player_turn-1].cards.append(new)
                                    
                                    
                                else:
                                    card_to_turn=game[player_turn-1].Solution(player_name,player_cards)
                                    
                                   
                        
                                    #player looses card
                                    player[player_turn-1].cards-=1
                                    turned_cards[player_turn-1].append(card_to_turn)
                                    turned_cards[player_turn-1].pop(0)
                                    for value in game:
                                        if card_to_turn in value.cards:
                                            index=value.cards.index(card_to_turn)
                                            value.cards.pop(index)
                                    legality=0
                                    if action=="murder":
                                        game[player_turn-1].coins-=3
                   
                    
                        
                                    
                            
                            
                            
                            
            
            if legality==1:
                #analazing actions
                if action!="change":
                    result=game[player_turn-1].Actions(action, other_players)
                else:
                    result=game[player_turn-1].Actions(action, game[player_turn-1].cards)
                while result=="not valid":
                    print("\nActions= income, foreign aid, coup, taxes, murder, extorsion, change")
                    action=input("You must perform a valid action: ")
                    if action!="change":
                        result=game[player_turn-1].Actions(action, other_players)
                    else:
                        result=game[player_turn-1].Actions(action, game[player_turn-1].cards)
                        
                #execution of actions
                if action=="murder":
                   for value in player:
                       if value.name== result:
                           index=player.index(value)
                           cards_to_kill=game[index].cards
                           print(cards_to_kill)
                   killed_card=input(str(result)+" please choose the card you want to turn over: ")
                   while killed_card not in cards_to_kill:
                        print(cards_to_kill)
                        killed_card=input("Please turn a valid card from your maze: ")
                
                   turned_cards[index].append(killed_card)
                   turned_cards[index].pop(0)
                   for value in game:
                       if killed_card in value.cards:
                           index=value.cards.index(killed_card)
                           value.cards.pop(index)
                                    
                   for value in player:
                        if value.name== result:
                            value.cards-=1
                
                if action=="coup":
                       for value in player:
                           if value.name== result:
                               index=player.index(value)
                               cards_to_coup=game[index].cards
                               print(cards_to_coup)
                       couped_card=input(str(result)+" please choose the card you want to coup: ")
                       while couped_card not in cards_to_coup:
                        print(cards_to_coup)
                        couped_card=input("Please turn a valid card from your maze: ")
                        
                       turned_cards[index].append(couped_card)
                       turned_cards[index].pop(0)
                       for value in game:
                           if couped_card in value.cards:
                               index=value.cards.index(couped_card)
                               value.cards.pop(index)
                           
                       for value in player:
                            if value.name== result:
                                value.cards-=1
                 
                if action=="extorsion":
                    counter=0
                    while counter <len(player):
                        if player[counter].name==result:
                            if game[counter].coins>=2:
                                game[player_turn-1].coins=game[player_turn-1].coins+2
                            elif game[counter].coins<2:
                                    game[player_turn-1].coins=game[player_turn-1].coins+1
                            else:
                                pass
                                
                            game[counter].coins=game[player_turn-1].Steal_actions(game[counter].coins)
                        counter+=1
                        
                if action=="change":
                    game[player_turn-1].cards=result
            
                    
            
            
                    
           
                        
       
        
        
        play+=1
        player_turn+=1
        #analizing all the posible ending scenarios
        if n_players==3:
            ending1=player[0].cards==0 and player[1].cards==0
            ending2=player[1].cards==0 and player[2].cards==0
            ending3=player[0].cards==0 and player[2].cards==0
        elif n_players==4:
            ending1=player[0].cards==0 and player[1].cards==0 and player[2].cards==0
            ending2=player[1].cards==0 and player[2].cards==0 and player[3].cards==0
            ending3=player[2].cards==0 and player[3].cards==0 and player[0].cards==0
            ending4=player[3].cards==0 and player[0].cards==0 and player[1].cards==0
        
        #killing cycle
        if n_players ==3:
            
            if ending1==True:
                kill=1
                winer=player[2].name
            elif ending2==True:
                kill=1
                winer=player[0].name
            elif ending3==True:
                kill=1
                winer=player[1].name
                
        elif n_players ==4:
            
            if ending1==True:
                kill=1
                winer=player[3].name
            elif ending2==True:
                kill=1
                winer=player[0].name
            elif ending3==True:
                kill=1
                winer=player[1].name
            elif ending4==True:
                kill=1
                winer=player[2].name
    
    
    
    
    
    
    
    
    
    
    
    
    

    print("\n  GAME OVER!!")
    print("The winer is :"+str(winer)+", congratulations!")

if __name__ == "__main__":
    main()