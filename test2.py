import cv2
import requests

img = cv2.imread('2.jpg')
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
file = '2.jpg'
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
headers = {
    'authority': 'imagerecognize.com',
    'origin': 'https://imagerecognize.com',
    'referer': 'https://imagerecognize.com/text/',
    'accept-language': 'en-US,en;q=0.9',
}

data = {
    'type': 'detect_text',
    'file': img,
    'Content-Type': 'image/jpeg'
}

response = requests.post('https://imagerecognize.com/ir.php', data=data)
print(response.json())
