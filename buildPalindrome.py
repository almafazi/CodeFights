i = len(Str)
    while True:
        canConvert = True
        j = 0
        while j < i - j - 1:
            if i - j - 1 < len(Str) and Str[j] != Str[i - j - 1]:
                canConvert = False
                break
            j += 1
        if canConvert:
            for j in range(len(Str), i):
                Str += Str[i - 1 - j]
            return Str
        i += 1
