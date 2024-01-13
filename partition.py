def partition(A, s, e, k):
    A[e], A[k] = A[k], A[e]
    pivot = A[e]
    gidx = s

    for i in range(s, e):
        if A[i] <= pivot:
            A[gidx], A[i] = A[i], A[gidx]
            gidx += 1
    #swap pivot with gidx
    A[gidx], A[e] = A[e], A[gidx]

    return gidx

if __name__ == "__main__":
    arr = [3, 4, 5, 1, 6, 2, 7, 8, 9]
    k = 5

    newk = partition(arr, 0, 8, k)
    
