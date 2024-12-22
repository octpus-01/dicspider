import requests

from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}

url = f"https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/contemporary"

re = requests.get(url, headers=header)

info = BeautifulSoup(re.text,"html")

print(info)

#   TODO:CONTINUE DEVELOPING
