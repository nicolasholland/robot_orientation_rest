from os.path import join
import imageio
import requests
from model import resize_dec
url = 'http://localhost:5000/api'


@resize_dec
def send(img, url):
    retval = requests.post(url, json=img.tolist())
    return retval.json()

img = imageio.imread(join('images', 'south.png'))[:, :, :3]
r = send(img, url)
print(r)

