def FECEncodeBits(inArray,Bd):
	# Returns a (much longer) FEC-encoded bit array from an input bit array
	# MIL-STD-188-110 specifies a scheme that returns two bits from every one
	# input bit. The even bits are encoded using x^6+x^4+x^3+x+1, and
	# the odd bits are encoded using x^6+x^5+x^4+x^3+1.
	fec_reg = [0, 0, 0, 0, 0, 0, 1] # Initialize the register
	x = 0 # initialize FEC output pointer
	if Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
		fec_out = [None]*(len(inArray)*2)
	elif Bd == 300:
		fec_out = [None]*(len(inArray)*4)
	elif Bd == 150:
		fec_out = [None]*(len(inArray)*8)
	elif Bd == 4800:
		return inArray
	for i in range(0, len(inArray)):
		fec_buffer[0] = inArray[i]
		if Bd == 150:
			fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
			fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
			fec_out[x+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
			fec_out[x+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
		elif Bd == 300:
			fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
			fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
		elif Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
			fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
			fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
		if Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
			x += 2
		elif Bd == 300:
			x += 4
		elif Bd == 150:
			x += 8
		fec_buffer[5] = fec_buffer[4]
		fec_buffer[4] = fec_buffer[3]
		fec_buffer[3] = fec_buffer[2]
		fec_buffer[2] = fec_buffer[1]
		fec_buffer[1] = fec_buffer[0]
	return fec_out
