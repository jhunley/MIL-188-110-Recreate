#ifndef _FECENCODEBITS_H
#define _FECENCODEBITS_H

#include <vector>
#include "Types.h"

size_t fecEncodeBits(std::vector<byte>* datastream, size_t baud, size_t bitlen);

#endif
