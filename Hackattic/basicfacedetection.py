import cv2
import json
import requests
import numpy as np

def take_access_token():
    return input('Please enter your access token : ')

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h, s = img.shape
    step = w//8
    answer = []
    for x in range(0, w+1, step):
        for y in range(0, h+1, step):
            faces = faceCascade.detectMultiScale(
                gray[x:x+step, y:y+step],
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                #flags = cv2.CV_HAAR_SCALE_IMAGE
            )
            if len(faces) > 0:
                answer.append([x//step, y//step])
    return answer

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
hackattic = 'https://hackattic.com/challenges/basic_face_detection/'
get = 'problem'
post = 'solve'
access_code = '?access_token=' + take_access_token()

# Access to Hackattic 
r = requests.get(hackattic + get + access_code)
url = r.json()['image_url']
pic = requests.get(url)

# Open Image
decoded = cv2.imdecode(np.frombuffer(pic.content, np.uint8), -1)
result = detect_face(decoded)

print(result)
            
pr = requests.post(hackattic + post + access_code, data=json.dumps({'face_tiles': result}))
print(pr.content)