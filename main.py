import sys
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from boyer_moore import *
from kmp import *
from regex import *
from synonim import *

def readFile(str):
	f = open(str, "r")
	if f.mode == "r":
		contents = f.read()
		return contents

if __name__ == "__main__":
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    
    T = readFile("pertanyaan.txt")
    Z1 = T.split('\n')
    Z2 = []
    Z3 = []

    for i in range(len(Z1)):
        Z2.append(Z1[i].split('. '))

    for j in range(len(Z2)):
        Z3.append(Z2[j][1].split('? '))

    Q = ''	
    for k in range(len(Z3)):
        temp = changeSinonim(Z3[k][0])
        kata = len(temp.split(' '))
        for i in range(kata):
            temp = stopword.remove(temp)
        Q += temp
        
        if (k != len(Z3)):
            Q += '\n'

    P = sys.argv[1]
    P = P.replace('?','')
    word = changeSinonim(P)
    kata = len(word.split(' '))
    for i in range(kata):
        word = stopword.remove(word)

    pil = int(sys.argv[2])
    if (pil == 1):
        id = Boyer_Moore(Q,word)
    elif (pil == 2):
        id = KMP(Q,word)

    idx = 0
    if (id != -1):
        for i in range(id):
            if (Q[i] == '\n'):
                idx = idx+1

        str = ''
        while (Q[id] != '\n'):
            id = id-1
        
        while (Q[id+1] != '\n'):
            str += Q[id+1]
            id = id+1
    else:
        idx = -1

    if (idx != -1):
        print(Z3[idx][1])
    else:
        print("Saya tidak mengerti maksud Anda :(")
