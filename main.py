import requests

from bs4 import BeautifulSoup


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}

words = ['replace','document']

for i in words:
    index_i = str(words.index(i))
    print('----------------------------------'+index_i+'----------------------------------')
    i = str(i)

    url = "https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/"+i
    
    re = requests.get(url, headers=header)
    info = BeautifulSoup(re.text,"html.parser")

    definition_CH = info.find_all("meta",attrs={'itemprop':'headline'})
    definition_en = info.find_all("div",attrs={'class':'def ddef_d db'})

    example = info.find_all("div",attrs={'class':'examp dexamp'})

    for con in definition_CH:
        print(con.get('content'))
      
    for c in definition_en:
        print(c.text)
        
    for b in example:
        print(b.text)
    
    print('\n')


