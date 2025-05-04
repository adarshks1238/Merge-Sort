def merge(low, mid, high):
    b = [0] * len(a)
    h = low
    j = mid + 1
    i = low

    while h <= mid and j <= high:
        if a[h] <= a[j]:
            b[i] = a[h]
            h += 1
        else:
            b[i] = a[j]
            j += 1
        i += 1

    while h <= mid:
        b[i] = a[h]
        h += 1
        i += 1

    while j <= high:
        b[i] = a[j]
        j += 1
        i += 1


