'''
Routes class takes a given area and creates a json object for that entire area.
Eventually, individual routes will be parsed out and saved into an array.
'''
import json
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Routes():

    def __init__(self, route_url):
        self.route_url = route_url
        self.route_df = self.getRouteDataFrame()

    def getRouteDataFrame(self):
        '''
        Create DataFrame object from JSON data
        '''
        page =  requests.get(self.route_url)
        json_data = json.loads(page.content.decode('utf-8'))
        route_df = pd.DataFrame(json_data['routes'])
        route_df['description'] = route_df.url.apply(self.getDescription)
        print(route_df.description)
        return route_df

    def getDescription(self, route_url):
        '''
        Pull description from route URL, and add to route_df
        '''
        page = requests.get(route_url)
        tree = html.fromstring(page.content)
        html_description = tree.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[3]/div[2]/div/text()')
        if html_description:
            html_description = html_description[0]
        return(html_description)


    '''
    Sport climbing routes on Mountain Project are graded on 5.x scale, with x being
    any number from 0 - 15. Routes may also have additional suffixes. Modifiers, 
    ordered from lowest to highest:
    a, -, b, [blank], c, +, d
    This function takes the difficulty and gives it an integer value. 
    '''
    def convertGradeToInt(self):
        pass
