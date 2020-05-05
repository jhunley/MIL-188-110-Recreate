def MGD_Decode150_600(inArray,interleave_length,inter_len,Bd):
	data_map = []
	if interleave_length == 'S':
		setlen = 45
	else:
		setlen = 360
	
	for i in range(len(inArray)): # converts Gray to symbols
		if inArray[i] == '0':
			data_map.append('0')
		elif inArray[i] == '1':
			data_map.append('4')
		if ((i % inter_len) == 0) and (i != 0):
			if Bd == 150:
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0440400400004444'*2)
				if interleave_length == 'L':
					data_map.extend('0'*11520)
					data_map.extend('0404404000004444'*2)
			if Bd == 300:
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0044440004404004'*2)
				if interleave_length == 'L':
					data_map.extend('0'*11520)
					data_map.extend('0000444404404004'*2)
			if Bd == 600:
				if interleave_length == 'S':
					data_map.extend('0'*1440)
					data_map.extend('0044440000444400'*2)
				if interleave_length == 'L':
					data_map.extend('0'*11520)
					data_map.extend('0000444400444400'*2)
	data_map2 = []
	for i in range(len(data_map)):
		for char in data_map[i]:
			data_map2.append(int(char))
	return data_map2
