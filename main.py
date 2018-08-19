from bs4 import BeautifulSoup
import requests
import shutil

# https://weather.gc.ca/lightning/index_e.html?id=NAT
# https://weather.gc.ca/lightning/index_e.html?id=ATL

r = requests.get('https://weather.gc.ca/lightning/index_e.html?id=ATL')

soup = BeautifulSoup(r.content, 'html.parser')

num_images = soup.find(id='wxo-animator').attrs['data-image-count']

for count in range(0, int(num_images)):
    current_image = soup.find(id='wxo-animator').attrs['data-wxo-anim-' + str(count)]

    img = requests.get('https://weather.gc.ca' + current_image, stream=True)

    filename = current_image.split('/')[-1:][0]

    if img.status_code == 200:
        with open('./img/' + filename, 'wb') as f:
            img.raw.decode_content = True
            shutil.copyfileobj(img.raw, f)

