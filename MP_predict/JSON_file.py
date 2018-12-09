import json
import urllib2
import requests

class JSON_file():

    def __init__(self, json_url, area):
        self.json_url = json_url
        self.area = area

    def save_file(self):
        route_link = requests.get(self.json_url)
        
        
