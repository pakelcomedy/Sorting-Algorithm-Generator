def merge(arr, l, m, r, steps):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
    steps.append(arr[:])

def merge_sort(arr, l, r, steps):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m, steps)
        merge_sort(arr, m + 1, r, steps)
        merge(arr, l, m, r, steps)

if __name__ == "__main__":
    from generate_puzzle import generate_puzzle

    puzzle = generate_puzzle(length=100)  # Menghasilkan 25.000 elemen
    print("Generated puzzle:", puzzle)

    steps = []
    merge_sort(puzzle, 0, len(puzzle) - 1, steps)

    print("Solution steps:")
    for step in steps:
        print(step)
