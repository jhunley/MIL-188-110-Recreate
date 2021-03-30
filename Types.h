#ifndef _TYPES_H
#define _TYPES_H

typedef unsigned char byte;

byte getBitVal(std::vector<byte> stream, size_t idx);
void setBitVal(std::vector<byte>* stream, size_t idx, byte val);
byte unaryXOR(byte val);

#endif