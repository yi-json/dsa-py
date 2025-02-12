def bubble_sort(A):
    for i in range(len(A)):
        did_swap = False
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] # swap
                did_swap = True
        if did_swap:
            break