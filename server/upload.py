import requests, json

def upload():
    url = "http://93.73.73.40:8000/"
    file = {'file': open('static/bg.jpg', 'rb')}

    r = requests.post(url, files=file)
    cnt = json.loads(r.content)

    print cnt['dress']

upload()
