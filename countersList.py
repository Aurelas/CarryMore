from lxml import html
import requests
import sys

i = 133
championList = []
champNames = []
herolist = ['aatrox', 'ahri', 'akali', 'alistar', 'amumu', 'anivia', 'annie', 'ashe', 'aurelionsol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'cassiopeia', 'chogath', 'corki', 'darius', 'diana', 'drmundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce', 'jhin', 'jinx', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kennen', 'khazix', 'kindred', 'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'masteryi', 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'nidalee', 'nocturne', 'nunu', 'olaf', 'orianna', 'pantheon', 'poppy', 'quinn', 'rammus', 'reksai', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'sejuani', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'syndra', 'tahmkench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vi', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xerath', 'xinzhao', 'yasuo', 'yorick', 'zac', 'zed', 'ziggs', 'zilean', 'zyra']
for x in range(133):
	lolcounter = requests.get('http://www.championcounter.com/' + herolist[x])
	tree = html.fromstring(lolcounter.content)
	weakAgainst = tree.xpath('//div[@id="weakAgainst"]//a//h4/text()')
	strongAgainst = tree.xpath('//div[@id="strongAgainst"]//a//h4/text()')
	weakList = list(set(weakAgainst))
	strongList = list(set(strongAgainst))
	weakStrongList = [weakList, strongList]
	championList.append([herolist[x], weakList, strongList])
	champNames.append(championList[x][0])
f = open('champion_list.txt', 'w')
for item in champNames:
  f.write("%s\n" % item)