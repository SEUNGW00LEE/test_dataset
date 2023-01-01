import requests,xmltodict

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'Z+qOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1/e7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20230101', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

content = requests.get(url, params=params).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body']['items'], ensure_ascii = False)
print(jsonString)