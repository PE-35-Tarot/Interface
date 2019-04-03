# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:31:52 2018

@author: PE_102
"""
from player import *
from Trump import Trump
from Card import Card
from Excuse import Excuse


class Human(Player):
    def __init__(self, score, name):
        Player.__init__(self, score, name)
        
    def card_is_played(self,b):
        pass
        
    #Redéfinir la méthode, remplacer les print par des actions visuelles
    def play(self, trick, played_listener):

        playable_cards=Player.playable_cards(self, trick)
        
        '''Gérer ces cartes jouables : les illuminer ou griser les autres
        Dans la boucle ci dessous, on attend le choix du joueur 
        (terminer la boucle en cliquant sur la carte)'''

        self.get_hand().get_cards().remove(playable_cards[card]) #WTF la classe cards a pas de methode remove, elle est dans hand
        return (playable_cards[card])
    
'''    def bid(self,dog):
        listeBid = ["Passe","Petite","Garde","Garde sans","Garde contre"] 
        while True:
            print(listeBid)
            print("\nVoici vous cartes : ")
            print(self.get_hand())
            choice = input("\nVotre choix de Prise? (Ecrire en lettre)")
            for i in range(len(listeBid)):
                if choice == listeBid[i]:
                    if choice == "Garde": #Le joueuur à choisi Garde
                        still_choosing =True#Il lui est donc proposé d'échanger ses cartes avec le chien(dog)
                        print("\nVous avez choisi Garde")
                        print("\nVous Pouvez échanger vos cartes avec celles qui sont dans le chien")
                        print("\Tapez 69 lorsque vous avez terminé")
                        while still_choosing:  
                             player_cards=Player.get_hand(self)
                             print("\nVos cartes : \n")
                             for i, el in enumerate(player_cards):
                                 print(str(i)+"-->"+str(el))
                             print("\nLes cartes du chien")
                             for i,el in enumerate(dog):
                                 print(str(i)+"-->"+str(el))
                             n1 = input("Le numero de la carte à mettre dans le chien")
                             n2 = input("Le numero de la carte à mettre dans votre jeu")
                            
                             print("\n-----------------------------------------------------------\n")
                             if type(n1)!=int or type(n2) != int or n1 == 69 or n2 == 69:
                                 still_choosing = False
                                 break
                             elif n1 < 19 and n2<6 : 
                                 hand = self.get_hand()
                                 
                                 card1 = hand.pop(n1)
                                 card2 = dog.pop(n2)
                                 dog.append(card1)
                                 hand.append(card2)
                                 self.set_hand(hand)
                             else:
                                 print("Veuillez renseigner un numero valide")
                    if choice == "Petite": #Le joueuur à choisi Petite, meme si tout recpoer n'est pas le plus optimisé
                        still_choosing =True#Il lui est donc proposé d'échanger ses cartes avec le chien(dog)
                        print("\nVous avez choisi Petite")#bite
                        print("\nVous Pouvez échanger vos cartes avec celles qui sont dans le chien")
                        print("\Tapez 69 lorsque vous avez terminé")
                        while still_choosing:  
                             player_cards=Player.get_hand(self)
                             print("\nVos cartes : \n")
                             for i, el in enumerate(player_cards):
                                 print(str(i)+"-->"+str(el))
                             print("\nLes cartes du chien")
                             for i,el in enumerate(dog):
                                 print(str(i)+"-->"+str(el))
                             n1 = input("Le numero de la carte à mettre dans le chien")
                             n2 = input("Le numero de la carte à mettre dans votre jeu")
                             try:
                                 n1 = int(n1)
                                 n2 = int(n2)
                                 print("\n-----------------------------------------------------------\n")
                                 if n1 == 69 or n2 == 69:
                                     still_choosing = False
                                     break
                                 elif n1 < 19 and n2<6 : 
                                     hand = self.get_hand()#Echange de cartes
                                     
                                     card1 = hand.pop(n1)
                                     card2 = dog.pop(n2)
                                     dog.append(card1)
                                     hand.append(card2)
                                     self.set_hand(hand)
                                 else:
                                     print("Veuillez renseigner un numero valide")
                             except:
                                 print("Veuillez renseigner un numero valide")

                                     
                            
                            
                        
                        
                
                    return choice
            print("\nArgument non valide")'''


#if __name__ == '__main__':
#    L=[Card(10, 'H'), Card(11, 'H'), Card(14, 'H'), Card(3, 'C'), Card(3, 'D'), Card(13,'S')]
#    joueur1=Human(L,0,"Jean")
