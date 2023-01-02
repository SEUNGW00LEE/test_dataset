import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/auct/pigJejuGrade'
params ={'serviceKey' : 'Z+qOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1/e7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ==', 'startYmd' : '20160120', 'endYmd' : '20160120', 'skinYn' : 'Y' }

response = requests.get(url, params=params)
print(response.content)