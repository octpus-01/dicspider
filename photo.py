import requests as re

from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}

url = 'https://wallspic.com/cn/album/3840x2160'

response = re.get(url=url,headers=header)

info = BeautifulSoup(response.text,"html.parser")

#urls_photo = info.find_all("div",attrs={'class':'gallery_fluid-column'})

print(info)