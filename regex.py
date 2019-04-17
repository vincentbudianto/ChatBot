from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re

def regex(T, P):
'''	factory = StopWordRemoverFactory()
	stopword = factory.create_stop_word_remover()
	cleanT = stopword.remove(T)
	cleanT = stopword.replace('?', '')'''
	stext = T.split()
	lengthP = len(P)
	lengthT = len(stext)
	found = False
	i = 0
	
	while ((i < lengthP) and not(found)):
		rtext = ''
		j = 0
		valid = True

		'''for j in range(lengthT):
			rtext += stext[j]
			
			if (j != (len(stext) - 1)):
				rtext += ' '
		print(rtext)'''

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
