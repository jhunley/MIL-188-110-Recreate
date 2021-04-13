#ifndef _CHANNEL_MAP_H
#define _CHANNEL_MAP_H

#include <iostream>
#include <vector>
#include "Types.h"

size_t channelMap(std::vector<byte>* datastream, size_t bitlen, int Baud, interleave_len inter_len, data_type dtype);

#endif
