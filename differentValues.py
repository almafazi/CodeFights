def differentValues(A, D):

    best = -1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            diff = abs(A[j] - A[i])
            if D-diff >= 0 and D-diff <= D-best:
                best = diff

    return best
