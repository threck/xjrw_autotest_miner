# -*- coding:utf-8 -*-
# 1mFIL = 10**-3 FIL
# 1μFIL = 10**-6 FIL
# 1nFIL = 10**-9 FIL
# 1pFIL = 10**-12 FIL
# 1fFIL = 10**-15 FIL
# 1aFIL = 10**-18 FIL


def to_nfil(count, unit):
    if unit == 'FIL':
        count = count * 1000000000
    elif unit == 'mFIL':
        count = count * 1000000
    elif unit == 'nFIL':
        count = count
    elif unit == 'pFIL':
        count = count * 0.001
    elif unit == 'fFIL':
        count = count * 0.000001
    elif unit == 'aFIL':
        if unit < 1:
            count = 0
        else:
            count = count * 0.000000001
    else:
        pass
        # if unit == 'μFIL':
        #     count = count * 1000
    return count, 'nFIL'

