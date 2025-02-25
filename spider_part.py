import requests

from bs4 import BeautifulSoup


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'}
url_initial = "https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/"


def find_everything(word):

    result = ''
    word = str(word)
    url = url_initial + word
    
    re = requests.get(url, headers=header)
    info = BeautifulSoup(re.text,"html.parser")

    headline_exp = info.find_all("h3",attrs={'class':'dsense_h'})

    example = info.find_all('div',attrs={'class':'def-body ddef_b'})

    definition_en = info.find_all("div",attrs={'class':'def ddef_d db'})

    l = len(headline_exp) - 1

    for i in range(0, l):
        result = result + '\n' + str(headline_exp[i].text)+'\n'+str(definition_en[i].text) + '\n'+ str(example[i].text)

    return result


                                                                                                                                         
