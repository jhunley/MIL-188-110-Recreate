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

	encodeInputText(&datastream, inter_len);

	fecEncodeBits(&datastream, 75);

	for (int i = 0; i < datastream.size(); i++)
	{
		std::cout << datastream[i];
	}

	std::cout << '\n';

	return 0;
}