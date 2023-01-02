import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/confirm/issueNo'
params ={'serviceKey' : 'Z%2BqOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1%2Fe7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ%3D%3D', 'animalNo' : '160053500174' }

response = requests.get(url, params=params)
print(response.content)