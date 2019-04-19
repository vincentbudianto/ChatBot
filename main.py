import sys
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from boyer_moore import *
from kmp import *
from regex import *
from synonim import *

def readFile(str):
	f = open(str, encoding = "utf8")
	contents = f.read()
	return contents

def getanswer(id):
	idx = 0
	
	for i in range(id):
		if (Q[i] == '\n'):
			idx = idx + 1

	str = ''
	
	while (Q[id] != '\n'):
		id = id - 1
	
	while (Q[id + 1] != '\n'):
		str += Q[id + 1]
		id = id + 1

	print(Z3[idx][1])

if __name__ == "__main__":
	factory = StopWordRemoverFactory()
	stopword = factory.create_stop_word_remover()

	T = readFile("pertanyaan.txt")
	Z1 = T.split('\n')
	Z2 = []
	Z3 = []
	Q = ''
	
	for i in range(len(Z1)):
		Z2.append(Z1[i].split('. '))

	for j in range(len(Z2)):
		Z3.append(Z2[j][1].split('? '))

	for k in range(len(Z3)):
		Z3[k][0] = Z3[k][0].replace('-', ' ')
		Z3[k][0] = stopword.remove(changeSinonim(Z3[k][0])).lower()
		temp = changeSinonim(Z3[k][0])
		kata = len(temp.split(' '))
		
		for i in range(kata):
			temp = stopword.remove(temp)
		
		Q += temp
		
		if (k != len(Z3)):
			Q += '\n'

	P = sys.argv[1]
	P = P.replace('?', '')
	P = P.replace('-', ' ')
	word = changeSinonim(P)
	kata = len(word.split(' '))

	for i in range(kata):
		word = stopword.remove(word).lower()

	pil = int(sys.argv[2])

	if (pil == 1):
		id = Boyer_Moore(Q,word)
	elif (pil == 2):
		id = KMP(Q,word)
	
	idx = 0

	if (id != -1):
		getanswer(id)
	else:
		id, percent = regex(Z3, word)
		
		if (id != -1):
			print(Z3[id][1])
		else:
			idr = sorted(range(len(percent)), key=lambda i: percent[i])[-3:]
			ids = []
			
			for m in range(3):
				if (percent[idr[m]] != 0):
					ids.insert(0, idr[m])
			
			if (len(ids) >= 1):
				if (percent[ids[0]] >= 0.9):
					print(Z3[ids[0]][1])
				else:
					ok = False
			
					if (len(ids) == 1):
						print('Mungkin maksud anda adalah:\n')
						print('1. ' + Z3[ids[0]][0])
						c = int(input('Pertanyaan ke-'))
						
						while (not(ok)):
							if (c == 1):
								idx = ids[0]
								ok = True
					elif (len(ids) == 2):
						print('Mungkin maksud anda adalah:')
						print('1. ' + Z3[ids[0]][0])
						print('2. ' + Z3[ids[1]][0])
						c = int(input('Pertanyaan ke-'))
						
						while (not(ok)):
							if (c == 1):
								idx = ids[0]
								ok = True
							elif (c == 2):
								idx = ids[1]
								ok = True
							else:
								c = int(input('Pertanyaan ke-'))
					elif (len(ids) == 3):
						print('Mungkin maksud anda adalah:')
						print('1. ' + Z3[ids[0]][0])
						print('2. ' + Z3[ids[1]][0])
						print('3. ' + Z3[ids[2]][0])
						c = int(input('Pertanyaan ke-'))
						
						while (not(ok)):
							if (c == 1):
								idx = ids[0]
								ok = True
							elif (c == 2):
								idx = ids[1]
								ok = True
							elif (c == 3):
								idx = ids[2]
								ok = True
							else:
								c = int(input('Pertanyaan ke-'))
					
					print(Z3[idx][1])
			else:
				print("Maaf saya tidak mengerti maksud Anda :(")			
