# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:07:02 2021

@author: nicol
"""

#importing libraries
from Player import Players
from Game import Game


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
            #asking
            
            """i=0
            while i<len(player):
                print(player[i].name,player[i].cards, game[i].coins)
                i+=1"""
              
            print("\nActions= income, foreign aid, coup, taxes, murder, extorsion, change")
            action=input("What action are you going to performe: ")
            other_players=[]
            for value in player:
                if value.name != player[player_turn-1].name:
                    other_players.append(value.name)
                    
            if action!="change":
                result=game[player_turn-1].Actions(action, other_players)
            else:
                result=game[player_turn-1].Actions(action, game[player_turn-1].cards)
                
           
            while result == "not valid":
                print("Actions= income, foreign aid, coup, taxes, murder, extorsion, change")
                action=input("You must give a valid action: ")
        
                if action!="change":
                     result=game[player_turn-1].Actions(action, other_players)
                else:
                    result=game[player_turn-1].Actions(action, game[player_turn-1].cards)
                
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