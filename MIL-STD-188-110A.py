import numpy as np
import scipy.io.wavfile as wavfile
import PreambleGenerate
import EncodeInputText
import FECEncodeBits
import InterleaveBits
import channelMap
import ScrambleBits
import ConvertToTones

samplerate = 384000
PreambleRandomizerSeq = [7, 4, 3, 0, 5, 1, 5, 0, 2, 2, 1, 1, 5, 7, 4, 3, 5, 0, 2, 6, 2, 1, 6, 2, 0, 0, 5, 0, 5, 2, 6, 6]
tone0, tone1, tone2, tone3, tone4, tone5, tone6, tone7 = [], [], [], [], [], [], [], []
f_c = 1800
for i in range(160):
	tone0.append(np.cos(2*np.pi*f_c*i/samplerate))
	tone1.append(np.cos(2*np.pi*f_c*i/samplerate + 45))
	tone2.append(np.cos(2*np.pi*f_c*i/samplerate + 90))
	tone3.append(np.cos(2*np.pi*f_c*i/samplerate + 135))
	tone4.append(np.cos(2*np.pi*f_c*i/samplerate + 180))
	tone5.append(np.cos(2*np.pi*f_c*i/samplerate + 225))
	tone6.append(np.cos(2*np.pi*f_c*i/samplerate + 270))
	tone7.append(np.cos(2*np.pi*f_c*i/samplerate + 315))

def main(instring, Baud, interleave_length, Data_type, frequency_mode, EOMCycles):
        # The main wrapper function.
        # instring is any ASCII string. No limit on length, but untested.
        # Baud is the selected baud. You have 75-4800 Baud, by halves.
        # interleave_length is self-explanatory. You have zero, short, and long.
        # Data type is data or voice. Voice is untested, nor do I know what data
        # it would expect. Haven't read that.
        # frequency mode is fixed or hopping. Hopping isn't implemented.
        # If you don't know what to pick, go 75L.
        # Returns the waveform in a numpy array, ready to write to a sound file.

        baudList = [75, 150, 300, 600, 1200, 2400, 4800]
        baudList2 = ["75", "150", "300", "600", "1200", "2400", "4800"]
        interlenList = ["Z", "S", "L"]
        interlenList2 = ["z", "s", "l"]
        datalist = ["Data", "Voice"]
        frqmodelist = ["fixed", "hopping"]
        
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
                else interleave_length == "L"
        if interleave_length == "z":
                interset = "Z"
        elif interleave_length == "s":
                interset = "S"
        else interleave_length == "L"

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
        
        if interset == "Z":
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

        preamble_array = PreambleGenerate(Bd, interset, Data_type)
        indata = EncodeInputText(instring, inter_len, EOMCycles)
        fec_out = FECEncodeBits(indata, Bd, frequency_mode)
        inter_out = InterleaveData(fec_out, Bd, interset, frequency_mode)
        mgd_out = MGD_Decode(inter_out, Bd, frequency_mode)
        map_out = channelMap(mgd_out, Bd, interset, frequency_mode, Data_type)
        scramble_out = ScrambleBits(map_out)
        totalMap = np.append(preamble_array, scramble_out)
        outsound = convertToTones(totalMap)
        return outsound
