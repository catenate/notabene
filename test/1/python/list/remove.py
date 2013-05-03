list = ['a', 'bb', 'ccc', 'eeeee' ]
list.remove('a')
print list

list = ['a', 'bb', 'ccc', 'eeeee' ]
list.remove('ccc')
print list

list = ['a', 'bb', 'ccc', 'eeeee' ]
list.remove('eeeee')
print list

list = ['a', 'bb', 'ccc', 'eeeee' ]
list.remove('a')
list.remove('ccc')
list.remove('eeeee')
print list

delist = ['a', 'bb', 'ccc', 'eeeee']
list = ['a', 'bb', 'ccc', 'eeeee' ]
for l in delist:
	list.remove(l)
	print "list ", list
