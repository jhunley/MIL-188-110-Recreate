#include <iostream>
#include <vector>
#include "mgdDecode.h"
#include "Types.h"

void mgdDecode(std::vector<byte>* datastream, size_t baud, size_t bitlen)
{
	byte temp;
	size_t idx = 0;
	byte idxInc;

	switch (baud)
	{
	case 75:
	case 1200:
		idxInc = 2;
		break;

	case 2400:
	case 4800:
		idxInc = 3;
		break;

	default:
		return;
	}
	
	while ((idx + idxInc) < bitlen)
	{
		temp = (getBitVal(*datastream, idx)) << (idxInc - 1);

		if (idxInc == 3)
		{
			temp |= (getBitVal(*datastream, idx + 1) << 1);
		}

		temp |= getBitVal(*datastream, idx + (idxInc - 1));

		switch (temp)
		{
		case 0:
		case 1:
			break;

		case 2:
			temp = 3;
			break;

		case 3:
			temp = 2;
			break;

		case 4:
			temp = 7;
			break;

		case 5:
			temp = 6;
			break;

		case 6:
			temp = 4;
			break;

		case 7:
			temp = 5;
			break;

		default:
			std::cerr << "Invalid symbol detected in stream. This shouldn't be possible.\n\n";
			exit(1);
		}

		setBitVal(datastream, idx, (temp & (1 << idxInc)));

		if (idxInc == 3)
		{
			setBitVal(datastream, idx + 1, ((temp & 2) >> 1));
		}

		setBitVal(datastream, idx + idxInc, temp & 1);

		idx += idxInc;
	}

	return;
}