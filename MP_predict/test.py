'''
Testing file for classes
'''

from Routes import Routes

def read_file():
    url = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=38.078&lon=-81.063&maxDistance=60&minDiff=5.6&maxDiff=5.15&key=200219818-f9fb243d0b8066ff66b9edc9f49bd3e4'
    area = 'NRG'
    route = Routes(url)


if __name__ == '__main__':
    read_file() 
