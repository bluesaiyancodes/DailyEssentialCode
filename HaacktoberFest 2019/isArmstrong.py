def is_armstrong(n):
	m=0
	t=n
	#flag = False
	while n>0:
		r=(n%10)
		#m += r ** 3
		m=m+(r*r*r)
		n=n/10
	print m
	if m==t:
		#flag = True
		print "Yes it is armstrong"
	'''else:
		print "Not it is not armstrong"'''
	return flag
is_armstrong(153)
