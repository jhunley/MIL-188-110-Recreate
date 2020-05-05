def convertToTones(message):
	outsound = np.array([None], dtype=np.float32)
	for i in range(len(message)):
		if message[i] == 0:
			outsound = np.concatenate([outsound, tone0])
		elif message[i] == 1:
			outsound = np.concatenate([outsound, tone1])
		elif message[i] == 2:
			outsound = np.concatenate([outsound, tone2])
		elif message[i] == 3:
			outsound = np.concatenate([outsound, tone3])
		elif message[i] == 4:
			outsound = np.concatenate([outsound, tone4])
		elif message[i] == 5:
			outsound = np.concatenate([outsound, tone5])
		elif message[i] == 6:
			outsound = np.concatenate([outsound, tone6])
		elif message[i] == 7:
			outsound = np.concatenate([outsound, tone7])
	outsound = np.delete(outsound, 0)
	return outsound
