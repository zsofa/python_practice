def jaccard(A, B):
    if not isinstance(A, str) or not isinstance(B, str):
        return float('nan')
    elif A is None or B is None:
        return float('nan')

    A = A.strip()
    B = B.strip()

    if not A or not B:
        return float('nan')

    # A and B together without spaces:
    set_A = set(A)
    set_B = set(B)

    # get Jaccard index
    intersection = len(set_A.intersection(set_B))
    union = len(set_A.union(set_B))

    if union == 0:
        return float('nan')

    return intersection / union

