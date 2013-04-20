def hash_weighted(astring, tablesize):
    sum = 0
    i = 1
    for pos in range(len(astring)):
        sum = sum + i*ord(astring[pos])
        i = i + 1

    return sum%tablesize
