def FECEncodeBits(inArray,Bd,fqmode='fixed'):
	# Returns a (much longer) FEC-encoded bit array from an input bit array
	# inArray is the input bitstream
	# Bd is the selected baud
	# fqmode is whether we're operating serial or frequency hopping.
	# Frequency hopping is not supported at this time.
	# MIL-STD-188-110 specifies a scheme that returns two bits from every one
	# input bit. The even bits are encoded using x^6+x^4+x^3+x+1, and
	# the odd bits are encoded using x^6+x^5+x^4+x^3+1.
	# These bits are repeat coded depending on the selected mode.
        fec_buffer = [0, 0, 0, 0, 0, 0, 1] # Initialize the buffer
        x = 0 # initialize FEC output pointer
        if fqmode == 'fixed':
                if Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
                        fec_out = [None]*(len(inArray)*2)
                elif Bd == 300:
                        fec_out = [None]*(len(inArray)*4)
                elif Bd == 150:
                        fec_out = [None]*(len(inArray)*8)
                elif Bd == 4800:
                        return inArray # 4800-baud does not receive error correction
                for i in range(0, len(inArray)):
                        fec_buffer[0] = inArray[i]
                        if Bd == 150:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]   # The error correction is just a simple convolution.
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6] # There is probably a more efficient way to do this.
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 8
                        elif Bd == 300:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 4
                        elif Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 2
                        fec_buffer[5] = fec_buffer[4]
                        fec_buffer[4] = fec_buffer[3]
                        fec_buffer[3] = fec_buffer[2]
                        fec_buffer[2] = fec_buffer[1]
                        fec_buffer[1] = fec_buffer[0]
                fec_out = np.array(fec_out, dtype=int)
                return fec_out
        elif fqmode == 'hopping':
                if Bd == 75:
                        fec_out = [None]*(len(inArray)*16)
                elif Bd == 150:
                        fec_out = [None]*(len(inArray)*8)
                elif Bd == 300:
                        fec_out = [None]*(len(inArray)*4)
                elif Bd == 600 or Bd == 1200:
                        fec_out = [None]*(len(inArray)*2)
                elif Bd == 2400:
                        fec_out = [None]*((len(inArray)/2)*3)
                elif Bd == 4800:
                        return inArray
                for i in range(0, len(inArray)):
                        fec_buffer[0] = inArray[i]
                        if Bd == 75:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+8] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+9] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+10] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+11] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+12] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+13] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+14] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+15] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]                                
                                x += 16
                        elif Bd == 150:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 8
                        elif Bd == 300:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 4
                        elif Bd == 600 or Bd == 1200:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                x += 2
                        elif Bd == 2400:
                                fec_out[x] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                fec_out[x+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                                fec_out[x+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                                x += 3
                        fec_buffer[5] = fec_buffer[4]
                        fec_buffer[4] = fec_buffer[3]
                        fec_buffer[3] = fec_buffer[2]
                        fec_buffer[2] = fec_buffer[1]
                        fec_buffer[1] = fec_buffer[0]
                fec_out = np.array(fec_out, dtype=int)
                return fec_out
