def encrypt(block, eKey, nKey):
    a = eKey
    b = block
    c = 1
    while a != 0:
        c = ((c * b) % nKey)
        a = (a - 1)
    return c
