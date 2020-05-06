def MGD_Decode2400_4800(inArray,interleave_length,inter_len,Bd,BdType):
	data_map = []
	if interleave_length == 'S':
		setlen = 45
	else:
		setlen = 360
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
		if mgd[i] == '000':
			data_map.append('0')
		elif mgd[i] == '001':
			data_map.append('1')
		elif mgd[i] == '010':
			data_map.append('2')
		elif mgd[i] == '011':
			data_map.append('3')
		elif mgd[i] == '100':
			data_map.append('4')
		elif mgd[i] == '101':
			data_map.append('5')
		elif mgd[i] == '110':
			data_map.append('6')
		elif mgd[i] == '111':
			data_map.append('7')
		if ((i % inter_len) == 0) and (i != 0):
			if Bd == 2400 and BdType == 'Data':
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0044440000004444'*2)
				if interleave_length == 'L':
					data_map.extend('0'*11520)
					data_map.extend('0000444400004444'*2)
			if Bd == 2400 and BdType == 'Voice':
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0440400404404004'*2)
				if interleave_length == 'L':
					raise ValueError("Only Short interleave is allowed for Secure Voice")
			if Bd == 4800:
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0440400400444400'*2)
				if interleave_length == 'L':
					raise ValueError("Only Short interleave is supported for 4800Bd")
	data_map2 = []
	for i in range(len(data_map)):
		for char in data_map[i]:
			data_map2.append(int(char))
	return data_map2
