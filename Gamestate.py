

class Gamestate(object):

    def __init__(self):
        #Legal state_num values are 0-5, 0-4 are states that pick actions and have transitions
        #state_num 5 is considered a Terminal state / has no transitions / is done
        #State_num 0 represents our choice/ users choice
        self.state_num = 0

        #Keep track of what has and hasn't been picked yet

        self.roles_picked = {'Support': False,'Mid': False, 'Top': False, 'Jungle': False, 'ADC': False}

        #Team champions that are picked are stored into lists, so that we can compare and make sure
        #either team doesnt pick duplicate champions, max of 5 champions each 0-4
        self.team_champions_picked = []

        #Holds a list of all AIs that will pick a champion during our simulations
        #Max of 5 AIs 0 - 4, the 0th spot in our ai list corresponds to state_num 1
        #since state_num 0 represents our choice / user choice
        self.ai = []
        self.champion_synergies = {'aatrox': ['gnar', 'xed', 'azir', 'masteryi', 'tryndamere', 'yasuo'],
                                   'ahri': ['jax', 'kled', 'riven', 'akali', 'vayne', 'katarina'],
                                   'akali': ['diana', 'kindred', 'shen', 'ahri', 'aeBlanc', 'katarina'],
                                   'alistar': ['tristana', 'jhin', 'kindred', 'vayne', 'yasuo', 'kalista'],
                                   'amumu': ['illaoi', 'malphite', 'annie', 'missfortune', 'katarina', 'kennen'],
                                   'anivia': ['janna', 'ashe', 'jarvaniv', 'jhin', 'trundle', 'vayne'],
                                   'annie': ['amumu', 'sivir', 'gangplank', 'katarina', 'jinx', 'kalista'],
                                   'ashe': ['janna', 'braum', 'thresh', 'morgana', 'missfortune', 'leona'],
                                   'aurelionsol': ['braum', 'tahmkench', 'ahri', 'morgana', 'missfortune', 'katarina'],
                                   'azir': ['amumu', 'gnar', 'pantheon', 'ahri', 'aatrox', 'yasuo'],
                                   'bard': ['jhin', 'missfortune', 'vayne', 'ezreal', 'jinx', 'caitlyn'],
                                   'blitzcrank': ['Tristana', 'Jhin', 'Miss Fortune', 'Draven', 'Vayne', 'Jinx'],
                                   'brand': ['Amumu', 'Sona', 'Vladimir', 'Jarvan IV', 'Maokai', 'Malphite'],
                                   'braum': ['kogmaw', 'sivir', 'ashe', 'lucian', 'vayne', 'kalista'],
                                   'caitlyn': ['sona', 'nami', 'thresh', 'bard', 'morgana', 'leona'],
                                   'cassiopeia': ['amumu', 'yorick', 'singed', 'twitch', 'katarina', 'teemo'],
                                   'chogath': ['nocturne', 'lulu', 'reksai', 'aatrox', 'poppy', 'yasuo'],
                                   'corki': ['sona', 'blitzcrank', 'nami', 'thresh', 'leona', 'alistar'],
                                   'darius': ['olaf', 'garen', 'masteryi', 'draven', 'fiora', 'teemo'],
                                   'diana': ['kassadin', 'zac', 'swain', 'akali', 'leona', 'yasuo'],
                                   'drmundo': ['anivia', 'olaf', 'darius', 'thresh', 'leona', 'teemo'],
                                   'draven': ['janna', 'sona', 'blitzcrank', 'nami', 'thresh', 'leona'],
                                   'ekko': ['gnar', 'vi', 'reksai', 'bard', 'annie', 'kalista'],
                                   'elise': ['rengar', 'blitzcrank', 'illaoi', 'karma', 'leona', 'velkoz'],
                                   'evelynn': ['twistedfate', 'orianna', 'shen', 'shaco', 'annie', 'chogath'],
                                   'ezreal': ['sona', 'lux', 'blitzcrank', 'thresh', 'taric', 'leona'],
                                   'fiddlesticks': ['amumu', 'galio', 'nocturne', 'reksai', 'veigar', 'kennen'],
                                   'fiora': ['morgana', 'blitzcrank', 'jarvaniv', 'darius', 'renekton', 'leblanc'],
                                   'fizz': ['amumu', 'vi', 'jarvaniv', 'nami', 'aatrox', 'leona'],
                                   'galio': ['fiddlesticks', 'nunu', 'illaoi', 'katarina', 'wukong', 'kennen'],
                                   'gangplank': ['amumu', 'twistedfate', 'pantheon', 'annie', 'aatrox', 'hecarim'],
                                   'garen': ['lux', 'jarvaniv', 'xinzhao', 'darius', 'katarina', 'nasus'],
                                   'gnar': ['orianna', 'jarvaniv', 'aatrox', 'azir', 'sion', 'yasuo'],
                                   'gragas': ['khazix', 'ashe', 'jayce', 'sejuani', 'malphite', 'yasuo'],
                                   'graves': ['blitzcrank', 'braum', 'taric', 'morgana', 'thresh', 'leona'],
                                   'hecarim': ['kled', 'nocturne', 'orianna', 'lulu', 'jayce', 'zilean'],
                                   'heimerdinger': ['blitzcrank', 'vi', 'rammus', 'thresh', 'skarner', 'teemo'],
                                   'illaoi': ['amumu', 'galio', 'orianna', 'morgana', 'elise', 'jinx'],
                                   'irelia': ['riven', 'orianna', 'malphite', 'ahri', 'akali', 'leesin'],
                                   'ivern': ['rengar', 'khazix', 'blitzcrank', 'teemo', 'caitlyn', 'nidalee'],
                                   'janna': ['ashe', 'jhin', 'draven', 'vayne', 'yasuo', 'caitlyn'],
                                   'jarvaniv': ['yasuo', 'gnar', 'orianna', 'anivia', 'fiora', 'katarina'],
                                   'jax': ['xinzhao', 'darius', 'pantheon', 'ahri', 'aatrox', 'teemo'],
                                   'jayce': ['blitzcrank', 'ahri', 'thresh', 'hecarim', 'skarner', 'nidalee'],
                                   'jhin': ['zyra', 'nautilus', 'blitzcrank', 'thresh', 'morgana', 'leona'],
                                   'jinx': ['ziggs', 'blitzcrank', 'thresh', 'morgana', 'leona', 'tahmkench'],
                                   'kalista': ['nautilus', 'braum', 'thresh', 'leona', 'alistar', 'tahmkench'],
                                   'karma': ['jhin', 'lucian', 'vayne', 'ezreal', 'jinx', 'caitlyn'],
                                   'karthus': ['amumu', 'yorick', 'vladimir', 'Nnocturne', 'soraka', 'kayle'],
                                   'kassadin': ['amumu', 'khazix', 'diana', 'aatrox', 'leesin', 'chogath'],
                                   'katarina': ['amumu', 'galio', 'garen', 'jarvaniv', 'malphite', 'leona'],
                                   'kayle': ['karthus', 'masteryi', 'tryndamere', 'ezreal', 'katarina', 'nasus'],
                                   'kennen': ['amumu', 'fiddlesticks', 'gnar', 'vladimir', 'galio', 'malphite'],
                                   'khazix': ['rengar', 'zed', 'ivern', 'xinzhao', 'aatrox', 'nasus'],
                                   'kindred': ['nocturne', 'ashe', 'thresh', 'bard', 'akali', 'alistar'],
                                   'kled': ['rammus', 'zac', 'ahri', 'aatrox', 'hecarim', 'yasuo'],
                                   'kogmaw': ['nunu', 'nami', 'lulu', 'braum', 'thresh', 'leona'],
                                   'leblanc': ['fiora', 'udyr', 'maokai', 'akali', 'leona', 'veigar'],
                                   'leesin': ['ryze', 'irelia', 'annie', 'warwick', 'yasuo', 'teemo'],
                                   'leona': ['ashe', 'jhin', 'missfortune', 'draven', 'jinx', 'kalista'],
                                   'lissandra': ['amumu', 'zyra', 'nunu', 'ashe', 'sejuani', 'trundle'],
                                   'lucian': ['nautilus', 'nami', 'braum', 'thresh', 'morgana', 'leona'],
                                   'lulu': ['kogmaw', 'missfortune', 'vayne', 'yasuo', 'kalista', 'caitlyn'],
                                   'lux': ['jhin', 'masteryi', 'morgana', 'ezreal', 'jinx', 'caitlyn'],
                                   'malphite': ['amumu', 'orianna', 'missfortune', 'yasuo', 'katarina', 'kennen'],
                                   'malzahar': ['amumu', 'nocturne', 'jarvaniv', 'maokai', 'warwick', 'skarner'],
                                   'maokai': ['ryze', 'brand', 'syndra', 'swain', 'leblanc', 'veigar'],
                                   'masteryi': ['amumu', 'lux', 'ashe', 'darius', 'morgana', 'aatrox'],
                                   'missfortune': ['sona', 'blitzcrank', 'malphite', 'thresh', 'morgana', 'leona'],
                                   'mordekaiser': ['amumu', 'yorick', 'blitzcrank', 'malphite', 'thresh', 'warwick'],
                                   'morgana': ['jhin', 'lucian', 'missfortune', 'twitch', 'jinx', 'caitlyn'],
                                   'nami': ['jhin', 'lucian', 'vayne', 'twitch', 'jinx', 'caitlyn'],
                                   'nasus': ['khazix', 'garen', 'zed', 'lulu', 'udyr', 'renekton'],
                                   'nautilus': ['jhin', 'lucian', 'draven', 'yasuo', 'jinx', 'kalista'],
                                   'nidalee': ['lux', 'jayce', 'ivern', 'varus', 'jinx', 'caitlyn'],
                                   'nocturne': ['fiddlesticks', 'twistedfate', 'kindred', 'reksai', 'hecarim', 'chogath'],
                                   'nunu': ['amumu', 'galio', 'kogmaw', 'ryze', 'corki', 'vayne'],
                                   'olaf': ['amumu', 'blitzcrank', 'drmundo', 'darius', 'aatrox', 'skarner'],
                                   'orianna': ['gnar', 'jarvaniv', 'illaoi', 'malphite', 'yasuo', 'wukong'],
                                   'pantheon': ['amumu', 'jax', 'blitzcrank', 'xinzhao', 'taric', 'sion'],
                                   'poppy': ['aatrox', 'sion', 'taliyah', 'vayne', 'alistar', 'chogath'],
                                   'quinn': ['janna', 'blitzcrank', 'nami', 'thresh', 'morgana', 'leona'],
                                   'rammus': ['heimerdinger', 'kled', 'shen', 'twistedfate', 'ahri', 'veigar'],
                                   'reksai': ['fiddlesticks', 'nocturne', 'shen', 'yasuo', 'ekko', 'chogath'],
                                   'renekton': ['amumu', 'lulu', 'braum', 'aatrox', 'fiora', 'nasus'],
                                   'rengar': ['khazix', 'shen', 'orianna', 'lulu', 'ivern', 'elise'],
                                   'riven': ['vi', 'irelia', 'orianna', 'ahri', 'aatrox', 'yasuo'],
                                   'rumble': ['amumu', 'sona', 'jarvaniv', 'sejuani', 'annie', 'kennen'],
                                   'ryze': ['amumu', 'nunu', 'udyr', 'maokai', 'leesin', 'chogath'],
                                   'sejuani': ['talon', 'yasuo', 'rumble', 'leona', 'lissandra', 'katarina'],
                                   'shaco': ['yorick', 'evelynn', 'blitzcrank', 'orianna', 'shen', 'teemo'],
                                   'shen': ['rengar', 'zed', 'twistedfate', 'ashe', 'reksai', 'akali'],
                                   'shyvana': ['riven', 'shen', 'orianna', 'jarvaniv', 'malphite', 'yasuo'],
                                   'singed': ['zilean', 'cassiopeia', 'sion', 'volibear', 'yasuo', 'teemo'],
                                   'sion': ['gnar', 'jhin', 'pantheon', 'poppy', 'yasuo', 'kalista'],
                                   'sivir': ['nami', 'braum', 'soraka', 'thresh', 'morgana', 'leona'],
                                   'skarner': ['heimerdinger', 'olaf', 'jayce', 'thresh', 'malzahar', 'veigar'],
                                   'sona': ['jhin', 'missfortune', 'draven', 'vayne', 'ezreal', 'caitlyn'],
                                   'soraka': ['sivir', 'jhin', 'lucian', 'vayne', 'jinx', 'caitlyn'],
                                   'swain': ['amumu', 'vladimir', 'diana', 'jarvaniv', 'maokai', 'aatrox'],
                                   'syndra': ['zyra', 'zilean', 'zac', 'maokai', 'nami', 'sion'],
                                   'tahmkench': ['jhin', 'aurelion Sol', 'draven', 'jinx', 'kalista', 'caitlyn'],
                                   'taliyah': ['blitzcrank', 'thresh', 'missfortune', 'poppy', 'vayne', 'yasuo'],
                                   'talon': ['amumu', 'darius', 'zed', 'sejuani', 'sion', 'katarina'],
                                   'taric': ['graves', 'sivir', 'ashe', 'jhin', 'jinx', 'ezreal'],
                                   'teemo': ['jax', 'blitzcrank', 'cassiopeia', 'darius', 'volibear', 'leesin'],
                                   'thresh': ['jhin', 'lucian', 'draven', 'vayne', 'jinx', 'kalista'],
                                   'tristana': ['blitzcrank', 'nami', 'braum', 'thresh', 'leona', 'alistar'],
                                   'trundle': ['blitzcrank', 'anivia', 'aatrox', 'layne', 'lissandra', 'nidalee'],
                                   'tryndamere': ['blitzcrank', 'ashe', 'aatrox', 'kayle', 'morgana', 'zilean'],
                                   'twistedfate': ['nocturne', 'shen', 'rammus', 'gangplank', 'blitzcrank', 'aatrox'],
                                   'twitch': ['nami', 'braum', 'thresh', 'morgana', 'taric', 'leona'],
                                   'udyr': ['amumu', 'janna', 'ryze', 'bard', 'leblanc', 'masus'],
                                   'urgot': ['nami', 'soraka', 'taric', 'thresh', 'leona', 'alistar'],
                                   'varus': ['janna', 'sona', 'blitzcrank', 'nami', 'thresh', 'leona'],
                                   'vayne': ['janna', 'blitzcrank', 'nami', 'lulu', 'braum', 'thresh'],
                                   'veigar': ['amumu', 'fiddlesticks', 'lux', 'maokai', 'warwick', 'leblanc'],
                                   'velkoz': ['amumu', 'jarvaniv', 'jhin', 'elise', 'leona', 'yasuo'],
                                   'vi': ['zed', 'riven', 'fizz', 'yasuo', 'ekko', 'caitlyn'],
                                   'viktor': ['amumu', 'sona', 'jarvaniv', 'aatrox', 'malzahar', 'chogath'],
                                   'vladimir': ['zed', 'jarvaniv', 'lulu', 'swain', 'brand', 'kennen'],
                                   'volibear': ['ashe', 'singed', 'vayne', 'teemo', 'yasuo', 'caitlyn'],
                                   'warwick': ['mordekaiser', 'lux', 'malzahar', 'leesin', 'veigar', 'katarina'],
                                   'wukong': ['amumu', 'galio', 'orianna', 'jarvaniv', 'yasuo', 'katarina'],
                                   'xerath':['amumu', 'evelynn', 'jarvaniv', 'jhin', 'varus', 'leona'],
                                   'xinzhao': ['khazix', 'garen', 'jax', 'jarvaniv', 'pantheon', 'yasuo'],
                                   'yasuo': ['janna', 'reksai', 'malphite', 'alistar', 'wukong', 'chogath'],
                                   'yorick': ['mordekaiser', 'zilean', 'cassiopeia', 'shaco', 'karthus', 'vayne'],
                                   'zac': ['kled', 'diana', 'orianna', 'lulu', 'syndra', 'yasuo'],
                                   'zed': ['khazix', 'shen', 'vi', 'talon', 'aatrox', 'nasus'],
                                   'ziggs': ['amumu', 'jarvaniv', 'aatrox', 'yasuo', 'jinx', 'kennen'],
                                   'zilean': ['jhin', 'syndra', 'tryndamere', 'hecarim', 'vayne', 'caitlyn'],
                                   'zyra': ['ashe', 'jhin', 'syndra', 'yasuo', 'jinx', 'caitlyn']
                                   }
        self.champion_roles = { 'aatrox': 'Jungle', 'ahri': 'Mid','akali': 'Mid', 'alistar': 'Support', 'amumu': 'Jungle',
                                'anivia': 'Mid', 'annie': 'Support', 'ashe': 'ADC', 'aurelionsol': 'Mid', 'azir': 'Mid',
                                'bard': 'Support', 'blitzcrank': 'Support', 'brand': 'Mid', 'braum': 'Support', 'caitlyn': 'ADC',
                                'cassiopeia': 'Mid','chogath': 'Top','corki': 'ADC','darius': 'Top','diana': 'Mid','drmundo': 'Top',
                                'draven': 'ADC', 'ekko': 'Mid', 'elise': 'Jungle', 'evelynn': 'Jungle','ezreal': 'ADC', 'fiddlesticks': 'Jungle',
                                'fiora': 'Top', 'fizz': 'Mid', 'galio': 'Mid', 'gangplank': 'Top', 'garen': 'Top', 'gnar': 'Top',
                                'gragas': 'Mid', 'graves': 'ADC', 'hecarim': 'Jungle', 'heimerdinger': 'Mid', 'illaoi': 'Top',
                                'irelia': 'Top', 'ivern': 'Jungle' , 'janna': 'Support', 'jarvaniv': 'Jungle', 'jax': 'Top','jayce': 'Top',
                                'jhin': 'ADC', 'jinx': 'ADC', 'kalista': 'ADC', 'karma': 'Support', 'karthus': 'Mid', 'kassadin': 'Mid',
                                'katarina': 'Mid', 'kayle': 'Top', 'kennen': 'Top', 'khazix': 'Jungle', 'kindred': 'Jungle','kled': 'Top',
                                'kogmaw': 'ADC', 'leblanc': 'Mid', 'leesin': 'Jungle', 'leona': 'Support', 'lissandra': 'Top', 'lucian': 'ADC',
                                'lulu': 'Support', 'lux': 'Mid', 'malphite': 'Top', 'malzahar': 'Mid', 'maokai': 'Top', 'masteryi': 'Jungle',
                                'missfortune': 'ADC', 'mordekaiser': 'Top',  'morgana': 'Support', 'nami': 'Support', 'nasus': 'Jungle',
                                'nautilus': 'Jungle', 'nidalee': 'Top', 'nocturne': 'Jungle', 'nunu': 'Jungle', 'olaf': 'Jungle',
                                'orianna': 'Mid', 'pantheon': 'Jungle', 'poppy': 'Top', 'quinn': 'Top', 'rammus': 'Jungle', 'reksai': 'Jungle',
                                'renekton': 'Top', 'rengar': 'Top', 'riven': 'Top', 'rumble': 'Top', 'ryze': 'Top', 'sejuani': 'Jungle',
                                'shaco': 'Jungle', 'shen': 'Top', 'shyvana': 'Jungle', 'singed': 'Top', 'sion': 'Top', 'sivir': 'ADC',
                                'skarner': 'Jungle', 'sona': 'Support', 'soraka': 'Support', 'swain': 'Top', 'syndra': 'Mid', 'tahmkench': 'Support',
                                'taliyah': 'Mid', 'talon': 'Mid', 'taric': 'Support', 'teemo': 'Top', 'thresh': 'Support', 'tristana': 'ADC',
                                'trundle': 'Top', 'tryndamere': 'Top', 'twistedfate': 'Mid', 'twitch': 'ADC', 'udyr': 'Jungle', 'urgot': 'ADC',
                                'varus': 'ADC', 'vayne': 'ADC', 'veigar': 'Mid', 'velkoz': 'Support', 'vi': 'Jungle', 'viktor': 'Mid',
                                'vladimir': 'Top', 'volibear': 'Jungle', 'warwick': 'Jungle', 'wukong': 'Top', 'xerath': 'Mid',
                                'xinzhao': 'Jungle', 'yasuo': 'Mid', 'yorick': 'Top', 'zac': 'Jungle', 'zed': 'Mid', 'ziggs': 'Mid', 'zilean': 'Support',
                                'zyra': 'Support'}
        self.jungle_champs = []
        self.mid_champs = []
        self.adc_champs = []
        self.support_champs = []
        self.top_champs = []

        self.get_champion_from_role()


    #Sets state of the gamestate, should be called after everytime we pick a champion
    def set_state(self,num):
        self.state_num = num

    #returns the state_num
    def get_state(self):
        return self.state_num

    #returns list of champions chosen
    def get_champions_picked(self):
        return self.team_champions_picked


    #takes champion_id and state
    #Once it determines the correct team that is choosing, append the champion chosen to that team's pick list
    def update_champions(self,champion_id):
            #if champion_id in self.team_champions_picked:
                #raise ValueError("champions_picked is not allowed to have duplicate champions")
        self.team_champions_picked.append(champion_id)


    #Returns size of the picked list based on state
    def get_champions_picked_size(self,):
            return len(self.team_champions_picked)


    #Returns the specific champion chosen per state
    def get_champion_from_state(self,state):
            return self.team_champions_picked[state - 1]


    #Checks to see whether or not the gamestate is in the TERMINAL STATE
    def is_end_state(self):
        if self.get_state() == 5:
            return True
        return False

    #Returns an integer that represents the next state
    def get_next_state(self):
        return self.state_num + 1

    def get_champion_from_role(self):
        for i in self.champion_roles:
            if self.champion_roles.get(i) == 'Jungle':
                self.jungle_champs.append(i)
            if self.champion_roles.get(i) == 'Mid':
                self.mid_champs.append(i)
            if self.champion_roles.get(i) == 'Top':
                self.top_champs.append(i)
            if self.champion_roles.get(i) == 'Support':
                self.support_champs.append(i)
            if self.champion_roles.get(i) == 'ADC':
                self.adc_champs.append(i)

    def reset_champions_picked(self,user_choice):
        new_list = []
        new_list.append(user_choice)
        self.team_champions_picked = new_list

    def get_role_from_champion(self,champion_name):
        return self.champion_roles[champion_name]






