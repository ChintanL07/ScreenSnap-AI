import requests

url = 'http://127.0.0.1:5000/generate-instructions'

# JSON data
data = {
    'context': 'Describe the context here'
}

# Image files
files = {
    'images': open('path/to/your/image1.png', 'rb'),
    'images': open('path/to/your/image2.png', 'rb')
}

response = requests.post(url, data=data, files=files)

print(response.json())