
def Boyer_Moore (T,P) :

	match = False
	
	m = len(P)
	n = len(T)
	i = m-1
	j = m-1
	
	while (i <= n-1 and not match) :
		if (T[i].lower() == P[j].lower()):
			if (j == 0) :
				match = True
			else :
				i = i-1
				j = j-1
		else :
			k = 0
			while (T[i].lower() != P[j].lower() and k < m) :
				k = k+1
				j = j-1
			
			i = i+k
			j = m-1
	
		
	return match
			 

#------------
#---Test----
#------------

print("Masukkan Text: ")
T = str(input())
print("Masukkan Pattern: ")
P = str(input())

match = Boyer_Moore(T,P)

if (match):
	print("------>>Ketemu!!")
else:
	print("Kaga ketemu!!")

