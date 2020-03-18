#Author BlackSpirit
code = input()
hex_byte = {
    '0': '00000',
    '1': '00001',
    '2': '00010',
    '3': '00011',
    '4': '00100',
    '5': '00101',
    '6': '00110',
    '7': '00111',
    '8': '01000',
    '9': '01001',
    'A': '01010',
    'B': '01011',
    'C': '01100',
    'D': '01101',
    'E': '01110',
    'F': '01111',
    'G': '10000',
    'H': '10001',
    'I': '10010',
    'J': '10011',
    'K': '10100',
    'L': '10101',
    'M': '10110',
    'N': '10111',
    'O': '11000',
    'P': '11001',
    'Q': '11010',
    'R': '11011',
    'S': '11100',
    'T': '11101',
    'U': '11110',
    'V': '11111'
}

decode_table = {
    '11': ' ',
    '101': 'e',
    '1001': 't',
    '10001': 'o',
    '10000': 'n',
    '011': 'a',
    '0101': 's',
    '01001': 'i',
    '01000': 'r',
    '0011': 'h',
    '00101': 'd',
    '001001': 'l',
    '001000': '!',
    '00011': 'u',
    '000101': 'c',
    '000100': 'f',
    '000011': 'm',
    '0000101': 'p',
    '0000100': 'g',
    '0000011': 'w',
    '0000010': 'b',
    '0000001': 'y',
    '00000001': 'v',
    '000000001': 'j',
    '0000000001': 'k',
    '00000000001': 'x',
    '000000000001': 'q',
    '000000000000': 'z'
}


bit_stream = ""
for letter in code:
    bit_stream += hex_byte[letter]

bits = ""
result = ""
for bit in bit_stream:
    bits += bit;
    if (bits in decode_table):
        result += decode_table[bits]
        bits = ""

print(result)
