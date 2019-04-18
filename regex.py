import re

def regex(T, P):
	text = P.split()
	lengthP = len(text)
	lengthT = len(T)
	percent = [0 for i in range(lengthT)]
	found = False
	i = 0

	while ((i < lengthT) and not(found)):
		j = 0
		length = 0
		valid = True
		
		while ((j < lengthP) and (valid)):
			x = re.search(text[j], T[i][0])
			
			if (x == None):
				valid = False
			else:
				length += len(text[j])
				
				if (j != (lengthP - 1)):
					length += 1
				
				j += 1

		if ((len(P) > len(T[i][0])) and (length != 0)):
			percent[i] = float(len(T[i][0])/len(P))
		else:
			percent[i] = float(length/len(T[i][0]))
		
		if (j == lengthP):
			found = True
		else:
			i += 1
	
	if (found):
		return i, percent
	else:
		return -1
