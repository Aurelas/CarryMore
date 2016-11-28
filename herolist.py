from lxml import html
import requests
import sys

champlist = requests.get('http://leagueoflegends.wikia.com/wiki/List_of_champions')
tree = html.fromstring(champlist.content)
heroes = tree.xpath('//table//tbody//tr')
herolist = list(set(heroes))

print "champion list: ", herolist