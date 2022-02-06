import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
data = BeautifulSoup(response,'html.parser')
#print(response)
#print(data)
kospi = data.select_one('#KOSPI_now')
print(f'현재의 코스피 지수를 {kospi.text}입니다.')
