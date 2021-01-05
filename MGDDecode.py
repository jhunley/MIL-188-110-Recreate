def MGD_Decode(indata, Bd):
    
    if (Bd == 75 or Bd == 1200):
        grouped = np.zeros([indata.shape[0]//2,],dtype=int)
        for i in range(0,len(indata),2):
            grouped[i//2] = int(str(indata[i]) + str(indata[i+1]), base=2)
        out = np.zeros(grouped.shape,dtype=int)
        for i, el in enumerate(grouped):
            if el == 0:
                out[i] = el
            elif el == 1:
                out[i] = el
            elif el == 2:
                out[i] = 3
            elif el == 3:
                out[i] = 2
            else:
                raise RuntimeError("Invalid symbol in bitstream.")
        return out
    elif (Bd == 150 or Bd == 300 or Bd == 600):
        out = np.zeros(indata.shape,dtype=int)
        for i in range(len(indata)):
            out[i] = int(str(indata[i]),base=2)
        return out
    elif (Bd == 2400 or Bd == 4800):
        grouped = np.zeros([indata.shape[0]//3,],dtype=int)
        for i in range(0,len(indata),3):
            grouped[i//3] = int(str(indata[i]) + str(indata[i+1]) + str(indata[i+2]), base=2)
        out = np.zeros(grouped.shape,dtype=int)
        for i, el in enumerate(grouped):
            if el == 0:
                out[i] = el
            elif el == 1:
                out[i] = el
            elif el == 2:
                out[i] = 3
            elif el == 3:
                out[i] = 2
            elif el == 4:
                out[i] = 7
            elif el == 5:
                out[i] = 6
            elif el == 6:
                out[i] = 4
            elif el == 7:
                out[i] = 5
            else:
                raise RuntimeError("Invalid symbol in bitstream.")
    else:
        raise RuntimeError("Invalid input.")
    
    
