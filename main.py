from bs4 import BeautifulSoup
import requests

# https://weather.gc.ca/lightning/index_e.html?id=NAT
# https://weather.gc.ca/lightning/index_e.html?id=ATL

r = requests.get('https://weather.gc.ca/lightning/index_e.html?id=ATL')

soup = BeautifulSoup(r.content, 'html.parser')

num_images = soup.find(id='wxo-animator').attrs['data-image-count']

for count in range(0, int(num_images)):
    print(soup.find(id='wxo-animator').attrs['data-wxo-anim-' + str(count)])
