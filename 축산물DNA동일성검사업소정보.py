import requests

url = 'http://data.ekape.or.kr/openapi-data/service/user/mtrace/dna/sampleGatherCompany'
params ={'serviceKey' : 'Z%2BqOG0BXgDHjNYllLmPz7rVXZehwdYityRTSOZLJRIYYpIos1%2Fe7Mm488NQHCx3OmzOjKti2u4Y56rggoC2ktQ%3D%3D', 'startYmd' : '20160101', 'endYmd' : '20160111', 'sampleTypeCd' : '200', 'localNm' : '전라남도', 'orgCd' : '4820000' }

response = requests.get(url, params=params)
print(response.content)