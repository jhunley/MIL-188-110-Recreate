def convertToTones(message):
	# Ah, finally, the last step (almost). This is dead simple.
	# Had to do it this way because numpy append and concatenate is SO SLOOOW
        outsound = np.empty(len(message) * 160, dtype=np.float32)
        _len = 160
        for i in range(len(message)):
                if message[i] == 0:
                        outsound[i*_len:i*_len+_len] = tone0
                elif message[i] == 1:
                        outsound[i*_len:i*_len+_len] = tone1
                elif message[i] == 2:
                        outsound[i*_len:i*_len+_len] = tone2
                elif message[i] == 3:
                        outsound[i*_len:i*_len+_len] = tone3
                elif message[i] == 4:
                        outsound[i*_len:i*_len+_len] = tone4
                elif message[i] == 5:
                        outsound[i*_len:i*_len+_len] = tone5
                elif message[i] == 6:
                        outsound[i*_len:i*_len+_len] = tone6
                elif message[i] == 7:
                        outsound[i*_len:i*_len+_len] = tone7
        return outsound
