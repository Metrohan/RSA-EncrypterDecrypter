def encrypt(block1, block2, eKey, nKey):
    a = eKey
    b1 = int(block1)
    b2 = int(block2)
    c = 1
    d = 1

    while a != 0:
        c = ((c * b1) % nKey)
        a = (a - 1)
    a = eKey

    while a != 0:
        d = ((d * b2) % nKey)
        a = (a - 1)

    if len(str(c)) < 4:
        c = '0' + str(c)

    if len(str(d)) < 4:
        d = '0' + str(d)

    lastblock = str(c) + ' ' + str(d)
    return lastblock
