'''
FINDLIST = file containing concept (expressed by one or more words) to be found (one concept per line) 
REPLACELIST = file containing concept (expressed by one or more words) that will be substituted to those on findlist (one concept per line)
F = file in which find and replace concept
FW = file in which store the result of find and replace
'''


''' Remove the \n terminator from a list of string '''
def removen(l,lun):
	for i in range(0,lun):
		l[i] = l[i].rstrip('\n')

''' Tokenize appropriately a line of f file '''		
def tokenizeline(l):
	l1 = l.split(',')
	l1[-1] = l1[-1].rstrip('\n')
	return l1

''' Write in the FW file the correct string '''
def writesub(el,lun):
	for i in range(0,lun):
		if el == fl[i]:
			el = rl[i]
			break
	fw.write(el)
		
''' Open the files '''
findlist = open('/home/andrea/Desktop/find','r')
replacelist = open('/home/andrea/Desktop/replace','r')
f = open('/home/andrea/Desktop/list','r')
fw = open('/home/andrea/Desktop/listm','w')

''' Tokenize the files '''
fl = list(findlist)
rl = list(replacelist)
lun = len(fl)
removen(fl,lun)
removen(rl,lun)

''' Find and replace '''
for line in f:
	l1 = tokenizeline(line)
	for el in l1:
		writesub(el,lun)
		fw.write(',')
	fw.write('\n')

''' Close all the files '''
findlist.close()
replacelist.close()
f.close()
fw.close()
