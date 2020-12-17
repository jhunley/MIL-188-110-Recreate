# MIL-188-110-Recreate
A recreation of the MIL-188-110 encoding scheme for HF digital data/voice transfer

The encoding steps are as follows:
Input string->EncodeText()->FECEncodeBits()->InterleaveBits()->MGD_Decode()->Scramble()->ConvertToTones()

You then manually run wavfile.write() (from scipy), so that you can choose your own save location.

Currently in the process of making the functions adaptable to all the different submodes (they are currently hardcoded to 75Bd, short interleave), as well as cleaning up the code and its inefficiencies.

-> Me, three years later: Well that was a lie


