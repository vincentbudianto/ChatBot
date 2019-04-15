from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def readFile(str):
	f = open(str, "r")
	if f.mode == "r":
		contents = f.read()
		return contents

def Boyer_Moore (T,P) :
	match = False
	m = len(P)
	n = len(T)
	i = m-1
	j = m-1
	
	while (i <= n-1 and not match) :
		if (T[i].lower() == P[j].lower()):
			if (j == 0) :
				match = True
			else :
				i = i-1
				j = j-1
		else :
			k = 0
			while (T[i].lower() != P[j].lower() and k < m):
				k = k+1
				j = j-1
			
			i = i+k
			j = m-1

	if (match):
		return i
	else:
		return -1

if __name__ == "__main__":
	T = readFile("pertanyaan.txt")
	print("Masukkan Pattern: ")
	P = str(input())
 
	factory = StopWordRemoverFactory()
	stopword = factory.create_stop_word_remover()
	stop = stopword.remove(P)
	stop = stop.replace('?','')
	id = Boyer_Moore(T,stop)
	
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
		# print(idx)
		