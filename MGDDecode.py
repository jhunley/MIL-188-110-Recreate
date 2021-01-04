def MGD_Decode(indata, Bd):
    
    if (Bd == 75 or Bd == 1200):
        group = 2
        grouped = np.zeros([indata.shape[0]//2,])
        
    elif (Bd == 150 or Bd == 300 or Bd == 600):
        group = 1
        out = np.zeros(indata.shape)
    elif (Bd == 2400 or Bd == 4800):
        group = 3
        out = np.zeros([indata.shape[0]//3,])
    else:
        raise RuntimeError("Invalid input.")
    
    
