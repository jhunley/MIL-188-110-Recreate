#include <iostream>
#include <algorithm>
#include <vector>
#include "Types.h"
#include "encodeInputText.h"

void encodeInputText(std::vector<byte>* datastream, size_t inter_len)
{
	size_t arlen = datastream->size();

	size_t additionalEl = 0;

	while ((arlen + 40 + 144 + additionalEl) % inter_len != 0)
	{
		additionalEl++;
	}
	size_t outlen = (arlen + 40 + 144 + (additionalEl / 8)) * sizeof(byte);

	datastream->insert(datastream->end(), &EOM[0], &EOM[39]);

	datastream->resize(outlen);

	return;
}