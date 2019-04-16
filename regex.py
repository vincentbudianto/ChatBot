from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re

def regex(T, P):
	stext = T.split()
	lengthP = len(P)
	lengthT = len(stext)
	found = False
	i = 0
	
	rtext = ''
	while ((i < lengthP) and not(found)):
		print(rtext)
		j = 0
		valid = True

		while ((j < lengthT) and (valid)):
			rtext += stext[j]
			
			if (j != (len(stext) - 1)):
				rtext += ' '
			
			x = re.search(rtext, P)
			
			if (x == None):
				valid = False
			
			j += 1
		
		if (j == lengthT):
			found = True
			
		i += 1
	
	if (found):
		return i
	else:
		return -1
