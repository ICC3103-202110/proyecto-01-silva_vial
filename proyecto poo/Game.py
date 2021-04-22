# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:17:51 2021

@author: nicol
"""
import random

class Game:
    def __init__(self,coins, cards, maze):
        self.coins=coins
        self.cards=cards
        self.maze=maze
        
    def Starting_money(self):
        Bag_of_coins= self.coins
        return Bag_of_coins 
    
    def Actions(self,action, array):
        validator=0
        while validator ==0:
            if action== "income":
                self.coins+=1
                return self.coins
    
            elif action == "foreign aid":
                self.coins+=2
                return self.coins
    
            elif action== "coup" :
                if self.coins>=7:
                    self.coins-=7
                    print(array)
                    couped_player=input("Which player do you want to copue: ")
                    while couped_player not in array:
                        print(array)
                        couped_player=input("You must give a valid player: ")
                    return couped_player
                else:
                    print("You don´t have enough coins to make that action\n")
                    return "not valid"
               
    
            elif action== 'taxes':
                self.coins+=3
                return self.coins
            
            elif action== "murder":
                if self.coins >=3:
                    self.coins-=3
                    print(array)
                    murdered_player=input("Which player do you want to kill: ")
                    while murdered_player not in array:
                        print(array)
                        murdered_player=input("You must give a valid player: ")
                    return murdered_player
                else:
                    print("You don´t have enough coins to make that action\n")
                    return "not valid"
    
            elif action == "extorsion":
               print(array)
               stealed_player=input("Which player do you want to steal from: ")
               while stealed_player not in array:
                   print(array)
                   stealed_player=input("You must give a valid player: ")
               return stealed_player
               
            elif action== "change":
                 if len(array)>1:
                     candidates=[]
                     random.shuffle(self.maze)
                     counter=0
                     while counter<len(array):
                        candidates.append(self.maze[0])
                        self.maze.pop(0)
                        counter+=1
                     print("\nThe candidates cards are: "+str(candidates))
                     print("Your cards are: "+str(array))
                     option1=array
                     option2=candidates
                     option3=[array[0],candidates[0]]
                     option4=[array[0],candidates[1]]
                     option5=[array[1],candidates[0]]
                     option6=[array[1],candidates[1]]
                     
                     options=[option1,option2,option3,option4,option5,option6] 
                     print("\nYour options are:")
                     counter=1
                     while counter<=len(options):
                         print(str(options[counter-1])+" ---> ",str(counter))
                         counter+=1
                    
                     answer=input("Please choose your combination: ")
                     while answer!="1" and answer!="2" and answer!="3" and answer!="4" and answer!="5" and answer!="6":
                       answer=input("You must give a valid answer: ")  
                       
                     if int(answer)==1:
                         return option1
                     if int(answer)==2:
                         return option2
                     if int(answer)==3:
                         return option3
                     if int(answer)==4:
                         return option4
                     if int(answer)==5:
                         return option5
                     if int(answer)==6:
                         return option6
                 else:
                     random.shuffle(self.maze)
                     changer= self.maze.pop(0)
                     option1=[changer]
                     option2=[array]
                     options=[option1,option2]
                     print("\nYour options are:")
                     number=1
                     for value in options:
                         print(str(value)+" ---> "+str(number))
                         number+=1
                    
                     answer=input("Please choose your combination: ")
                     while answer!="1" and answer!="2":
                       answer=input("You must give a valid answer: ")  
                     if int(answer)==1:
                         return option1
                     if int(answer)==2:
                         return option2
                 
                
                    
        
            else:
                return "not valid"
                
    def Steal_actions(self, bag_of_coins):#steals coins from other players
            if bag_of_coins>=2:
                
                return bag_of_coins-2
            else:
                if bag_of_coins==0:
                    print("This player has no coins left")
                    return bag_of_coins
                else:
                    return bag_of_coins-1
    
    def Influence(self, action):
        
        if action=="tax":
            return "duke"
        
        elif action=="murder":
            return "assasin"
        
        elif action=="extorsion":
            return "captain"
        
        elif action=="change":
            return "ambassador"
        else:
            pass
        
    def CounterInfluence(self,action):
        if action=="foreign aid":
            return "duke"
        
        if action=="murder":
            return "countess"
        
        if action=="extorsion":
            return "captain"
        
    def Solution(self, looser, array):
        print(array)
        card_to_turn=input(looser+", you have lost, which card do you want to turn: ")
        while card_to_turn not in array:
            card_to_turn=input("You must give a card from your maze: ")
        return card_to_turn
    
    def Refresh(self, card):
        random.shuffle(self.maze)
        new_card=self.maze.pop(0)
        self.maze.append(card)
        return new_card
    
        
            
            
      
    
       
          