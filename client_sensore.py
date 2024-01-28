import requests
import random
import time

from time import sleep
from tqdm import tqdm
immagine=None

BASE_URL = "http://127.0.0.1:8000"


def model(immagine):
    print("..faccio la predizione...")
    for i in tqdm(range(5)):
        sleep(1)
    return random.choice([1,2,3,4])


### viene azionata dal pir/sensori di movimento la fotocamera
### la foto viene scattata
while True:
    
    input("immagine rilevata (S/N):")
    sleep(3)
    print("scatto la foto")
    data_to_send = {"ripartizione_del_cestino": model(immagine)}


    headers={'User-Agent': 'Custom'}
    response = requests.post(f"{BASE_URL}/api_post", json=data_to_send)
    print("POST:::", response.status_code, response.text)



#response = requests.get(f"{BASE_URL}/api_get")
#print("GET:::", response.status_code, response.text)