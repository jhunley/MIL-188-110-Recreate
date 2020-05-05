def MGD_Decode75_1200(inArray):
	# Modified Gray Decodes the input data into symbols ready to scramble
	mgd = []
	for i in range(len(inArray)): # converts binary to Gray
		if inArray[i] == '00':
			mgd.append('00')
		elif inArray[i] == '01':
			mgd.append('01')
		elif inArray[i] == '10':
			mgd.append('11')
		elif inArray[i] == '11':
			mgd.append('10')
	data_map = []
	for i in range(len(mgd)): # converts Gray to symbols
		if i % 33 == 0: #use exceptional set
			if mgd[i] == '00':
				data_map.append('0000')
				data_map.append('4444')
			elif mgd[i] == '01':
				data_map.append('0404')
				data_map.append('4040')
			elif mgd[i] == '10':
				data_map.append('0044')
				data_map.append('4400')
			elif mgd[i] == '11':
				data_map.append('0440')
				data_map.append('4004')
		else: # use normal set
			if mgd[i] == '00':
				data_map.append('0000')
			elif mgd[i] == '01':
				data_map.append('0404')
			elif mgd[i] == '10':
				data_map.append('0044')
			elif mgd[i] == '11':
				data_map.append('0440')
	data_map2 = []
	for i in range(len(data_map)):
		for char in data_map[i]:
			data_map2.append(int(char))
	return data_map2
