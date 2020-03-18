#Author Moriarty
encoder = {
' ': '11',
'e': '101',
't': '1001',
'o': '10001',
'n': '10000',
'a': '011',
's': '0101',
'i': '01001',
'r': '01000',
'h': '0011',
'd': '00101',
'l': '001001',
'!': '001000',
'u': '00011',
'c': '000101',
'f': '000100',
'm': '000011',
'p': '0000101',
'g': '0000100',
'w': '0000011',
'b': '0000010',
'y': '0000001',
'v': '00000001',
'j': '000000001',
'k': '0000000001',
'x': '00000000001',
'q': '000000000001',
'z': '000000000000'
}

decoder = {}

for k in encoder:
    decoder[encoder[k]] = k

def decode(s):
    radix = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
    e = ''
    for c in s:
        w = radix.index(c)
        e += ('{:05b}'.format(w))
    b = ''
    res = ''
    for c in e:
        if b+c in decoder:
            res += decoder[b+c]
            b = ''
        else:
            b += c
    return res
print(decode(raw_input()))
