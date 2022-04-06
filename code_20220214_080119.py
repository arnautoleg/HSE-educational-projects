def find_percentile(a, b, p):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1

    if (len(a) + len(b)) % 2 == 0:
        return result[int((len(a) + len(b))*(p/100))-1]
    return result[int((len(a) + len(b))*(p/100))]
