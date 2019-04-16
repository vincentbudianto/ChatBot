def Boyer_Moore (T,P) :
	match = False
	m = len(P)
	n = len(T)
	i = m-1
	j = m-1
	count = 0
	
	while (i <= n-1 and not match) :
		if (T[i].lower() == P[j].lower()):
			count += 1
			if (j == 0) :
				match = True
			else :
				i = i-1
				j = j-1
		else :
			k = 0
			while (T[i].lower() != P[j].lower() and k < m):
				k = k+1
				j = j-1
			
			i = i+k+count
			count = 0
			j = m-1

	if (match):
		return i
	else:
		return -1
