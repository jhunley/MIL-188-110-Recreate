def MGD_Decode1200(inArray,interleave_length):
	# Modified Gray Decodes the input data into symbols ready to scramble
	mgd = []
	if interleave_length == 'S':
		inter_len = 1440
	else:
		inter_len = 11520
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
		if mgd[i] == '00':
			data_map.append('0')
		elif mgd[i] == '01':
			data_map.append('2')
		elif mgd[i] == '10':
			data_map.append('4')
		elif mgd[i] == '11':
			data_map.append('6')
		if ((i % inter_len) == 0) and (i != 0):
			if interleave_length == 'S':
				data_map.extend('0'*1440)
				data_map.extend('0044440004044040'*2)
			if interleave_length == 'L':
				data_map.extend('0'*11520)
				data_map.extend('0000444404044040'*2)
	data_map2 = []
	for i in range(len(data_map)):
		for char in data_map[i]:
			data_map2.append(int(char))
	return data_map2
