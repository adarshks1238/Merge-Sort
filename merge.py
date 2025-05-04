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

    for k in range(low, high + 1):
        a[k] = b[k]


a = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nBefore merge:", a)

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)

merge_sort(0, len(a) - 1)

print("After merge: ", a)
