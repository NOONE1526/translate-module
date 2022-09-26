def translate(data):
	forlist = []
	translated = []
	translate = {'q':'й','w':'ц','e':'у','r':'к','t':'е','y':'н','u':'г','i':'ш',
	'o':'щ','p':'з','a':'ф','s':'ы','d':'в','f':'а','g':'п','h':'р','j':'о','k':'л',
	'l':'д','z':'я','x':'ч','c':'с','v':'м','b':'и','n':'т','m':'ь'}
	for i in data:
			forlist.append(i)
	try:
		for i in forlist:
			translated.append(translate[i])
		print(''.join(translated))
	except:
		pass
	try:
		for i in forlist:
			translated.append(list(translate.keys())[list(translate.values()).index(i)])
		print(''.join(translated))
	except:
		pass
		
