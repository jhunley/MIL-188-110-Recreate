import numpy as np
PreambleRandomizerSeq = [7, 4, 3, 0, 5, 1, 5, 0, 2, 2, 1, 1, 5, 7, 4, 3, 5, 0, 2, 6, 2, 1, 6, 2, 0, 0, 5, 0, 5, 2, 6, 6]

def PreambleGenerate(bps, interleave_len, dtyp = "Data"):
	if interleave_len == "Z" or interleave_len == "S":
		count = 2
		data_array = np.array([])
		while count >= 0:
			data_array = np.append(data_array, [0b000,0b001,0b011,0b000,0b001,0b011,0b001,0b010,0b000])
			if bps == 75:
				data_array = np.append(data_array, [0b111,0b101])
			elif bps == 150:
				data_array = np.append(data_array, [0b111,0b100])
			elif bps == 300:
				data_array = np.append(data_array, [0b110,0b111])
			elif bps == 600:
				data_array = np.append(data_array, [0b110,0b110])
			elif bps == 1200:
				data_array = np.append(data_array, [0b110,0b101])
			elif bps == 2400 and dtyp == "Data":
				data_array = np.append(data_array, [0b110,0b100])
			elif bps == 2400 and dtyp == "Voice":
				data_array = np.append(data_array, [0b111,0b111])
			elif bps == 4800:
				data_array = np.append(data_array, [0b111,0b110])
			else:
				raise Exception("Invalid input.")
			temp = bin(count)[2:].zfill(6)
			C1 = temp[:2]
			C2 = temp[2:4]
			C3 = temp[4:]
			if C1 == '00':
				C1 = 0b100
			elif C1 == '10':
				C1 = 0b101
			elif C1 == '01':
				C1 = 0b110
			elif C1 == '11':
				C1 = 0b111
			if C2 == '00':
				C2 = 0b100
			elif C2 == '10':
				C2 = 0b101
			elif C2 == '01':
				C2 = 0b110
			elif C2 == '11':
				C2 = 0b111
			if C3 == '00':
				C3 = 0b100
			elif C3 == '10':
				C3 = 0b101
			elif C3 == '01':
				C3 = 0b110
			elif C3 == '11':
				C3 = 0b111
			data_array = np.append(data_array, [C1, C2, C3, 0b000])
			count -= 1
	elif interleave_len == "L":
		count = 23
		data_array = np.array([])
		while count >= 0:
			data_array = np.append(data_array, [0b000,0b001,0b011,0b000,0b001,0b011,0b001,0b010,0b000])
			if bps == 75:
				data_array = np.append(data_array, [0b111,0b101])
			elif bps == 150:
				data_array = np.append(data_array, [0b111,0b100])
			elif bps == 300:
				data_array = np.append(data_array, [0b110,0b111])
			elif bps == 600:
				data_array = np.append(data_array, [0b110,0b110])
			elif bps == 1200:
				data_array = np.append(data_array, [0b110,0b101])
			elif bps == 2400 and dtyp == "Data":
				data_array = np.append(data_array, [0b110,0b100])
			elif bps == 2400 and dtyp == "Voice":
				data_array = np.append(data_array, [0b111,0b111])
			elif bps == 4800:
				data_array = np.append(data_array, [0b111,0b110])
			else:
				raise RuntimeError("Invalid input.")
			temp = bin(count)[2:].zfill(6)
			C1 = temp[:2]
			C2 = temp[2:4]
			C3 = temp[4:]
			if C1 == '00':
				C1 = 0b100
			elif C1 == '10':
				C1 = 0b101
			elif C1 == '01':
				C1 = 0b110
			elif C1 == '11':
				C1 = 0b111
			if C2 == '00':
				C2 = 0b100
			elif C2 == '10':
				C2 = 0b101
			elif C2 == '01':
				C2 = 0b110
			elif C2 == '11':
				C2 = 0b111
			if C3 == '00':
				C3 = 0b100
			elif C3 == '10':
				C3 = 0b101
			elif C3 == '01':
				C3 = 0b110
			elif C3 == '11':
				C3 = 0b111
			data_array = np.append(data_array, [C1, C2, C3, 0b000])
			count -= 1
	else:
		raise RuntimeError("Invalid input.")
	data_out = np.array([], dtype=int)
	for i in range(len(data_array)):
		if data_array[i] == 0:
			data_out = np.append(data_out, [0,0,0,0,0,0,0,0] * 4)
		elif data_array[i] == 1:
			data_out = np.append(data_out, [0,4,0,4,0,4,0,4] * 4)
		elif data_array[i] == 2:
			data_out = np.append(data_out, [0,0,4,4,0,0,4,4] * 4)
		elif data_array[i] == 3:
			data_out = np.append(data_out, [0,4,4,0,0,4,4,0] * 4)
		elif data_array[i] == 4:
			data_out = np.append(data_out, [0,0,0,0,4,4,4,4] * 4)
		elif data_array[i] == 5:
			data_out = np.append(data_out, [0,4,0,4,4,0,4,0] * 4)
		elif data_array[i] == 6:
			data_out = np.append(data_out, [0,0,4,4,4,4,0,0] * 4)
		elif data_array[i] == 7:
			data_out = np.append(data_out, [0,4,4,0,4,0,0,4] * 4)
	for i in range(len(data_out)):
		data_out[i] = (data_out[i] + PreambleRandomizerSeq[i % 32]) % 8
	return data_out
