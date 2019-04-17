import re

text = input('Masukan input: ')
print(text)

stext = text.split()
length = len(stext)
print(stext)

rtext = ''
'''for i in range(length):
	rtext += stext[i]
	
	if (i != (len(stext) - 1)):
		rtext += ' '
print(rtext)'''

st = 'siapa saya?'

i = 0
valid = True
while ((i < length) and (valid)):
	rtext += stext[i]
	
	if (i != (len(stext) - 1)):
		rtext += ' '
	
	print(rtext)
	
	x = re.search(rtext, st)
	
	if (x == None):
		valid = False
		print('string not found')
	
	i += 1

if (valid):
	print('string found\n' + rtext)
