import numpy as np
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

PreambleRandomizerSeq = [7, 4, 3, 0, 5, 1, 5, 0, 2, 2, 1, 1, 5, 7, 4, 3, 5, 0, 2, 6, 2, 1, 6, 2, 0, 0, 5, 0, 5, 2, 6, 6]

def PreambleGenerate(bps, interleave_len, dtyp="Data"):
    # The first step in the process chain.
    # Creates a specific symbol pattern based on the selected inputs,
    # and then XOR scrambles it with a pattern specific to the preamble (above
    # list).
    # The returned numpy array does not get used until much later in the chain,
    # where it gets a massive tail.

    if interleave_len == "Z" or interleave_len == "S":
        # All cases where the user selects short interleave get two cycles of the preamble sequence,
        # otherwise they get 23
        count = 2

        data_array = np.array([])

        while count > 0:

            data_array = np.append(data_array, [0b000,0b001,0b011,0b000,0b001,0b011,0b001,0b010,0b000]) # [0, 1, 3, 0, 1, 3, 1, 2, 0] begins all preambles

            if bps == 75:
                data_array = np.append(data_array, [0b111,0b101]) # This tells the receiving modem the selected baud rate

            elif bps == 150:
                data_array = np.append(data_array, [0b111,0b100])

            elif bps == 300:
                data_array = np.append(data_array, [0b110,0b111])

            elif bps == 600:
                data_array = np.append(data_array, [0b110,0b110])

            elif bps == 1200:
                data_array = np.append(data_array, [0b110,0b101])

            elif bps == 2400 and dtyp == "Data":
                data_array = np.append(data_array, [0b110,0b100]) # and selected data type, as needed

            elif bps == 2400 and dtyp == "Voice":
                data_array = np.append(data_array, [0b111,0b111])

            elif bps == 4800:
                data_array = np.append(data_array, [0b111,0b110])

            else:
                raise Exception("Invalid input.") # Always with the input checks!

            temp = bin(count)[2:].zfill(6) # The standard specifies including the count number, split into three two-bit groups, each offset by 4.
            # This is why I went for this while loop.

            C1 = temp[:2]
            C2 = temp[2:4]
            C3 = temp[4:]

            if C1 == '00':
                C1 = 0b100 # GIVE ME MY GODDAMN SWITCH CASE STATEMENTS

            elif C1 == '10':
                C1 = 0b101

            elif C1 == '01':
                C1 = 0b110

            elif C1 == '11':
                C1 = 0b111

            if C2 == '00':
                C2 = 0b100

            elif C2 == '10':
                C2 = 0b101

            elif C2 == '01':
                C2 = 0b110

            elif C2 == '11':
                C2 = 0b111

            if C3 == '00':
                C3 = 0b100

            elif C3 == '10':
                C3 = 0b101

            elif C3 == '01':
                C3 = 0b110

            elif C3 == '11':
                C3 = 0b111

            data_array = np.append(data_array, [C1, C2, C3, 0b000])

            count -= 1

    elif interleave_len == "L":
        # And here's the other case!

        count = 23

        data_array = np.array([])

        while count >= 0:

            data_array = np.append(data_array, [0b000,0b001,0b011,0b000,0b001,0b011,0b001,0b010,0b000]) # Same as above

            if bps == 75:
                data_array = np.append(data_array, [0b111,0b101])

            elif bps == 150:
                data_array = np.append(data_array, [0b111,0b100])

            elif bps == 300:
                data_array = np.append(data_array, [0b110,0b111])

            elif bps == 600:
                data_array = np.append(data_array, [0b110,0b110])

            elif bps == 1200:
                data_array = np.append(data_array, [0b110,0b101])

            elif bps == 2400 and dtyp == "Data":
                data_array = np.append(data_array, [0b110,0b100])

            elif bps == 2400 and dtyp == "Voice":
                data_array = np.append(data_array, [0b111,0b111])

            elif bps == 4800:
                data_array = np.append(data_array, [0b111,0b110])

            else:
                raise RuntimeError("Invalid input.")

            temp = bin(count)[2:].zfill(6)
            C1 = temp[:2]
            C2 = temp[2:4]
            C3 = temp[4:]

            if C1 == '00':
                C1 = 0b100

            elif C1 == '10':
                C1 = 0b101

            elif C1 == '01':
                C1 = 0b110

            elif C1 == '11':
                C1 = 0b111

            if C2 == '00':
                C2 = 0b100

            elif C2 == '10':
                C2 = 0b101

            elif C2 == '01':
                C2 = 0b110

            elif C2 == '11':
                C2 = 0b111

            if C3 == '00':
                C3 = 0b100

            elif C3 == '10':
                C3 = 0b101

            elif C3 == '01':
                C3 = 0b110

            elif C3 == '11':
                C3 = 0b111

            data_array = np.append(data_array, [C1, C2, C3, 0b000])
            count -= 1

    else:
        raise RuntimeError("Invalid input.")

    # Almost there!
    # Now we need to map the symbols above to their final channel symbols, before we then scramble them!
    # This gives the preamble its distinctive tone
    # Each number from 0 to 7 at this point and beyond corresponds to a point counterclockwise around the 8-PSK circle

    data_out = np.array([], dtype=int)

    for i in range(len(data_array)):
        if data_array[i] == 0:
            data_out = np.append(data_out, [0,0,0,0,0,0,0,0] * 4)

        elif data_array[i] == 1:
            data_out = np.append(data_out, [0,4,0,4,0,4,0,4] * 4)

        elif data_array[i] == 2:
            data_out = np.append(data_out, [0,0,4,4,0,0,4,4] * 4)

        elif data_array[i] == 3:
            data_out = np.append(data_out, [0,4,4,0,0,4,4,0] * 4)

        elif data_array[i] == 4:
            data_out = np.append(data_out, [0,0,0,0,4,4,4,4] * 4)

        elif data_array[i] == 5:
            data_out = np.append(data_out, [0,4,0,4,4,0,4,0] * 4)

        elif data_array[i] == 6:
            data_out = np.append(data_out, [0,0,4,4,4,4,0,0] * 4)

        elif data_array[i] == 7:
            data_out = np.append(data_out, [0,4,4,0,4,0,0,4] * 4)

        # and now for the actual scramble! Technically there's some junk involving a GLFSR
        # in the original specification, but it just results in the stuff we do below.

    for i in range(len(data_out)):
        data_out[i] = (data_out[i] + PreambleRandomizerSeq[i % 32]) % 8

    return data_out

def EncodeInputText(instring, inter_len=90, EOMCycles=1):
    ''' Converts an ASCII string to its bitwise representation and
    prepares it for the signal chain.
    instring is the ASCII string you wish to encode.
    inter_len describes the length in bits of a single interleaver chunk,
    which the output array should be a multiple of.
    EOMCycles is how many times the signal should send the EOM message before ending.
    This module returns a numpy array of ints, each int holding one bit of data.
    Yes. That is gross. Deal with it.
    This module should not be called by the user.'''

    asciitemp = []
    for char in instring:
        asciitemp.append(bin(ord(char))[2:].zfill(8))
    indata = []
    for i in range(len(asciitemp)):
        for bit in asciitemp[i]:
            indata.append(int(bit))
    EOM = [0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1]
    for i in range(EOMCycles):
        indata.extend(EOM)
    indata.extend(([0]*144))
    if inter_len != 0:
        while ((len(indata)%inter_len)!=0):
            indata.append(0)
    indata = np.array(indata, dtype=int)
    return indata

def FECEncodeBits(inArray,Bd,fqmode='fixed'):
    '''Convulutional forward error-correction module with optional repeat coding.
    MIL-STD-188-110 specifies a scheme that returns two bits from every one
    input bit. The even bits are encoded using x^6+x^4+x^3+x+1, and
    the odd bits are encoded using x^6+x^5+x^4+x^3+1.
    The specific encoding is selected with Bd and fqmode.
    This module should not be called by the user.'''

    fec_buffer = [0, 0, 0, 0, 0, 0, 1] # Initialize the buffer. The LSB is always set.
    optr = 0 # initialize FEC output pointer

    if fqmode == 'fixed':

        if Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75: # Choose output encoding
            fec_out = [None]*(len(inArray)*2)

        elif Bd == 300:
            fec_out = [None]*(len(inArray)*4)

        elif Bd == 150:
            fec_out = [None]*(len(inArray)*8)

        elif Bd == 4800: # 4800-baud doesn't get encoded
            return inArray

        for i in range(0, len(inArray)): # now we start churning!
            fec_buffer[0] = inArray[i] # Start by loading a bit in the buffer

            if Bd == 150:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6] # Naive repeat coding by literally repeating it
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 8

            elif Bd == 300:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 4

            elif Bd == 600 or Bd == 1200 or Bd == 2400 or Bd == 75:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 2

            fec_buffer[5] = fec_buffer[4] # And shift!
            fec_buffer[4] = fec_buffer[3]
            fec_buffer[3] = fec_buffer[2]
            fec_buffer[2] = fec_buffer[1]
            fec_buffer[1] = fec_buffer[0]

        fec_out = np.array(fec_out, dtype=int) # cast to a numpy array
        return fec_out # and get out of here

    elif fqmode == 'hopping': # same as above
        if Bd == 75:
            fec_out = [None]*(len(inArray)*16)

        elif Bd == 150:
            fec_out = [None]*(len(inArray)*8)

        elif Bd == 300:
            fec_out = [None]*(len(inArray)*4)

        elif Bd == 600 or Bd == 1200:
            fec_out = [None]*(len(inArray)*2)

        elif Bd == 2400:
            fec_out = [None]*((len(inArray)/2)*3) # Except here we "puncture code" by omitting every fourth bit, yielding a 2/3 code

        elif Bd == 4800:
            return inArray

        for i in range(0, len(inArray)):
            fec_buffer[0] = inArray[i]

            if Bd == 75:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+8] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+9] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+10] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+11] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+12] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+13] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+14] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+15] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]                
                optr += 16

            elif Bd == 150:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+4] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+5] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+6] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+7] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 8

            elif Bd == 300:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+3] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 4

            elif Bd == 600 or Bd == 1200:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                optr += 2

            elif Bd == 2400:
                fec_out[optr] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                fec_out[optr+1] = fec_buffer[0] ^ fec_buffer[1] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[6]
                fec_out[optr+2] = fec_buffer[0] ^ fec_buffer[2] ^ fec_buffer[3] ^ fec_buffer[5] ^ fec_buffer[6]
                optr += 3

            fec_buffer[5] = fec_buffer[4]
            fec_buffer[4] = fec_buffer[3]
            fec_buffer[3] = fec_buffer[2]
            fec_buffer[2] = fec_buffer[1]
            fec_buffer[1] = fec_buffer[0]

        fec_out = np.array(fec_out, dtype=int)
        return fec_out

def InterleaveChunk(inchunk, numrows, numcols, rowInc,colDec):
    '''Interleave the input data. You shouldn't be calling this function manually.
    The standard calls for a dual-matrix buffer approach (in hardware):
    Load each bit in a certain pattern to the load buffer, the unload in a different pattern.
    Do this every so many bits (a buffer length) over the entire data.'''
    
    if len(inchunk) != (numrows * numcols): # more bounds checking!
        raise RuntimeError("The input chunk doesn't fit in the interleave matrix.")

    idx = 0 # multi-purpose index used for both loading and fetching.
    rownum = 0 # row index
    colnum = 0 # column index
    temp = np.zeros(inchunk.shape) # temporary store buffer
    out = np.zeros(inchunk.shape) # and the output buffer

    while idx < numrows * numcols:
        count = 0 # We use this variable because our rownum is preoccupied with other math; while rownum may wrap around (multiple times), we still need to load a full row

        while count < numrows:
            temp[colnum + numcols * rownum] = inchunk[idx]

            rownum = (rownum + rowInc) % numrows # aformentioned other math
            count += 1
            idx += 1

        rownum = 0
        colnum += 1

    idx = 0 # reset the indices for the fetching loop
    rownum = 0
    colnum = 0
    del count # not needed anymore, might as well get rid of it now

    while idx < numrows * numcols: # and now we do pretty much the same thing as before, but in a different order.
        lastcolnum = colnum

        while rownum < numrows:
            out[idx] = temp[colnum + numcols * rownum]

            rownum += 1
            colnum = (colnum - colDec) % numcols
            idx += 1

        rownum = 0
        colnum = lastcolnum + 1
        lastcolnum = colnum
    return out

def InterleaveData(indata, Bd=75, interleave_len="S", frqmode="fixed"):
    '''Chunkwise interleave the input data.
    indata contains the bit array that needs interleaved.
    Bd, interleave_len, and frqmode are mode selector switches.
    Will only run if the length of the input is evenly divisible by
    chunk size.'''

    if interleave_len == "Z": # pretty self-explanatory
        return indata

    elif Bd == 75 and interleave_len == "S" and frqmode == "fixed":
        numrows = 10 # number of rows in the matrix
        numcols = 9 # number of columns in the matrix
        rowInc = 7 # how far we move through rows
        colDec = 7 # how far we move through columns

    elif Bd == 75 and interleave_len == "L" and frqmode == "fixed":
        numrows = 20
        numcols = 36
        rowInc = 7
        colDec = 7

    elif Bd == 75 and interleave_len == "S" and frqmode == "hopping":
        numrows = 40
        numcols = 18
        rowInc = 9
        colDec = 17

    elif Bd == 75 and interleave_len == "L" and frqmode == "hopping":
        numrows = 40
        numcols = 144
        rowInc = 9
        colDec = 17

    elif (Bd == 150 or Bd == 300 or Bd == 600) and interleave_len == "S":
        numrows = 40
        numcols = 18
        rowInc = 9
        colDec = 17

    elif (Bd == 150 or Bd == 300 or Bd == 600) and interleave_len == "L":
        numrows = 40
        numcols = 144
        rowInc = 9
        colDec = 17

    elif Bd == 1200 and interleave_len == "S":
        numrows = 40
        numcols = 36
        rowInc = 9
        colDec = 17

    elif Bd == 1200 and interleave_len == "L":
        numrows = 40
        numcols = 288
        rowInc = 9
        colDec = 17

    elif Bd == 2400 and interleave_len == "S":
        numrows = 40
        numcols = 72
        rowInc = 9
        colDec = 17

    elif Bd == 2400 and interleave_len == "L":
        numrows = 40
        numcols = 576
        rowInc = 9
        colDec = 17

    elif Bd == 4800: # 4800-baud doesn't get encoded
        return indata

    else:
        raise RuntimeError("Invalid input.")
    
    interlen = numrows * numcols

    if Bd == 2400 and frqmode == 'hopping': # need an extra temp to do the special puncture coding for this config
        tmpout = np.zeros(indata.shape)
        out = np.array([])
    else:
        out = np.zeros(indata.shape)
    
    if (len(indata) % interlen) != 0:
        raise RuntimeError("The input data does not evenly fit in the interleaver. Something is VERY wrong.")
    
    for i in range(0,len(indata),interlen):
        temp = indata[i:i+interlen] # snip a chunk

        temp = InterleaveChunk(temp,numrows,numcols,rowInc,colDec) # interleave it

        if Bd == 2400 and frqmode == 'hopping':
            tmpout[i:i+interlen] = temp
        else:
            out[i:i+interlen] = temp # and put it away

        if Bd == 2400 and frqmode == 'hopping': # or puncture it, if applicable. Another 2/3 encoding, which means 3/4 bits for some reason.
            for i in range(len(tmpout)):
                if i % 4 != 3:
                    out.append(tmpout[i])

    out = np.array(out, dtype=int)
    return out

def MGD_Decode(indata, Bd, frqmode):
    '''Convert the input bitstream to Gray form and group them up, depending on mode.
    We use Gray code because if we accidentally ID a symbol wrong, we'll only be wrong by one bit,
    making recovery much easier.'''

    if ((Bd == 75 and frqmode == 'fixed') or Bd == 1200): # 75 baud and 1200 baud use identical codings here.
        grouped = np.zeros([indata.shape[0]//2,],dtype=int) # Because we're grouping the input into two bits, the output is going to be half as long.

        for i in range(0,len(indata),2): # Start by actually grouping the bits.
            grouped[i//2] = int(str(indata[i]) + str(indata[i+1]), base=2)

        out = np.zeros(grouped.shape,dtype=int)

        for i, el in enumerate(grouped): # Then go through the groups and modulate them.
            if el == 0:
                out[i] = 0

            elif el == 1:
                out[i] = 1

            elif el == 2:
                out[i] = 3

            elif el == 3:
                out[i] = 2

            else:
                raise RuntimeError("Invalid symbol in bitstream.")

        return out # And we're done!

    elif (Bd == 150 or Bd == 300 or Bd == 600 or (Bd == 75 and frqmode == 'hopping')): # These modes just pass through (nearly) unchanged. They take polar opposite sides of the phase circle.
        out = np.zeros(indata.shape,dtype=int)

        for i in range(len(indata)):
            if indata[i] == 0:
                out[i] = 0

            elif indata[i] == 1:
                out[i] = 4

        return out

    elif (Bd == 2400 or Bd == 4800): # And here we group by threes.
        grouped = np.zeros([indata.shape[0]//3,],dtype=int)

        for i in range(0,len(indata)-1,3):
            grouped[i//3] = int(str(indata[i]) + str(indata[i+1]) + str(indata[i+2]), base=2)

        out = np.zeros(grouped.shape,dtype=int)

        for i, el in enumerate(grouped):
            if el == 0:
                out[i] = 0

            elif el == 1:
                out[i] = 1

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

        return out

    else:
        raise RuntimeError("Invalid input.")

def channelMap(indata, Bd, inter_len, frqmode, data_type):
    '''Map MGD groups to their final form as channel symbols.
    This is what I am most unsure about so far.
    I cannot guarantee I interpreted the standards document correctly.
    Every symbol after this point directly correlates to a position on the phase circle.'''

    if frqmode == 'fixed':
        if Bd == 75: # 75-baud is special, in that it does not get any known data probes,
                     # but it does get special Walsh modulation that alternates between two forms every lenMod symbols (one set)

            if inter_len == "Z" or inter_len == "S":
                lenMod = 45

            elif inter_len == "L":
                lenMod = 360

            map_out = [] # stores the output symbols

            for i in range(len(indata)):
                if ((i % lenMod == 0) and (i != 0)): # The normal form
                    if indata[i] == 0:
                        map_out += [0,0,0,0] * 8

                    elif indata[i] == 1:
                        map_out += [0,4,0,4] * 8

                    elif indata[i] == 2:
                        map_out += [0,0,4,4] * 8

                    elif indata[i] == 3:
                        map_out += [0,4,4,0] * 8

                    else:
                        raise RuntimeError("Invalid symbol in stream.")

                else: # The special form
                    if indata[i] == 0:
                        map_out += [0,0,0,0,4,4,4,4] * 4

                    elif indata[i] == 1:
                        map_out += [0,4,0,4,4,0,4,0] * 4

                    elif indata[i] == 2:
                        map_out += [0,0,4,4,4,4,0,0] * 4

                    elif indata[i] == 3:
                        map_out += [0,4,4,0,4,0,0,4] * 4

                    else:
                        raise RuntimeError("Invalid symbol in stream.")

            map_out = np.array(map_out)
            return map_out

        elif Bd == 150 or Bd == 300 or Bd == 600: # These modes don't get repeat coding
            unknownMod = 20 # how much unknown data to send between data probes
            map_out = [] # ouput array
            i = 0 # index
            affecting = False # Whether we're sending a probe

            while (i < len(indata)):
                if affecting == False:
                    for j in range(i,i + unknownMod): # send unknown data without repeat coding
                        if indata[j] == 0:
                            map_out += [0]

                        elif indata[j] == 1:
                            map_out += [4]

                        else:
                            raise RuntimeError("Invalid symbol in stream.")

                    i += unknownMod
                    affecting = True # and toggle
                else: # A known data probe is composed of two symbols that tells the radio what mode is being sent, and corrects for doppler effects
                      # These are the same symbols from the preamble.
                    if Bd == 150:
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,4,4,0,4,0,0,4] * 2 
                            D2 = [0,0,0,0,4,4,4,4] * 2

                        elif inter_len == "L":
                            D1 = [0,4,0,4,4,0,4,0] * 2
                            D2 = [0,0,0,0,4,4,4,4] * 2

                    elif Bd == 300:
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,0,4,4,4,4,0,0] * 2
                            D2 = [0,4,4,0,4,0,0,4] * 2

                        elif inter_len == "L":
                            D1 = [0,0,0,0,4,4,4,4] * 2
                            D2 = [0,4,4,0,4,0,0,4] * 2

                    elif Bd == 600:
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,0,4,4,4,4,0,0] * 2
                            D2 = [0,0,4,4,4,4,0,0] * 2

                        elif inter_len == "L":
                            D1 = [0,0,0,0,4,4,4,4] * 2
                            D2 = [0,0,4,4,4,4,0,0] * 2

                    map_out = map_out + D1 + D2 + [0, 0, 0, 0] # The known symbol count for these modes is 20. The standard just pads zeros to the 16 above symbols.
                    affecting = False # and toggle

            map_out = np.array(map_out)
            return map_out

        elif Bd == 1200: # same concept as above, except with pseudo-4PSK
            unknownMod = 20
            map_out = []
            i = 0
            affecting = False

            while (i < len(indata)):
                if affecting == False:
                    for j in range(i,i + unknownMod):
                        if indata[j] == 0:
                            map_out += [0]

                        elif indata[j] == 1:
                            map_out += [2]

                        elif indata[j] == 2:
                            map_out += [4]

                        elif indata[j] == 3:
                            map_out += [6]

                        else:
                            raise RuntimeError("Invalid symbol in stream.")
                    i += unknownMod
                    affecting = True

                else:
                    if inter_len == "Z" or inter_len == "S":
                        D1 = [0,0,4,4,4,4,0,0] * 2
                        D2 = [0,4,0,4,4,0,4,0] * 2

                    elif inter_len == "L":
                        D1 = [0,0,0,0,4,4,4,4] * 2
                        D2 = [0,4,0,4,4,0,4,0] * 2
                        
                    map_out = map_out + D1 + D2 + [0, 0, 0, 0]
                    affecting = False

            map_out = np.array(map_out)
            return map_out

        elif Bd == 2400 or Bd == 4800: # Slightly different here: We send more unknown data at a time, and also less known data (16 instead of 20 symbols)
            unknownMod = 32
            map_out = []
            i = 0
            affecting = False

            while (i < len(indata)):
                if affecting == False:
                    for j in range(i,i + unknownMod): # Also we just send the data through raw to scramble
                        try:
                            map_out += [indata[j]]
                        except:
                            pass
                    i += unknownMod
                    affecting = True
                else:
                    if Bd == 2400 and data_type == "Data":
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,0,4,4,4,4,0,0] * 2
                            D2 = [0,0,0,0,4,4,4,4] * 2

                        elif inter_len == "L":
                            D1 = [0,0,0,0,4,4,4,4] * 2
                            D2 = [0,0,0,0,4,4,4,4] * 2
                            
                    elif Bd == 2400 and data_type == "Voice":
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,4,4,0,4,0,0,4] * 2
                            D2 = [0,4,4,0,4,0,0,4] * 2
                            
                        elif inter_len == "L":
                            raise RuntimeError("Invalid input.")

                    elif Bd == 4800:
                        if inter_len == "Z" or inter_len == "S":
                            D1 = [0,4,4,0,4,0,0,4] * 2
                            D2 = [0,0,4,4,4,4,0,0] * 2
                            
                        elif inter_len == "L":
                            raise RuntimeError("Invalid input.")

                    map_out = map_out + D1 + D2
                    affecting = False

            map_out = np.array(map_out)
            return map_out

def ScrambleBits(inArray):
    '''Just a simple XOR, to make the data appear 8-PSK.
    We're almost done!'''

    scramble_out = [4, 1, 0, 2, 2, 1, 5, 4, 3, 6, 6, 2, 2, 4, 4, 2, 6, 0, 5, 1, 3, 6, 6, 2, 5, 1, 0, 3, 3, 1, 7, 1, 0, 2, 7, 5, 0, 1, 4, 3, 5, 1, 1, 5, 6, 7, 3, 7, 5, 1, 0, 4, 1, 0, 2, 5, 4, 1, 5, 6, 7, 4, 2, 1, 0, 5, 5, 3, 0, 1, 1, 5, 6, 0, 6, 3, 4, 4, 1, 6, 1, 3, 6, 4, 3, 4, 5, 2, 7, 2, 2, 7, 4, 3, 0, 7, 2, 4, 1, 1, 1, 4, 7, 0, 4, 6, 7, 0, 0, 1, 3, 6, 6, 5, 0, 5, 1, 6, 2, 3, 7, 2, 4, 3, 0, 0, 0, 5, 4, 5, 5, 7, 5, 3, 3, 3, 1, 2, 5, 5, 7, 0, 0, 3, 2, 7, 2, 7, 4, 4, 2, 6, 7, 0, 5, 2, 3, 7, 0, 5]
    scramble_temp = scramble_out
    while (len(scramble_temp) < len(inArray)): # Repeat the above scramble pattern until it's longer than the input array (to be replaced with something actually smart)
        scramble_temp.extend(scramble_out)

    scrambld = []
    for i in range(len(inArray)): # do the thing
        scrambld.append(inArray[i] ^ scramble_temp[i])

    scrambld = np.array(scrambld, dtype=int)
    return scrambld

samplerate = 384000 # Minimum samplerate needed to not distort the tones, found by experiment
tone0, tone1, tone2, tone3, tone4, tone5, tone6, tone7 = [], [], [], [], [], [], [], [] # 8-PSK signal, need 8 tones of constant frequency but differing phase
f_c = 1800 # Baseband frequency of signal

for i in range(160): # Init
    tone0.append(np.cos(2*np.pi*f_c*i/samplerate))
    tone1.append(np.cos(2*np.pi*f_c*i/samplerate + 45))
    tone2.append(np.cos(2*np.pi*f_c*i/samplerate + 90))
    tone3.append(np.cos(2*np.pi*f_c*i/samplerate + 135))
    tone4.append(np.cos(2*np.pi*f_c*i/samplerate + 180))
    tone5.append(np.cos(2*np.pi*f_c*i/samplerate + 225))
    tone6.append(np.cos(2*np.pi*f_c*i/samplerate + 270))
    tone7.append(np.cos(2*np.pi*f_c*i/samplerate + 315))


def convertToTones(message): # Simple loop
    outsound = np.empty(len(message) * 160, dtype=np.float32) # Need to pre-allocate array, because numpy append is really nasty slow, and so is Python's at this point
    _len = 160 # Length of a symbol

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

def main(instring, Baud, interleave_length, Data_type, frequency_mode, EOMCycles):
    '''The main wrapper function.
    instring is any ASCII string. No limit on length, but untested.
    Baud is the selected baud. You have 75-4800 Baud, by halves.
    interleave_length is self-explanatory. You have zero, short, and long.
    Data type is data or voice. Voice is untested, nor do I know what data
    it would expect. Haven't read that.
    frequency mode is fixed or hopping. Hopping isn't implemented.
    If you don't know what to pick, go 75L.
    Returns the waveform in a numpy array (samplerate 384000, mono, float), ready to write to a sound file.'''

    baudList = [75, 150, 300, 600, 1200, 2400, 4800] # available bauds, in int and text form
    baudList2 = ["75", "150", "300", "600", "1200", "2400", "4800"]

    interlenList = ["Z", "S", "L"] # available interleave lengths
    interlenList2 = ["z", "s", "l"]

    datalist = ["Data", "Voice"] # data modes
    frqmodelist = ["fixed", "hopping"] # frequency modes
        
    if instring == "":
        print("No input. Not tested.")

    if Baud not in baudList:
        if Baud not in baudList2:
            raise ValueError("Invalid baud setting detected.")
        Bd = int(Baud)
    else:
        Bd = Baud

    if interleave_length not in interlenList:
        if interleave_length not in interlenList2:
            raise ValueError("Invalid interleave setting detected.")
        if interleave_length == "z":
            interset = "Z"
        elif interleave_length == "s":
            interset = "S"
        else:
            interset = "L"
    if interleave_length == "z":
        interset = "Z"
    elif interleave_length == "s":
        interset = "S"
    else:
        interset = "L"

    if Data_type not in datalist:
        raise ValueError("Invalid data setting detected.")
    if Data_type == "Voice":
        print("Voice input is not tested.")

    if frequency_mode not in frqmodelist:
        raise ValueError("Invalid frequency mode setting detected.")
    if frequency_mode == "hopping":
        raise RuntimeError("Frequency hopping mode is not supported at this time.")

    if type(EOMCycles) != int:
        raise RuntimeError("EOMCycles expects an integer.")
        
    if interset == "Z": # Now we load inter_len for EncodeInputText(); it is the length of a single interleaver chunk in bits
        inter_len = 0

    elif interset == "S":
        if Bd == 75:
            inter_len = 90

        elif (Bd == 150 or Bd == 300 or Bd == 600):
            inter_len = 720

        elif Bd == 1200:
            inter_len = 1440

        elif Bd == 2400:
            inter_len = 2880

        elif Bd == 4800:
            inter_len = 0

    elif interset == "L":
        if Bd == 75:
            inter_len = 720

        elif (Bd == 150 or Bd == 300 or Bd == 600):
            inter_len = 5760

        elif Bd == 1200:
            inter_len = 11520

        elif Bd == 2400:
            inter_len = 23040

        elif Bd == 4800:
            inter_len = 0

    # And now we start chugging!
    preamble_array = PreambleGenerate(Bd, interset, Data_type)
    indata = EncodeInputText(instring, inter_len, EOMCycles)
    fec_out = FECEncodeBits(indata, Bd, frequency_mode)
    inter_out = InterleaveData(fec_out, Bd, interset, frequency_mode)
    mgd_out = MGD_Decode(inter_out, Bd, frequency_mode)
    map_out = channelMap(mgd_out, Bd, interset, frequency_mode, Data_type)
    scramble_out = ScrambleBits(map_out)
    totalMap = np.append(preamble_array, scramble_out)
    outsound = convertToTones(totalMap)

    # And finally, we correct the bandwidth (3kHz, centered on 1800 Hz)
    outsound = butter_lowpass_filter(outsound, 3300, samplerate, order=1)
    outsound = butter_highpass_filter(outsound, 300, samplerate, order=1)

    return outsound
