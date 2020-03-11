import requests

for i in range(1, 100):
    url = 'http://45.40.253.112/lovechat//main/question?count=20&page={}'.format(i)

    response = requests.get(url=url)
    print(response.json())
