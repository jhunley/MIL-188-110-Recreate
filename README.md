# MIL-188-110-Recreate
A recreation of the MIL-188-110 encoding scheme for HF digital data/voice transfer

The encoding steps are as follows:
PreambleGenerate() + Input string -> EncodeInputText() -> FECEncodeBits() -> InterleaveBits() -> MGD_Decode() -> channelMap() -> Scramble() -> append -> ConvertToTones()

All you have to do is:
open a shell in the file directory
```py
import MIL-STD-188-110A
instring = "Hello, World!"
outsound = main(instring, 75, "L", "Data", "fixed", 1)
wavfile.write("/dir/here/filename.wav", 384000, outsound)
```
You then manually run wavfile.write() (from scipy), so that you can choose your own save location.

The current code is capable of fixed-frequency text encoding, and it produces audio that sounds right, though I don't have a way of testing a decode.
The code SHOULD run, but could probably be implemented better.

-------------------------------------------------------------------------------------

The C++ code, on the other hand, is not complete, will not run (yet), and could almost DEFINITELY be done a lot better.
For both languages, PLEASE MAKE SUGGESTIONS AND COMMENTS
I DON'T KNOW IF I'M DOING SOMETHING REAL BAD UNLESS IT IMMEDIATELY BREAKS SOMETHING
I AM A HUGE BEGINNER
HELP NEEDED

-------------------------------------------------------------------------------------

The standard used is available here: https://www.sigidwiki.com/images/c/c8/MIL-STD-188_110C_CHG_NOTICE-1.pdf
