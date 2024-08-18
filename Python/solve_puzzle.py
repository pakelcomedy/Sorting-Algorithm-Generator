def merge_sort(arr, left, right, steps):
    """Perform merge sort on the array."""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, steps)
        merge_sort(arr, mid + 1, right, steps)
        merge(arr, left, mid, right, steps)

def merge(arr, left, mid, right, steps):
    """Merge two sorted halves of the array."""
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

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

    steps.append(arr[:])  # Save the current state of the array
