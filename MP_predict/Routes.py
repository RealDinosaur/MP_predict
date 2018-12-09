'''
Routes class takes a given area and creates a json object for that entire area. 
Eventually, individual routes will be parsed out and saved into an array.
'''
import requests
import json

class Routes():

    def __init__(self, route_url):
        self.request =  requests.get(route_url)
        self.json = self.request.json()
        self.route_list = []
        print(self.json)
        
