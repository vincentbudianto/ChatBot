import re

def regex(T, P):
	stext = P.split()
	lengthP = len(stext)
	lengthT = len(stext)
	found = False
	i = 0
	rtext = ''

	while ((i < lengthT) and not(found)):
		j = 0
		valid = True

		while ((j < lengthP) and (valid)):
			rtext += stext[j]

			if (j != (len(stext) - 1)):
				rtext += ' '
			
			x = re.search(rtext, P)
			
			if (x == None):
				valid = False
			
			j += 1
		
		if (j == lengthP):
			found = True
			
		i += 1
	
	if (found):
		return x.span()[1]
	else:
		return -1
