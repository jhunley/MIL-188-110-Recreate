def TotalEncode(instring,Bd=75,BdType='Data',interleave_length='S'):
	if Bd == 75:
		if interleave_length == 'S':
			inter_len = 90
			numrows = 10
			numcols = 9
			rowinc = 7
			rowincmod = 10
			coldec = 7
			fetch_num = 2
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode75(inter_out)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync75s,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 720
			numrows = 20
			numcols = 36
			rowinc = 7
			rowincmod = 20
			coldec = 7
			fetch_num = 2
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode75(inter_out)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync75l,scrambld)
			outsound = convertToTones(message)
	if Bd == 150:
		if interleave_length == 'S':
			inter_len = 720
			numrows = 40
			numcols = 18
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync150s,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 5760
			numrows = 40
			numcols = 144
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync150l,scrambld)
			outsound = convertToTones(message)
	if Bd == 300:
		if interleave_length == 'S':
			inter_len = 720
			numrows = 40
			numcols = 18
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync300s,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 5760
			numrows = 40
			numcols = 144
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap =MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync300l,scrambld)
			outsound = convertToTones(message)
	if Bd == 600:
		if interleave_length == 'S':
			inter_len = 720
			numrows = 40
			numcols = 18
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap =MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync600s,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 5760
			numrows = 40
			numcols = 144
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode150_600(inter_out,inter_len,Bd)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync600l,scrambld)
			outsound = convertToTones(message)
	if Bd == 1200:
		if interleave_length == 'S':
			inter_len = 1440
			numrows = 40
			numcols = 36
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 2
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode1200(inter_out,interleave_length)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync1200s,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 11520
			numrows = 40
			numcols = 288
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 1
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode1200(inter_out,interleave_length)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync1200l,scrambld)
			outsound = convertToTones(message)
	if Bd == 2400 and BdType == 'Data':
		if interleave_length == 'S':
			inter_len = 2880
			numrows = 40
			numcols = 72
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 3
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode2400_4800(inter_out,interleave_length,inter_len,Bd,BdType)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync2400sd,scrambld)
			outsound = convertToTones(message)
		elif interleave_length == 'L':
			inter_len = 23040
			numrows = 40
			numcols = 576
			rowinc = 9
			rowincmod = 40
			coldec = 17
			fetch_num = 3
			indata = EncodeInputText(instring,inter_len)
			fec_out = FECEncodeBits(indata,Bd)
			inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
			datamap = MGD_Decode2400_4800(inter_out,interleave_length,inter_len,Bd,BdType)
			scrambld = ScrambleBits(datamap)
			message = messageCompose(scramsync2400ld,scrambld)
			outsound = convertToTones(message)
	if Bd == 2400 and BdType == 'Voice':
		inter_len = 2880
		numrows = 40
		numcols = 72
		rowinc = 9
		rowincmod = 40
		coldec = 17
		fetch_num = 3
		indata = EncodeInputText(instring,inter_len)
		fec_out = FECEncodeBits(indata,Bd)
		inter_out = InterleaveBits(fec_out,inter_len,numrows,numcols,rowinc,rowincmod,coldec,fetch_num)
		datamap = MGD_Decode2400_4800(inter_out,interleave_length,inter_len,Bd,BdType)
		scrambld = ScrambleBits(datamap)
		message = messageCompose(scramsync2400sv,scrambld)
		outsound = convertToTones(message)
	if Bd == 4800:
		inter_len = len(instring)
		indata = EncodeInputText(instring,inter_len)
		datamap = MGD_Decode2400_4800(inter_out,interleave_length,inter_len,Bd,BdType)
		scrambld = ScrambleBits(datamap)
		message = messageCompose(scramsync4800,scrambld)
		outsound = convertToTones(message)
	return outsound
