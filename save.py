
def save(text,fil):
    text = str(text)
    with open(file=fil,mode='a+') as f :
        f.write(text)
    
    f.close()

    return None


