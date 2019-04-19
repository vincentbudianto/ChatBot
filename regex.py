import re

def regex(T, P):
	textP = P.split()
	lengthP = len(textP)
	lengthR = len(P)
	lengthT = len(T)
	percent = [0 for i in range(lengthT)]
	found = False
	i = 0
	
	#while ((i < lengthT) and not(found)):
	while (i < 30):
		j = 0
		length = 0
		textQ = T[i][0].split()
		lengthQ = len(textQ)
		lengthS = len(T[i][0])
		valid = True
		
		if (lengthP > lengthQ):
			while ((j < lengthQ) and valid):
				x = re.search(textQ[j], P)
				
				if (x == None):
					valid = False
				else:
					length += len(textQ[j])
					
					if (j != (lengthQ - 1)):
						length += 1
				
				j += 1
			
			percent[i] = float(length/lengthR)
		else:
			while ((j < lengthP) and valid):
				x = re.search(textP[j], T[i][0])
				
				if (x == None):
					valid = False
				else:
					length += len(textQ[j])
					
					if (j != (lengthP - 1)):
						length += 1
				
				j += 1
			
			percent[i] = float(length/lengthS)
		
		#if (((j == lengthP) or (j == lengthQ)) and valid):
		#	found = True
		#else:
			#i += 1
		i += 1
	
	if (found):
		return [i, percent]
	else:
		return [-1, percent]
