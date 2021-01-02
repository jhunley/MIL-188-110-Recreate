import numpy as np
import scipy.io.wavfile as wavfile

x = np.arange(160)
x = x / 384000
f_c = 1800
tone0 = np.cos(2*np.pi*f_c*x)
tone1 = np.cos(2*np.pi*f_c*x+45)
tone2 = np.cos(2*np.pi*f_c*x+90)
tone3 = np.cos(2*np.pi*f_c*x+135)
tone4 = np.cos(2*np.pi*f_c*x+180)
tone5 = np.cos(2*np.pi*f_c*x+225)
tone6 = np.cos(2*np.pi*f_c*x+270)
tone7 = np.cos(2*np.pi*f_c*x+315)

def PreambleGenerate(data_array, bps, interleave_len, dtyp = "Data"):
	if interleave_len == "Z" or interleave_len == "S":
		count = 2
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
		return data_array
	elif interleave_len == "L":
		count = 23
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
		return data_array
	else:
		raise RuntimeError("Invalid input.")

