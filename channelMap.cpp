#include <iostream>
#include <vector>
#include "Types.h"
#include "channelMap.h"
#include "AddStream.h"

size_t channelMap(std::vector<byte>* datastream, size_t bitlen, int Baud, interleave_len inter_len, data_type dtype)
{
	size_t lenMod, outlen = 0, unknownMod, i = 0;
	byte temp;
	std::vector<byte> map_out, D1, D2;
	bool affecting = false;

	switch (Baud)
	{
	case 75:
	{
		switch (inter_len)
		{
		case _zero:
		case _short:
		{
			lenMod = 45;
			break;
		}

		case _long:
		{
			lenMod = 360;
			break;
		}
		}

		for (i = 0; i < bitlen / 3; i += 3)
		{
			if ((i % lenMod == 0) && (i != 0))
			{
				temp = (getBitVal(*datastream, i) << 2) + (getBitVal(*datastream, i + 1) << 1) + (getBitVal(*datastream, i + 2));
				switch (temp)
				{
				case 0:
				{
					outlen += 96;
					map_out.resize(((outlen) / 8) + ((outlen % 8 != 0) ? 1 : 0));
					break;
				}

				case 1:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 3, 1);
					setBitVal(&map_out, outlen + 9, 1);
					setBitVal(&map_out, outlen + 15, 1);
					setBitVal(&map_out, outlen + 21, 1);
					setBitVal(&map_out, outlen + 27, 1);
					setBitVal(&map_out, outlen + 33, 1);
					setBitVal(&map_out, outlen + 39, 1);
					setBitVal(&map_out, outlen + 45, 1);
					setBitVal(&map_out, outlen + 51, 1);
					setBitVal(&map_out, outlen + 57, 1);
					setBitVal(&map_out, outlen + 63, 1);
					setBitVal(&map_out, outlen + 69, 1);
					setBitVal(&map_out, outlen + 75, 1);
					setBitVal(&map_out, outlen + 81, 1);
					setBitVal(&map_out, outlen + 87, 1);
					setBitVal(&map_out, outlen + 93, 1);
					outlen += 96;
					break;
				}

				case 2:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 6, 1);
					setBitVal(&map_out, outlen + 9, 1);
					setBitVal(&map_out, outlen + 18, 1);
					setBitVal(&map_out, outlen + 21, 1);
					setBitVal(&map_out, outlen + 30, 1);
					setBitVal(&map_out, outlen + 33, 1);
					setBitVal(&map_out, outlen + 42, 1);
					setBitVal(&map_out, outlen + 45, 1);
					setBitVal(&map_out, outlen + 54, 1);
					setBitVal(&map_out, outlen + 57, 1);
					setBitVal(&map_out, outlen + 66, 1);
					setBitVal(&map_out, outlen + 69, 1);
					setBitVal(&map_out, outlen + 78, 1);
					setBitVal(&map_out, outlen + 81, 1);
					setBitVal(&map_out, outlen + 90, 1);
					setBitVal(&map_out, outlen + 93, 1);
					outlen += 96;
					break;
				}

				case 3:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 3, 1);
					setBitVal(&map_out, outlen + 6, 1);
					setBitVal(&map_out, outlen + 15, 1);
					setBitVal(&map_out, outlen + 18, 1);
					setBitVal(&map_out, outlen + 27, 1);
					setBitVal(&map_out, outlen + 30, 1);
					setBitVal(&map_out, outlen + 39, 1);
					setBitVal(&map_out, outlen + 42, 1);
					setBitVal(&map_out, outlen + 51, 1);
					setBitVal(&map_out, outlen + 54, 1);
					setBitVal(&map_out, outlen + 63, 1);
					setBitVal(&map_out, outlen + 66, 1);
					setBitVal(&map_out, outlen + 75, 1);
					setBitVal(&map_out, outlen + 78, 1);
					setBitVal(&map_out, outlen + 87, 1);
					setBitVal(&map_out, outlen + 90, 1);
					outlen += 96;
					break;
				}

				default:
				{
					std::cerr << "Bad symbol in MGD stream!\n";
					exit(-1);
				}
				}
			}
			else
			{
				temp = (getBitVal(*datastream, i) << 2) + (getBitVal(*datastream, i + 1) << 1) + (getBitVal(*datastream, i + 2));
				switch (temp)
				{
				case 0:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 12, 1);
					setBitVal(&map_out, outlen + 15, 1);
					setBitVal(&map_out, outlen + 18, 1);
					setBitVal(&map_out, outlen + 21, 1);
					setBitVal(&map_out, outlen + 36, 1);
					setBitVal(&map_out, outlen + 39, 1);
					setBitVal(&map_out, outlen + 32, 1);
					setBitVal(&map_out, outlen + 45, 1);
					setBitVal(&map_out, outlen + 60, 1);
					setBitVal(&map_out, outlen + 63, 1);
					setBitVal(&map_out, outlen + 66, 1);
					setBitVal(&map_out, outlen + 69, 1);
					setBitVal(&map_out, outlen + 84, 1);
					setBitVal(&map_out, outlen + 87, 1);
					setBitVal(&map_out, outlen + 90, 1);
					setBitVal(&map_out, outlen + 93, 1);
					outlen += 96;
					break;
				}

				case 1:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 3, 1);
					setBitVal(&map_out, outlen + 9, 1);
					setBitVal(&map_out, outlen + 12, 1);
					setBitVal(&map_out, outlen + 18, 1);
					setBitVal(&map_out, outlen + 27, 1);
					setBitVal(&map_out, outlen + 33, 1);
					setBitVal(&map_out, outlen + 36, 1);
					setBitVal(&map_out, outlen + 42, 1);
					setBitVal(&map_out, outlen + 51, 1);
					setBitVal(&map_out, outlen + 57, 1);
					setBitVal(&map_out, outlen + 60, 1);
					setBitVal(&map_out, outlen + 66, 1);
					setBitVal(&map_out, outlen + 75, 1);
					setBitVal(&map_out, outlen + 81, 1);
					setBitVal(&map_out, outlen + 84, 1);
					setBitVal(&map_out, outlen + 90, 1);
					outlen += 96;
					break;
				}

				case 2:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 6, 1);
					setBitVal(&map_out, outlen + 9, 1);
					setBitVal(&map_out, outlen + 12, 1);
					setBitVal(&map_out, outlen + 15, 1);
					setBitVal(&map_out, outlen + 30, 1);
					setBitVal(&map_out, outlen + 33, 1);
					setBitVal(&map_out, outlen + 36, 1);
					setBitVal(&map_out, outlen + 39, 1);
					setBitVal(&map_out, outlen + 54, 1);
					setBitVal(&map_out, outlen + 57, 1);
					setBitVal(&map_out, outlen + 60, 1);
					setBitVal(&map_out, outlen + 63, 1);
					setBitVal(&map_out, outlen + 78, 1);
					setBitVal(&map_out, outlen + 81, 1);
					setBitVal(&map_out, outlen + 84, 1);
					setBitVal(&map_out, outlen + 87, 1);
					outlen += 96;
					break;
				}

				case 3:
				{
					map_out.resize(((outlen + 96) / 8) + (((outlen + 96) % 8 != 0) ? 1 : 0));
					setBitVal(&map_out, outlen + 3, 1);
					setBitVal(&map_out, outlen + 6, 1);
					setBitVal(&map_out, outlen + 12, 1);
					setBitVal(&map_out, outlen + 21, 1);
					setBitVal(&map_out, outlen + 27, 1);
					setBitVal(&map_out, outlen + 30, 1);
					setBitVal(&map_out, outlen + 36, 1);
					setBitVal(&map_out, outlen + 45, 1);
					setBitVal(&map_out, outlen + 51, 1);
					setBitVal(&map_out, outlen + 54, 1);
					setBitVal(&map_out, outlen + 60, 1);
					setBitVal(&map_out, outlen + 69, 1);
					setBitVal(&map_out, outlen + 75, 1);
					setBitVal(&map_out, outlen + 78, 1);
					setBitVal(&map_out, outlen + 84, 1);
					setBitVal(&map_out, outlen + 93, 1);
					outlen += 96;
					break;
				}

				default:
				{
					std::cerr << "Bad symbol in MGD stream!\n";
					exit(-1);
				}
				}
			}
		}

		datastream->clear();
		datastream->resize(map_out.size());
		std::copy(map_out.begin(), map_out.end(), datastream->begin());
		return outlen;
	}

	case 150:
	case 300:
	case 600:
	{
		unknownMod = 20;
		while (i < bitlen)
		{
			if (affecting == false)
			{
				for (size_t j = i; j < i + unknownMod; j++)
				{
					temp = getBitVal(*datastream, j);
					switch (temp)
					{
					case 0:
					{
						outlen += 3;
						map_out.resize(((outlen) / 8) + ((outlen % 8 != 0) ? 1 : 0));
						break;
					}

					case 1:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						outlen += 3;
						break;
					}

					default:
					{
						std::cerr << "Invalid symbol in MGD stream!\n";
						exit(-1);
					}
					}
				}

				i += unknownMod;
				affecting = true;
			}
			else
			{
				switch (Baud)
				{
				case 150:
				{
					switch (inter_len)
					{
					case interleave_len::_zero:
					case interleave_len::_short:
					{
						D1 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
						D2 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
						break;
					}

					case interleave_len::_long:
					{
						D1 = { 0x10, 0x48, 0x20, 0x10, 0x48, 0x20 };
						D2 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
						break;
					}
					}
				}

				case 300:
				{
					switch (inter_len)
					{
					case interleave_len::_zero:
					case interleave_len::_short:
					{
						D1 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
						D2 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
						break;
					}

					case interleave_len::_long:
					{
						D1 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
						D2 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
						break;
					}
					}
				}

				case 600:
				{
					switch (inter_len)
					{
					case interleave_len::_zero:
					case interleave_len::_short:
					{
						D1 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
						D2 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
						break;
					}

					case interleave_len::_long:
					{
						D1 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
						D2 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
						break;
					}
					}
				}
				}

				size_t dlen = 16 * 3;
				std::vector<byte> zeroPad = { 0x00, 0x00 };
				size_t padlen = 12;

				outlen = addStreams(&map_out, &D1, outlen, dlen);
				outlen = addStreams(&map_out, &D2, outlen, dlen);
				outlen = addStreams(&map_out, &zeroPad, outlen, padlen);

				affecting = false;
			}
		}

		datastream->clear();
		datastream->resize(map_out.size());
		std::copy(map_out.begin(), map_out.end(), datastream->begin());
		return outlen;
	}

	case 1200:
	{
		unknownMod = 20;
		while (i < bitlen)
		{
			if (affecting == false)
			{
				for (size_t j = i; j < i + (unknownMod * 2); j+= 2)
				{
					temp = (getBitVal(*datastream, j) << 1) | getBitVal(*datastream, j + 1);
					switch (temp)
					{
					case 0:
					{
						outlen += 3;
						map_out.resize(((outlen) / 8) + ((outlen % 8 != 0) ? 1 : 0));
						break;
					}

					case 1:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen + 1, 1);
						outlen += 3;
						break;
					}

					case 2:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						outlen += 3;
						break;
					}

					case 3:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen + 1, 1);
						setBitVal(&map_out, outlen, 1);
						outlen += 3;
						break;
					}

					default:
					{
						std::cerr << "Invalid symbol in MGD stream!\n";
						exit(-1);
					}
					}
				}

				i += (unknownMod * 2);
				affecting = true;
			}
			else
			{
				
				switch (inter_len)
				{
				case interleave_len::_zero:
				case interleave_len::_short:
				{
					D1 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
					D2 = { 0x10, 0x48, 0x20, 0x10, 0x48, 0x20 };
					break;
				}

				case interleave_len::_long:
				{
					D1 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
					D2 = { 0x10, 0x48, 0x20, 0x10, 0x48, 0x20 };
					break;
				}
				}

				size_t dlen = 48;
				std::vector<byte> zeroPad = { 0x00, 0x00 };
				size_t padlen = 12;

				outlen = addStreams(&map_out, &D1, outlen, dlen);
				outlen = addStreams(&map_out, &D2, outlen, dlen);
				outlen = addStreams(&map_out, &zeroPad, outlen, padlen);

				affecting = false;
			}
		}

		datastream->clear();
		datastream->resize(map_out.size());
		std::copy(map_out.begin(), map_out.end(), datastream->begin());
		return outlen;
	}

	case 2400:
	case 4800:
	{
		unknownMod = 16;
		while (i < bitlen)
		{
			if (affecting == false)
			{
				for (size_t j = i; j < i + (unknownMod * 3); j += 3)
				{
					temp = (getBitVal(*datastream, j) << 2) | (getBitVal(*datastream, j + 1) << 1) | getBitVal(*datastream, j + 2);
					switch (temp)
					{
					case 0:
					{
						outlen += 3;
						map_out.resize(((outlen) / 8) + ((outlen % 8 != 0) ? 1 : 0));
						break;
					}

					case 1:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen + 2, 1);
						outlen += 3;
						break;
					}

					case 2:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen + 1, 1);
						outlen += 3;
						break;
					}

					case 3:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen + 2, 1);
						setBitVal(&map_out, outlen + 1, 1);
						outlen += 3;
						break;
					}

					case 4:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						outlen += 3;
						break;
					}

					case 5:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						setBitVal(&map_out, outlen + 2, 1);
						outlen += 3;
						break;
					}

					case 6:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						setBitVal(&map_out, outlen + 1, 1);
						outlen += 3;
						break;
					}

					case 7:
					{
						map_out.resize(((outlen + 3) / 8) + (((outlen + 3) % 8 != 0) ? 1 : 0));
						setBitVal(&map_out, outlen, 1);
						setBitVal(&map_out, outlen + 1, 1);
						setBitVal(&map_out, outlen + 2, 1);
						outlen += 3;
						break;
					}

					default:
					{
						std::cerr << "Invalid symbol in MGD stream!\n";
						exit(-1);
					}
					}
				}

				i += (unknownMod * 3);
				affecting = true;
			}
			else
			{
				switch (Baud)
				{
				case 2400:
				{
					switch (inter_len)
					{
					case interleave_len::_zero:
					case interleave_len::_short:
					{
						if (dtype == data_type::data)
						{
							D1 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
							D2 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
							break;
						}
						else
						{
							D1 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
							D2 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
							break;
						}
					}

					case interleave_len::_long:
					{
						if (dtype == data_type::data)
						{
							D1 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
							D2 = { 0x00, 0x09, 0x24, 0x00, 0x09, 0x24 };
							break;
						}
						else
						{
							std::cerr << "Invalid interleave length selected. How did this happen?\n";
							exit(1);
						}
					}
					}
				}

				case 4800:
				{
					switch (inter_len)
					{
					case interleave_len::_zero:
					case interleave_len::_short:
					{
						D1 = { 0x12, 0x08, 0x04, 0x12, 0x08, 0x04 };
						D2 = { 0x02, 0x49, 0x00, 0x02, 0x49, 0x00 };
						break;
					}

					case interleave_len::_long:
					{
						std::cerr << "Invalid interleave length selected. How did this happen?\n";
						exit(1);
					}
					}
				}
				}

				size_t dlen = 48;

				outlen = addStreams(&map_out, &D1, outlen, dlen);
				outlen = addStreams(&map_out, &D2, outlen, dlen);

				affecting = false;
			}
		}

		datastream->clear();
		datastream->resize(map_out.size());
		std::copy(map_out.begin(), map_out.end(), datastream->begin());
		return outlen;
	}

	default:
	{
		std::cerr << "Invalid baud selected. How did this happen?\n";
		exit(1);
	}
	}
}
