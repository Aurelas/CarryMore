
import util
class QLearningAgent(object):

    def __init__(self):
        #A counter is a ((state,action) = value), pairing
        #Ex (1,East) = 2.3745
        self.qValues = util.Counter()

    def getQValue(self, state, action):
        #Returns the value of the state/action pairing that is located in self.qValues
        return self.qValues[(state,action)]
