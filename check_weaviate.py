import weaviate
import cv2 
import base64

client = weaviate.Client(
    url="http://44.208.20.199:8080"
)

print(client.get_meta())

img64 = cv2.imread('/home/davide/Documents/Microorganism_Search_Engine-main/webinterface/src/assets/log.png')
try:
    img64 = cv2.imencode('.png', img64)
except:
    print('skipped')
img64 = base64.b64encode(img64[1]).decode('utf-8')


u = client.query.get(
       "Microrganism", ['species', 'attributes']
       ).with_near_image(
           { "image": img64}, encode=False
       ).with_limit(2).with_additional(['certainty']).do()

print(u)