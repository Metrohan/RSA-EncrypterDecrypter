def decrypt(block, block2, d, nKey):

    block = int(block)
    block2 = int(block2)

    a = d
    b = 1
    c = 1

    print(block, block2)

    while a != 0:
        b = (block * b)
        a = a - 1
    b = b % nKey
    a = d

    while a != 0:
        c = (block2 * c)
        a = a - 1
    c = c % nKey

    b = str(b)
    c = str(c)

    if len(str(b)) < 4:
        block1_1 = str(b[:1])
        block1_2 = str(b[1:])
    else:
        block1_1 = str(b[:2])
        block1_2 = str(b)[2:]

    if len(str(c)) < 4:
        block2_1 = str(c[:1])
        block2_2 = str(c[1:])
    else:
        block2_1 = str(c[:2])
        block2_2 = str(c[2:])

    letters = []
    for num in (block1_1, block1_2, block2_1, block2_2):
        letter = chr(int(num) + 65)
        letters.append(letter)
    result = ''.join(letters)

    return result
