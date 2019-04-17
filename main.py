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
	Z1 = T.split('\n')
	Z2 = []
	Z3 = []
	
	for i in range(len(Z1)):
		Z2.append(Z1[i].split('. '))

	for j in range(len(Z2)):
		Z3.append(Z2[j][1].split('? '))
	
	Q = ''
	
	for k in range(len(Z3)):
		Q += Z3[k][0]
		
		if (k != len(Z3)):
			Q += '\n'
	
	print("Masukkan Pattern: ")
	P = str(input())

	factory = StopWordRemoverFactory()
	stopword = factory.create_stop_word_remover()
	stop = stopword.remove(P)
	stop = stop.replace('?','')
	pil = 0
	
	while (pil != 4):
		print("Pilih Metode Pencarian")
		print("1. Boyer Moore")
		print("2. KMP")
		print("3. Regex")
		pil = int(input())

		if (pil == 1):
			id = Boyer_Moore(Q, stop)
		elif (pil == 2):
			id = KMP(Q, stop)
		elif (pil == 3):
			id = regex(Q, stop)
			
		print(id)

		idx = 0
		if (id != -1) and ((pil == 1) or (pil == 2)):
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
		
		print(idx)

		print(Z3[idx][1])
