def InterleaveChunk(inchunk, numrows, numcols):
	'''Interleave the input data. You shouldn't be calling this function manually.'''
	
	if len(inchunk) != (numrows * numcols):
		raise RuntimeError("The input chunk doesn't fit in the interleave matrix.")
	i = 0
	rownum = 0
	colnum = 0
	temp = np.zeros(x.shape)
	out = np.zeros(x.shape)

	while i < numrows * numcols:
		count = 0
		while count < numrows:
			temp[colnum + numcols * rownum] = inchunk[i]
			rownum = (rownum + 7) % numrows
			count += 1
			i += 1
		rownum = 0
		colnum += 1

	i = 0
	rownum = 0
	colnum = 0
	del count

	while i < numrows * numcols:
		lastcolnum = colnum
		while rownum < numrows:
			out[i] = temp[colnum + numcols * rownum]
			rownum += 1
			colnum = (colnum - 7) % numcols
			i += 1
		rownum = 0
		colnum = lastcolnum + 1
		lastcolnum = colnum
	return out

def InterleaveData(indata, Bd=75, interleave_len="S"):
	'''Chunkwise interleave the input data.'''
	if interleave_len == "Z":
		return inchunk
	elif Bd == 75 and interleave_len == "S":
		numrows = 10
		numcols = 9
	elif Bd == 75 and interleave_len == "L":
		numrows = 20
		numcols = 36
	elif (Bd == 150 or Bd == 300 or Bd == 600) and interleave_len == "S":
		numrows = 40
		numcols = 18
	elif (Bd == 150 or Bd == 300 or Bd == 600) and interleave_len == "L":
		numrows = 40
		numcols = 144
	elif Bd == 1200 and interleave_len == "S":
		numrows = 40
		numcols = 36
	elif Bd == 1200 and interleave_len == "L":
		numrows = 40
		numcols = 288
	elif Bd == 2400 and interleave_len == "S":
		numrows = 40
		numcols = 72
	elif Bd == 2400 and interleave_len == "L":
		numrows = 40
		numcols = 576
	else:
		raise RuntimeError("Invalid input.")
	
	z = numrows * numcols
	
	out = np.zeros(indata.shape)
	
	if (len(indata) % z) != 0:
		raise RuntimeError("The input data does not evenly fit in the interleaver. Something is VERY wrong.")
	
	for i in range(0,len(indata),z):
		temp = indata[i:i+z]
		temp = InterleaveChunk(temp,numrows,numcols)
		out[i:i+z] = temp
	return out
