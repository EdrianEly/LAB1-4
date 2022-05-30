def findMinRec(A,n):
    # if size = 0 means whole array
    # has been traversed
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))


# Driver Code
if __name__ == '__main__':
    A = [1, 4, 45, 6, -50, 10, 2]
    n = len(A)
    print(findMinRec(A, n))


def findMaxRec(B, n):
    if (n == 1):
        return B[0]
    return max(B[n - 1], findMaxRec(B, n - 1))

if __name__ == "__main__":
    B = [1, 4, 45, 6, -50, 10, 2]
    n = len (B)
    print (findMaxRec(B, n))
