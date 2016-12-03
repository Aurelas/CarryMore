
import util,random
import operator
class QLearningAgent(object):

    def __init__(self,champion_role_list):
        self.qValues = {}
        self.epsilon = .98
        self.alpha = .5
        for i in champion_role_list:
            self.qValues[i] = 1

    def getQValue(self):
        return self.qValues

    def resetQValue(self):
        for i in self.qValues:
            self.qValues[i] = 0

    def computeActionFromQValues1(self,):

        return max(self.qValues.iteritems(), key=operator.itemgetter(1))[0]


    #getAction
    def chooseChampion(self,Gamestate):

        action = None
        choose_random = util.flipCoin(self.epsilon)

        #Champion choice
        if choose_random:
            action = random.choice(self.qValues.keys())
        else:
            action = self.getPolicy()

        return action


    def updateQValue(self,Gamestate,action, reward):

        oldValue = self.qValues[action]
        newValue = self.qValues[action] + reward

        self.qValues[action] = oldValue + self.alpha * (newValue - oldValue)


    def getPolicy(self, ):
        return self.computeActionFromQValues1()

    def getReward(self,action,Gamestate):
        reward = 0
        for i in Gamestate.get_champions_picked():
            if action in Gamestate.champion_synergies[i]:
                reward += 1.3
            else:
                reward += .9
        return reward

    def altGetReward(self,action,Gamestate):
        reward = 0
        userChoice = Gamestate.get_champions_picked()[0]
        if action in Gamestate.champion_synergies[userChoice]:
            reward += 1.3
        else:
            reward += .9

        return reward