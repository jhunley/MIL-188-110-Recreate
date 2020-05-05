def FECEncodeBits(inArray):
	# Returns a (much longer) FEC-encoded bit array from an input bit array
	# MIL-STD-188-110 specifies a scheme that returns two bits from every one
	# input bit. The even bits are encoded using x^6+x^4+x^3+x+1, and
	# the odd bits are encoded using x^6+x^5+x^4+x^3+1.
	fec_reg = [0, 0, 0, 0, 0, 0, 1] # Initialize the register
	x = 0 # initialize FEC output pointer
	fec_out = [None]*(len(inArray)*2)
	for i in range(0, len(inArray)):
		fec_buffer[0] = inArray[i]
		fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
		fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
		x += 2
		fec_buffer[5] = fec_buffer[4]
		fec_buffer[4] = fec_buffer[3]
		fec_buffer[3] = fec_buffer[2]
		fec_buffer[2] = fec_buffer[1]
		fec_buffer[1] = fec_buffer[0]
	return fec_out
