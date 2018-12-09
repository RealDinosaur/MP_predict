'''
Simple html read file - example file
'''
from lxml import html

import requests

page = requests.get('https://www.mountainproject.com/route/106895203/lost-souls')
tree = html.fromstring(page.content)

description = tree.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[3]/div[2]/div/text()')

print(description)
