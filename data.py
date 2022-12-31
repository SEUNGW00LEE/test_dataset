import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/animalTrace/traceNoSearch'
params ={'serviceKey' : 'Yt8D2ZaS0jiWYKFjO8tk+5j/dc2KHCs7mOFhjdLGpil1WgX3RBYzX1j91EG2PqKHxlo6lTcXURg3iSdWOEuEhw==', 'traceNo' : 'L01709271277007t', 'optionNo' : '9', 'corpNo' : '1178522046' }

response = requests.get(url, params=params)
print(response.content)