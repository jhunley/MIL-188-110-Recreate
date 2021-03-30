#include <algorithm>
#include <iostream>
#include <vector>
#include "Types.h"
#include "interleaveBits.h"

void interleave_chunk(std::vector<byte>* chunk, size_t numrows, size_t numcols)
{
	if (chunk->size() != (numcols * numrows))
	{
		std::cerr << "The input chunk doesn't fit in the interleave matrix. How did you do this?\n\n";
		exit(1);
	}

	size_t i = 0, rownum = 0, colnum = 0;
	std::vector<byte> temp(chunk->size()), out(chunk->size());

	while (i < (numrows * numcols))
	{
		size_t count = 0;

		while (count < numrows)
		{
			setBitVal(&temp, (colnum + numcols * rownum), getBitVal(*chunk, i));
			rownum = (rownum + 7) % numrows;
			count++; i++;
		}

		rownum = 0;
		colnum++;
	}

	i = 0;
	rownum = 0;
	colnum = 0;
	size_t lastcolnum;

	while (i < (numcols * numrows))
	{
		lastcolnum = colnum;

		while (rownum < numrows)
		{
			setBitVal(&out, i, getBitVal(temp, (colnum + numcols * rownum)));
			rownum++;
			colnum = (colnum - 7) % numcols;
			i++;
		}

		rownum = 0;
		colnum = lastcolnum + 1;

	}
}

void interleave_data(std::vector<byte>* datastream, size_t baud, interleave_len chunklen)
{
	size_t numrows, numcols;

	switch (baud)
	{
	case 150:
	case 300:
	case 600:
	{
		switch (chunklen)
		{
		case _zero:
			return;

		case _short:
			numcols = 18;
			numrows = 40;
			break;

		case _long:
			numcols = 144;
			numrows = 40;
			break;
		}
		break;
	}

	case 75:
	{
		switch (chunklen)
		{
		case _zero:
			return;

		case _short:
			numcols = 9;
			numrows = 10;
			break;

		case _long:
			numcols = 36;
			numrows = 20;
			break;
		}
		break;
	}

	case 1200:
	{
		switch (chunklen)
		{
		case _zero:
			return;

		case _short:
			numcols = 36;
			numrows = 40;
			break;

		case _long:
			numcols = 288;
			numrows = 40;
			break;
		}
		break;
	}

	case 2400:
	{
		switch (chunklen)
		{
		case _zero:
			return;

		case _short:
			numcols = 72;
			numrows = 40;
			break;

		case _long:
			numcols = 576;
			numrows = 40;
			break;
		}
		break;
	}

	default:
		return;
	}

	size_t z = numcols * numrows;

	if ((datastream->size() % z) != 0)
	{
		std::cerr << "The input data does not fit evenly into the interleaver. Check upstream! (interleave_data)\n\n";
		exit(1);
	}

	std::vector<byte> temp(z);

	for (size_t i = 0; i < datastream->size() * 8; i += z)
	{
		temp = std::vector<byte>(datastream->begin() + i, datastream->begin() + i + z);
		interleave_chunk(&temp, numrows, numcols);
		std::copy(std::begin(temp), std::end(temp), std::begin(*datastream) + i);
	}

	return;
}