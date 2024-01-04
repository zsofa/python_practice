def jaccard(A, B):
    set_A = set(A)
    set_B = set(B)

    intersection = set_A.intersection(set_B)
    union = set_A.union(set_B)

    if len(union) == 0:
        return float('NaN')

    return len(intersection) / len(union)
