import os
import random

from pyraptorq import Encoder, Decoder


SYMBOL_SIZE = 768
DATA_SIZE = 2000
SYMBOL_COUNT = (DATA_SIZE + SYMBOL_SIZE - 1) // SYMBOL_SIZE


data = os.urandom(DATA_SIZE)


encoder = Encoder(data, SYMBOL_SIZE)

symbols = list(enumerate([encoder.gen_symbol(i) for i in range(0, SYMBOL_COUNT + 10)]))

print(symbols)


decoder = Decoder(SYMBOL_COUNT, SYMBOL_SIZE, DATA_SIZE)

random.shuffle(symbols)

for s in symbols:
    print('adding symbol id#', s[0])
    decoder.add_symbol(s[0], s[1])
    print(decoder.may_try_decode())
    if decoder.may_try_decode():
        print('decoding...')
        result = decoder.try_decode()
        if result is not None:
            break
else:
    raise Exception('Failed to decode')

assert result == data
