lnum = [15, 23, 16, 42, 4, 8]
numlist = []

def find_lowest(numlist):
	lowest=lnum[0]
	for x in lnum:
		if(x<lowest):
			lowest=x
	
	return lowest

while(len(lnum)>0):
	x = find_lowest(lnum)
	lnew.append (x)
	lnum.remove (x)

print lnew

	
