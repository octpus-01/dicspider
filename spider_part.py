import requests

from bs4 import BeautifulSoup


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}
url_initial = "https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/"


def find_everything(word):

    word = str(word)
    url = url_initial + word
    
    re = requests.get(url, headers=header)
    info = BeautifulSoup(re.text,"html.parser")

    definition_CH = info.find("div",attrs={'class':'def ddef_d db'}).text

    return definition_CH


    # 找到英语解释
    #definition_en = info.find_all("div",attrs={'class':'def ddef_d db'})

    # 找到例句和翻译
    #example = info.find_all("div",attrs={'class':'examp dexamp'})


    #print(definition_CH[0].get('content'))

    #for c in definition_en:
    #    print(c.text)
        
    #for b in example:
     #   print(b.text)
    
    #print('\n')

                                                                                                                                                                          
