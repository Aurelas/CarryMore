from RiotApi import RiotAPI
from Gamestate import Gamestate
from QLearningAgent import QLearningAgent
import string
import json
import operator
import random


def parse_champion_name(name):
    new_name =name.translate(None,"'")
    new_name = new_name.translate(None," ")
    return new_name.lower()


def main():

    #Assuming that the user picks riven first for now
    #Updates the gamestate and everything before we run it through a loop

    ################################################################
    # THIS IS WHERE USER INPUT SHOULD GO

    User_choice = parse_champion_name("""Miss Fortune""")
    ################################################################

    # USER COULD CHOOSE NUMBER OF SIMULATIONS?
    #100000 simulations takes like 20 seconds to complete
    # 1mil simulations takes ~ 1 - 1.5mins This should be the limit
    simulations = 100000

    game = Gamestate()
    #Depending on either True / False it swaps the reward function
    User_choice_only = False
    game.roles_picked[game.champion_roles[User_choice]] = True
    game.update_champions(User_choice)
    game.set_state(game.get_next_state())


    #Creates AI for each champion type that we dont have after taking the user choice into consideration
    for i in game.roles_picked.keys():
        if not game.roles_picked[i]:
            if i == 'ADC':
               game.ai.append(QLearningAgent(game.adc_champs))
            if i == 'Support':
                game.ai.append(QLearningAgent(game.support_champs))
            if i == 'Mid':
                game.ai.append(QLearningAgent(game.mid_champs))
            if i == 'Top':
                game.ai.append(QLearningAgent(game.top_champs))
            if i == 'Jungle':
                game.ai.append(QLearningAgent(game.jungle_champs))

    #THE SIMULATOR
    for i in range(0,simulations):
        #Based on how many iterations are left in the simulation we make our ai choose less randomly
        #if i <= simulations/3:
            #for j in game.ai:
                #j.epsilon = .1
        #if i >= simulations/3 and i <= simulations/1.2:
            #for j in game.ai:
                #j.epsilon = .4
        #if i >= simulations/1.2:
            #for j in game.ai:
                #j.epsilon = .7

        #For each simulation load up the champion list with picks
        for i in game.ai:
            game.update_champions(i.chooseChampion(game))
            game.set_state(game.get_next_state())

        j = 2
        for i in game.ai:
            #Only considers the User_choice synergies in reward function
            if User_choice_only:
                i.updateQValue(game,game.get_champion_from_state(j),
                               i.altGetReward(game.get_champion_from_state(j),game))
            #Considers all champions on the team for reward
            else:
                i.updateQValue(game, game.get_champion_from_state(j),
                               i.getReward(game.get_champion_from_state(j), game))
            j += 1

        #Reset counters to keep track of game state
        game.reset_champions_picked(User_choice)
        if game.is_end_state():
            game.set_state(1)

    ################################################################
    # THIS OUTPUTS THE TOP 5 CHOICES FOR EACH AI (ROLE)
    ################################################################
    for i in game.ai:
        t = sorted(i.qValues.iteritems(), key=lambda x: -x[1])[:5]
        for x , y in t:
            print game.get_role_from_champion(x),":", x,":", y





if __name__ == '__main__':
    main()

