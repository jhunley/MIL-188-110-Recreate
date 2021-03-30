#ifndef _INTERLEAVE_BITS_H
#define _INTERLEAVE_BITS_H

#include <vector>
#include "Types.h"

enum interleave_len
{
	_zero,
	_short,
	_long
};

interleave_len length = _short;

void interleave_data(std::vector<byte>* datastream, size_t baud, interleave_len chunklen);
void interleave_chunk(std::vector<byte>* chunk, size_t numrows, size_t numcols);

#endif