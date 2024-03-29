#ifndef _ENCODEINPUTTEXT_H
#define _ENCODEINPUTTEXT_H

#include "Types.h"

// EOM is a bytestream containing the End-Of-Message bytes contained in every transmission.
static const byte EOM[] = { 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b,
			    0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b,
			    0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b,
			    0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b, 0x4b };


/*
	encodeInputText() is a function takes a vector with an input message
	and in-place prepares it for the encoding chain, returning the length
	of the resulting stream in bits (because it doesn't return full bytes).
*/
size_t encodeInputText(std::vector<byte>* datastream, size_t inter_len);

#endif
