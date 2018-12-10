'''
Routes class takes a given area and creates a json object for that entire area.
Eventually, individual routes will be parsed out and saved into an array.
'''
import json
from lxml import html
import requests

class Routes():

    def __init__(self, route_url):
        self.page =  requests.get(route_url)
        self.data = json.loads(self.page.content.decode('utf-8'))
        self.route_dict = self.data['routes']
        self.getDescription()
        self.convertGradeToInt()
        self.route_values = {}

        #print(self.route_dict[5])
        #print(self.route_dict[5].get('id'))

    '''
    Get URL from route dictonary, use HTML parser to get route description from
    MP page, add value of "description" for the route. 

    [[NOTE: had to add try/except, route "Baby With a Nail Gun" was showing error
    at html_description, most likely an issue on MP site.]]
    '''
    def getDescription(self):
        i = 0
        for route in self.route_dict:
            i += 1
            route_url = route['url'] 
            page = requests.get(route_url)
            tree = html.fromstring(page.content)
            try:
                html_description = tree.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[3]/div[2]/div/text()')
                route['description'] = html_description[0]
            except:
                route['description'] = 'No description'

    '''
    Sport climbing routes on Mountain Project are graded on 5.x scale, with x being
    any number from 0 - 15. Routes may also have additional suffixes. Modifiers, 
    ordered from lowest to highest:
    a, -, b, [blank], c, +, d
    This function takes the difficulty and gives it an integer value. 
    '''
    def convertGradeToInt(self):
        pass
