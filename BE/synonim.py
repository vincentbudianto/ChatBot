import json


def load(filename):	
    with open(filename) as data_file:
        data = json.load(data_file)	

    return data

mydict = load('dictionary.json')

def getSinonim(word):
    global mydict
    for kata in mydict.keys():
        for sinonim in mydict[kata]['sinonim']:
            if (sinonim == word):
                return kata

    return word


def changeSinonim(word):
    str = word.split( )
    for i in range(len(str)):
        str[i] = getSinonim(str[i])
    word = ' '.join(str)
    return word


# lis = getSinonim('kamu')
# if (lis != 0):
#     print(lis)
# else:
#     print("tidak ada")