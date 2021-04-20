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
    
    #setting cards and mazes
    counter=0
    while counter<len(player):
        game[counter].cards=player[0].Player_cards()
        counter+=1
    for value in game:
        value.maze=player[game.index(value)].Return_deck()
        
   
    
    while kill!=1:
        print("\nPlay N° ",play)
        if player_turn==n_players+1:
            player_turn=1
        print(str(player[player_turn-1].name)+" is playing")
        print("You have "+str(game[player_turn-1].coins)+ " coins")
        Card_watcher=input('\nWould you like to see your cards (yes/no): ')
        while Card_watcher!= "yes" and Card_watcher!="no":
            Card_watcher=input('\nYou must give a valid answer to see your cards(yes/no): ')
        if Card_watcher == "yes":
            print('Your cards are '+str(game[player_turn-1].cards)) 

        #automatic coup
        if game[player_turn-1].coins>=10:
            print('You have to performe coup')
            action="coup"
                
        else:
            #asking actions to the playing player
            
            """i=0
            while i<len(player):
                print(player[i].name,player[i].cards, game[i].coins)
                i+=1"""
        
            other_players=[]
            for value in player:
                if value.name != player[player_turn-1].name:
                    if value.cards>0:
                        other_players.append(value.name)
            
            print("\nActions= income, foreign aid, coup, taxes, murder, extorsion, change")
            action=input("What action are you going to performe: ")
            while action!="income" and action!="foreign aid" and action!="coup" and action!="taxes" and action!="murder" and action!="extorsion" and action!="change":
                print("Actions= income, foreign aid, coup, taxes, murder, extorsion, change")
                action=input("You must give a valid action: ")
        
            
            #counterattack and challenges
            counterattacks=[]
            challenges=[]
            for value in other_players:
                answer=input(value+", you can: challenge, counterattack or pass: ")
                while answer != "challenge" and answer!= "counterattack" and answer!="pass":
                    print("you can: challenge, counterattack or pass: ")
                    answer=input(value+ ", you must give a valid input: ")
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
                action_influence=game[player_turn-1].Influence(action)
                player_name=player[player_turn-1].name
                player_cards=[game[player_turn-1].cards[0],game[player_turn-1].cards[1]]
                challenger_cards=[]
                value=0
                while value <len(player):
                    if player[value].name==challenger:
                        challenger_cards.append(game[value].cards[0])
                        challenger_cards.append(game[value].cards[1])
                        challenger_name=player[value].name
                    value+=1
                action_influence=game[player_turn-1].Influence(action)
                counteraction_influence=game[player_turn-1].CounterInfluence(action)
                
                print(player_name+", you have been challenged by "+challenger_name)
                defense=input("Would you like to counter challenge him (yes/no): ")
                while defense !="yes" and defense !="no":
                     defense=input("You must give a valid input (yes/no): ")
                
                if defense=="no":
                    if action_influence not in player_cards:
                        card_to_turn=game[player_turn-1].Solution(player_name,player_cards)
                        
                    else:
                        card_to_turn=game[player_turn-1].Solution(challenger_name,challenger_cards)
                        
                        for value in player:
                            if value.name==challenger_name:
                                value.cards-=1
                                
                        counter=0
                        while counter <2:
                            if game[player_turn-1].cards[counter]==action_influence:
                                game[player_turn-1].cards[counter]=game[player_turn-1].Refresh(action_influence)
                            counter+=1
                                
                        
                else:
                    print(challenger_name+", you have been counter challenged by " +player_name)
                    if  counteraction_influence not in challenger_cards:
                        card_to_turn=game[player_turn-1].Solution(challenger_name,challenger_cards)
                        for value in player:
                            if value.name==challenger_name:
                                value.cards-=1
                    else:
                        card_to_turn=game[player_turn-1].Solution(player_name,player_cards)
                        player[player_turn-1].cards-=1
                        
                        counter1=0
                        while counter1 <len(game):
                            if player[counter1].name==challenger_name:
                                counter2=0
                                while counter2<2:
                                    if game[counter1].cards[counter2]==counteraction_influence:
                                        game[counter1].cards[counter2]=game[player_turn-1].Refresh(counteraction_influence)
                                    counter2+=1
                                        
                            counter1+=1
                            
                    
            #challenging
               
                
                    
                                
                        
                        
                        
                        
            
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
            
            
                    
           
                        
       
        #i=0
        #while i<len(player):
        #    print(player[i].name,player[i].cards, game[i].coins, game[i].cards,)
        #    i+=1
        
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
            elif ending2==True:
                kill=1
            elif ending3==True:
                kill=1
                
        elif n_players ==4:
            
            if ending1==True:
                kill=1
            elif ending2==True:
                kill=1
            elif ending3==True:
                kill=1
            elif ending4==True:
                kill=1
    
    
    
    
    
    
    
    
    
    
    
    
    

    

if __name__ == "__main__":
    main()