def separate1(word):
    word = word.strip()
    word = word.lower()
    print(word)
    blocks1 = []
    blocks2 = []

    for character in word:
        block = str(ord(character) - 97)
        if int(block) < 10:
            block = '0' + block
        blocks1.append(block)

    blocks2.extend(blocks1[-2:])
    blocks1 = blocks1[:-2]

    block1 = "".join(blocks1)
    block2 = "".join(blocks2)

    return block1, block2
