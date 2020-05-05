def InterleaveBits(inArray,inter_len=90,numrows=10,numcols=9,rowinc=7,rowincmod=10,coldec=7,fetch_num=2):
	# Use an interleaving matrix to scramble the bit order.
	# MIL-STD-188-110 defines the interleave process as such:
	# Fill (0,0) of a 10 row x 9 col matrix with the first bit, then increment
	# the row by 7 mod 10. When that row is full, rotate the cols right once, and
	# repeat the process until the matrix is full. Once full, fetch the bits thusly:
	# Fetch the bit at (0,0). Then, move down one row, and right 2 mod 9 (described
	# in the paper as left 7 mod 9), and repeat until you reach the bottom of the matrix.
	# Go back to row 0, and a column to the right of the one you were at last time you were
	# at row 0; rinse and repeat until the matrix is empty again. Now to fill with more bits!
	bitIndex = 0
	row = 0
	col = 0
	inter_out = []
	temp = []
	print(fetch_num)
	interleave_matrix = initialize_matrix(None) # initialize vars
	for i in range(0,len(inArray),inter_len): # fill/fetch loop
		for i in range(numcols): # fill loop
			row = 0
			if ((bitIndex+rowincmod) >= len(inArray)):
				for j in range(bitIndex,len(inArray)): # row filling loop
					interleave_matrix[row][0] = inArray[j]
					row = (row+rowinc)%rowincmod
				for j in range(numrows): # column shifting loop
					interleave_matrix[j] = interleave_matrix[j][-1:] + interleave_matrix[j][:-1]
			else:
				for j in range(bitIndex,bitIndex+rowincmod): # row filling loop
					interleave_matrix[row][0] = inArray[j]
					row = (row+rowinc)%rowincmod
				for j in range(numrows): # column shifting loop
					interleave_matrix[j] = interleave_matrix[j][-1:] + interleave_matrix[j][:-1]
			bitIndex += rowincmod
		for i in range(inter_len): # bit fetching loop
			if fetch_num == 1:
				inter_out.append(temp)
				temp = []
			elif fetch_num == 2:
				if len(temp) < 2:
					temp.append(interleave_matrix[row][col])
				elif len(temp) == 2:
					inter_out.append(str(temp[0])+str(temp[1]))
					temp = []
				else:
					raise ValueError("Something went VERY WRONG1")
			elif fetch_num == 3:
				if len(temp) < 3:
					temp.append(interleave_matrix[row][col])
				elif len(temp) == 3:
					inter_out.extend(str(temp[0])+str(temp[1])+str(temp[2]))
					temp = []
				else:
					raise ValueError("Something went VERY WRONG2")
			row += 1
			if row == (numrows-1):
				row = 0
			elif row < (numrows-1):
				col = (col - coldec) % numcols
			else:
				raise ValueError("Math may be hard")
	return inter_out
