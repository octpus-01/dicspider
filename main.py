from spider_part import find_everything

type_in = ''
words = []
while type_in != '0' :
   
    type_in = str(input('enter the words or 0 to stop: '))
    words.append(type_in)

words.remove('0')
    

print(words)


for i in words:
    index_i = str(words.index(i))

    print('----------------------------------'+index_i+'----------------------------------')


    print(find_everything(i))
