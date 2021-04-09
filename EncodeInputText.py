def EncodeInputText(instring, inter_len=90, EOMCycles=1):
	'''Converts an ASCII string to its bitwise representation and
	prepares it for the signal chain. inter_len describes the length
	in bits of a single interleaver chunk, which the output array should
	be a multiple of. EOMCycles is how many times the signal should
	send the EOM message before ending. This module should not be called
	by the user.'''
	
        asciitemp = []
        for char in instring:
                asciitemp.append(bin(ord(char))[2:].zfill(8))
        indata = []
        for i in range(len(asciitemp)):
                for bit in asciitemp[i]:
                        indata.append(int(bit))
        EOM = [0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1]
        for i in range(EOMCycles):
                indata.extend(EOM)
        indata.extend(([0]*144))
        if inter_len != 0:
                while ((len(indata)%inter_len)!=0):
                        indata.append(0)
        indata = np.array(indata, dtype=int)
        return indata
