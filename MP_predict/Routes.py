'''
Routes class takes a given area and creates a json object for that entire area.
Eventually, individual routes will be parsed out and saved into an array.
'''
import requests
import json

class Routes():

    def __init__(self, route_url):
        self.page =  requests.get(route_url)
        self.data = json.loads(self.page.content.decode('utf-8'))
        self.route_dict = self.data['routes']
        self.getDescription

        print(self.route_dict[5].get('id'))

    def getDescription(self):
        for route in route_dict:
            # description =
            # route['description'] = description

