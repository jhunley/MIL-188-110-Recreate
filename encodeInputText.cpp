#include <iostream>
#include <algorithm>
#include <vector>
#include "Types.h"
#include "encodeInputText.h"

size_t encodeInputText(std::vector<byte>* datastream, size_t inter_len)
{
	size_t arlen = datastream->size();
	size_t bitlen = arlen * 8 + 320 + 144;

	size_t additionalEl = 0;

	while ((bitlen + additionalEl) % inter_len != 0)
	{
		additionalEl++;
	}
	size_t outlen = ((bitlen + additionalEl) / 8) + (((bitlen + additionalEl) % 8 != 0) ? 1 : 0);
	bitlen += additionalEl;

	datastream->insert(datastream->end(), &EOM[0], &EOM[39]);

	datastream->resize(outlen);

	return bitlen;
}
