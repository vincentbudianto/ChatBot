def file():
	f = open("pertanyaan.txt", "r")
	if f.mode == "r":
		contents = f.read()
		return contents

def Boyer_Moore (T,P) :

	match = False
	
	m = len(P)
	n = len(T)
	i = m-1
	j = m-1
	id = 0
	
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
	T = file()
	print("Masukkan Pattern: ")
	P = str(input())

	id = Boyer_Moore(T,P)

	if (id != -1):
		idx = 0
		for i in range(id):
			if (T[i] == '\n'):
				idx = idx+1

		print(idx)
	else:
		print(id)