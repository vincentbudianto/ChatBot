from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def readFile(str):
	f = open(str, "r")
	if f.mode == "r":
		contents = f.read()
		return contents

def computeFail(P):
	length = len(P)
	fail = [0 for i in range(length)]
	i = 1
	j = 0
	
	while (i < length):
		if (P[j].lower() == P[i].lower()):
			fail[i] = j + 1
			i += 1
			j += 1
		elif (j > 0):
			j = fail[j - 1]
		else:
			fail[i] = 0
			i += 1
	
	return fail

def KMP(T, P):
	lengthP = len(P)
	lengthT = len(T)
	fail = computeFail(P)
	i = 0
	j = 0
	
	while (i < lengthT):
		if (P[j].lower() == T[i].lower()):
			if (j == (lengthP - 1)):
				return i - lengthP + 1
			
			i += 1
			j += 1
		elif (j > 0):
			j = fail[j - 1]
		else:
			i += 1
	
	return -1