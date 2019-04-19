import re

def regex(T, P):
	textP = P.split()
	lengthP = len(textP)
	lengthR = len(P)
	lengthT = len(T)
	percent = [0 for i in range(lengthT)]
	i = 0
	
	while (i < lengthT):
		j = 0
		length = 0
		textQ = T[i][0].split()
		lengthQ = len(textQ)
		lengthS = len(T[i][0])
		
		if (lengthP > lengthQ):
			while (j < lengthQ):
				x = re.search(textQ[j], P)
				
				if (x != None):
					length += len(textQ[j])
					
					if (j != (lengthQ - 1)):
						length += 1
				
				j += 1
			
			percent[i] = float(length/lengthR)
		else:
			while (j < lengthP):
				x = re.search(textP[j], T[i][0])
				
				if (x != None):
					length += len(textQ[j])
					
					if (j != (lengthP - 1)):
						length += 1
					
				j += 1
			
			percent[i] = float(length/lengthS)
	
		i += 1
	
	return (i, percent)
