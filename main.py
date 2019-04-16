from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from boyer_moore import *
from kmp import *
from regex import *

def readFile(str):
	f = open(str, "r")
	if f.mode == "r":
		contents = f.read()
		return contents

if __name__ == "__main__":
    T = readFile("pertanyaan.txt")
    print("Masukkan Pattern: ")
    P = str(input())

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    stop = stopword.remove(P)
    stop = stop.replace('?','')

    print("Pilih Metode Pencarian")
    print("1. Boyer Moore")
    print("2. KMP")
    print("3. Regex")
    pil = int(input())

    if (pil == 1):
        id = Boyer_Moore(T,stop)
    elif (pil == 2):
        id = KMP(T,stop)
    elif (pil == 3):
        id = regex(T,stop)

    idx = 0
    if (id != -1):
        for i in range(id):
            if (T[i] == '\n'):
                idx = idx+1

        str = ''
        while (T[id] != '\n'):
            id = id-1
        
        while (T[id+1] != '\n'):
            str += T[id+1]
            id = id+1

        if (str.lower() != stop.lower()):
            idx = -1
    else:
        idx = -1

    if (idx != -1):
        J = readFile("jawaban.txt")
        n = 0
        ans = ''
        i = 0
        while (n != idx):
            if (J[i] == '\n'):
                n = n+1
            i = i+1

        while (J[i] != '\n'):
            ans += J[i]
            i = i+1

        print(ans)