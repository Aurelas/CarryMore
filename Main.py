from RiotApi import RiotAPI
from Gamestate import Gamestate
from QLearningAgent import QLearningAgent
import json
import operator
import random
from MDP import mdp
##################
# I think we are gonna try Q-learning with this
#################
def main():

    #API stuff
    possible_picks = [1,2,3,4,5,6,7,7,9,10]
    api = RiotAPI('RGAPI-91670249-d254-49f7-9036-cbb60b5bc523')
    champs = 10

    stats = {'a': 100, 'b': 100, 'c':50}

    print max(stats.iteritems(), key=operator.itemgetter(1))[0], "/////"


    #Agent Stuff

    state = Gamestate()

    Agent = QLearningAgent()
    Agent.qValues[(1,2)] = 3


    Agent2 = QLearningAgent()
    Agent2.qValues[(1, 2)] = 8

    state._ai.append(Agent)
    state._ai.append(Agent2)

    state.set_state(1)
    ai = state.get_ai_from_state(state.get_state())
    print ai.getQValue(1,2), "!!"



    #Gamestate stuff
    state = Gamestate()

    while state.is_end_state() is False:
        state.update_champions(random.randint(1,20000), state._state_num)
        state.set_state(state._state_num + 1)


    print state._team1_champions_picked
    print state._team2_champions_picked
    print state._team2_champions_picked[0]

    print state.get_champion_from_state(2)




    summoner_response = api.get_summoner_by_name('KmancXC')

    # Parse the output
    temp = json.dumps(summoner_response)
    temp = json.loads(temp)
    print temp
    summoner_id = (temp['kmancxc']['id'])
    summoner_name = (temp['kmancxc']['name'])

    mastery_response = api.get_top_mastery_data(summoner_id, champs)
    print mastery_response
    id = mastery_response[0]['championId']
    print api.get_champion_role(summoner_id,[id]), "!!"

    print id


if __name__ == '__main__':
    main()