def MGD_Decode2400_4800(inArray):
	# Modified Gray Decodes the input data into symbols ready to scramble
	mgd = []
	for i in range(len(inArray)): # converts binary to Gray
		if inArray[i] == '000':
			mgd.append('000')
		elif inArray[i] == '001':
			mgd.append('001')
		elif inArray[i] == '010':
			mgd.append('011')
		elif inArray[i] == '011':
			mgd.append('010')
		elif inArray[i] == '100':
			mgd.append('110')
		elif inArray[i] == '101':
			mgd.append('110')
		elif inArray[i] == '110':
			mgd.append('100')
		elif inArray[i] == '111':
			mgd.append('101')
	data_map = []
	for i in range(len(mgd)): # converts Gray to symbols
		if i % (32*45) == 0: #use exceptional set
			if mgd[i] == '000':
				data_map.append('0')
			elif mgd[i] == '001':
				data_map.append('1')
			elif mgd[i] == '010':
				data_map.append('2')
			elif mgd[i] == '011':
				data_map.append('3')
			if mgd[i] == '100':
				data_map.append('4')
			elif mgd[i] == '101':
				data_map.append('5')
			elif mgd[i] == '110':
				data_map.append('6')
			elif mgd[i] == '111':
				data_map.append('7')
	data_map2 = []
	for i in range(len(data_map)):
		for char in data_map[i]:
			data_map2.append(int(char))
	return data_map2
