#include <iostream>
#include <vector>
#include "Types.h"
#include "encodeInputText.h"
#include "fecEncodeBits.h"
//#include "interleaveBits.h"

int main()
{
	std::string in = "Hello, World!";
	std::vector<byte> datastream(in.begin(), in.end());

	size_t inter_len = 90;

	size_t bitlen = encodeInputText(&datastream, inter_len);

	bitlen = fecEncodeBits(&datastream, 75, bitlen);

	for (int i = 0; i < datastream.size(); i++)
	{
		std::cout << datastream[i];
	}

	std::cout << '\n';

	return 0;
}