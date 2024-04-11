"""
To test the message bot function we created a dummy group on telegram and tested it using this script
"""

import requests
from PIL import Image

# Load the image
image = Image.open('logo.png')

# Resize the image as before
new_width = image.width // 2
new_height = image.height // 2
resized_image = image.resize((new_width, new_height))

# Save the resized image with compression
resized_image.save('image.png', 'PNG', quality=25)

bot_token = "insert bot_token here"
chat_id = 'insert chat_id here'
file_path = 'image.png'
url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'


# For the caption, replace 'Your caption here' with your actual caption
data = {
    'chat_id': chat_id,
    'caption': 'Hello everybody. Check out our website for courses in professional tech development, \
    specifically designed for displaced Afghans in Scotland\n\
        سلام به همه. وب سایت ما را برای دوره های توسعه فنی حرفه ای، که به طور خاص برای افغان های آواره در اسکاتلند طراحی شده است، بررسی کنید:\n \
            www.inserturlhere.co.uk'
}

files = {
    'photo': open(file_path, 'rb')
}

response = requests.post(url, data=data, files=files)
print(response.json())