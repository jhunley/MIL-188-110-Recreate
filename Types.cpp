#include <iostream>
#include <vector>
#include "Types.h"

byte getBitVal(std::vector<byte> stream, size_t idx)
{
	if (idx < 0 || idx > (stream.size() * 8))
	{
		std::cerr << "FEC index out of bounds. (getBitVal)\n\n";
		std::cerr << "stream:\n";
		for (size_t i = 0; i < stream.size(); i++)
		{
			std::cerr << stream[i];
		}
		std::cerr << "\n\n";

		std::cerr << "idx: " << idx << "\n\n";
		exit(1);
	}

	int byteidx = idx / 8;
	byte bitidx = idx % 8;

	byte tmp = stream[byteidx];

	byte result = tmp & (0x80 >> bitidx);

	return (result >> (7 - bitidx));
}

void setBitVal(std::vector<byte>* stream, size_t idx, byte val)
{
	if ((idx < 0) || (idx >= stream->size() * 8))
	{
		std::cerr << "FEC index out of bounds. (getBitVal)\n\n";
		std::cerr << "stream:\n";
		for (size_t i = 0; i < stream->size(); i++)
		{
			std::cerr << stream->at(i);
		}
		std::cerr << "\n\n";

		std::cerr << "idx: " << idx << "\n\n";
		exit(1);
	}

	int byteidx = idx / 8;
	byte bitidx = idx % 8;

	byte tmp = stream->at(byteidx);

	byte setmask = ~(0x80 >> bitidx);

	val <<= (7 - bitidx);

	if (val == 0)
		tmp &= setmask;
	else
		tmp |= val;

	stream->at(byteidx) = tmp;

	return;
}

byte unaryXOR(byte val)
{
	byte result = 0;
	while (val)
	{
		result ^= val & 1;
		val >>= 1;
	}

	return result;
}
