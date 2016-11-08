from lxml import html
import requests
import sys

champion = sys.argv[1]
lolcounter = requests.get('http://lolcounter.com/champions/' + champion)
tree = html.fromstring(lolcounter.content)
champSynergy = tree.xpath('//div[@class="good-block"]//div[contains(@class, "champ-block")]//a//@find[1]')

uniList = list(set(champSynergy))

print "synergy: ", uniList