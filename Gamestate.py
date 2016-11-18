
#This Object will know everything thats important to our program
#It will know the state we are in
#It will know what champion each team has picked
#It will have a list of AIs that work for each state
#There will be 9 different AIs Working on our simulation 1 - 9, each AI will determine
#the best champion to pick for the role it is designated to work on
class Gamestate(object):

    def __init__(self):
        #Legal state_num values are 0-10, 0-9 are states that pick actions and have transitions
        #state_num 10 is considered a Terminal state / has no transitions / done
        #State_num 0 represents our choice/ users choice
        self._state_num = 0
        #Team champions that are picked are stored into lists, so that we can compare and make sure
        #either team doesnt pick duplicate champions, max of 5 champions each 0-4
        self._team1_champions_picked = []
        self._team2_champions_picked = []

        #Holds a list of all AIs that will pick a champion during our simulations
        #Max of 9 AIs 0 - 8, the 0th spot in our ai list corresponds to state_num 1
        #since state_num 0 represents our choice / user choice
        self._ai = []


    #Sets state of the gamestate, should be called after everytime we pick a champion
    def set_state(self,num):
        self._state_num = num

    #returns the state_num
    def get_state(self):
        return self._state_num

    #returns list of champions chosen by team 1
    def get_team1_champions(self):
        return self._team1_champions_picked

    #returns lsit of champions chosen by team 2
    def get_team2_champions(self):
        return self._team2_champions_picked

    #takes champion_id and state
    #Uses the state to determine which team is choosing, <= 4 is team 1, >= 5 is team 2
    #Once it determines the correct team that is choosing, append the champion chosen to that team's pick list
    def update_champions(self,champion_id,state):
        if state <= 4:
            if champion_id in self._team1_champions_picked:
                raise ValueError("champions_picked is not allowed to have duplicate champions")
            self._team1_champions_picked.append(champion_id)
        elif state >= 5 and state <= 9:
            if champion_id in self._team2_champions_picked:
                raise ValueError("champions_picked is not allowed to have duplicate champions")
            self._team2_champions_picked.append(champion_id)
        else:
            raise ValueError("team parameter is not valid")

    #Returns size of the picked list based on state
    def get_champions_picked_size(self,state):
        if state <= 4:
            return len(self._team1_champions_picked)
        elif state >= 5 and state >= 9:
            return len(self._team2_champions_picked)

    #Returns the specific champion chosen per state
    def get_champion_from_state(self,state):
        if state <= 4:
            return self._team1_champions_picked[state - 1]
        elif state >= 5 or state >= 9:
            print state, "3"
            return self._team2_champions_picked[state - 5]

    #Returns the specific AI that is working on a state
    #Each AI will have it's own different list of champions it can work with and their QValues
    #Thus is why we need multiple AIs working in our program
    def get_ai_from_state(self,state):
        return self._ai[state - 1]

    #Checks to see whether or not the gamestate is in the TERMINAL STATE
    def is_end_state(self):
        if self.get_state() == 10:
            return True
        return False

    #Returns an integer that represents the next state
    def get_next_state(self):
        return self._state_num + 1



