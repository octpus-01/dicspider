from spider_part import find_everything

words = ['challenge']

for i in words:
    index_i = str(words.index(i))
    print('----------------------------------'+index_i+'----------------------------------')

    print(find_everything(i))
