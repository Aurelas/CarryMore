from lxml import html
import requests
import sys

champion = sys.argv[1]
lolcounter = requests.get('http://lolcounter.com/champions/' + champion)
tree = html.fromstring(lolcounter.content)
synergy = tree.xpath('//div[@class="good-block"]//div[contains(@class, "champ-block")]//a//@find[1]')
weakAgainst = tree.xpath('//div[@class="weak-block"]//div[contains(@class, "champ-block")]//a//@find[1]')
strongAgainst = tree.xpath('//div[@class="strong-block"]//div[contains(@class, "champ-block")]//a//@find[1]')

synList = list(set(Synergy))
weakList = list(set(Synergy))
strongList = list(set(Synergy))

print "synergy: ", uniList, "\n weak: ", weakList, "\nstrong: ", strongList