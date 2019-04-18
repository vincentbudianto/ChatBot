import re

def regex(T, P):
	stext = P.split()
	lengthP = len(stext)
	lengthT = len(T)
	found = False
	i = 0

	while ((i < lengthT) and not(found)):
		j = 0
		rtext = ''
		valid = True
		
		while ((j < lengthP) and (valid)):
			rtext += stext[j]
			
			if (j != (len(stext) - 1)):
				rtext += ' '
			
			x = re.search(rtext, T[i][0])
			
			if (x == None):
				valid = False
			else:
				j += 1
		
		if (j == lengthP):
			found = True
		else:
			i += 1
	
	if (found):
		return i
	else:
		return -1
