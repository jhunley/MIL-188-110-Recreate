#include <iostream>
#include <vector>
#include "Types.h"
#include "encodeInputText.h"
#include "fecEncodeBits.h"
#include "interleaveBits.h"
#include "mgdDecode.h"
#include "ScrambleBits.h"
#include "PreambleGenerate.h"
#include "AddStream.h"
#include "channelMap.h"

int main()
{
	std::string in = "Hello, World!";
	std::vector<byte> datastream(in.begin(), in.end());
	std::vector<byte> preamble_stream;
	std::vector<byte> out_stream;

	size_t inter_len = 90;

	size_t plen = preambleGenerate(&preamble_stream, 75, _short, data);

	size_t bitlen = encodeInputText(&datastream, inter_len, 1);

	bitlen = fecEncodeBits(&datastream, 75, bitlen);

	interleave_data(&datastream, 75, _short, bitlen);

	bitlen = mgdDecode(&datastream, 75, bitlen);

	bitlen = channelMap(&datastream, bitlen, 75, _short, data);

	scrambleData(&datastream, bitlen, dscramble_pattern, 60);

	plen = addStreams(&out_stream, &preamble_stream, 0, plen);

	size_t outlen = addStreams(&out_stream, &datastream, plen, bitlen);

	for (int i = 0; i < out_stream.size(); i++)
	{
		std::cout << out_stream[i];
	}

	std::cout << '\n';

	return 0;
}
