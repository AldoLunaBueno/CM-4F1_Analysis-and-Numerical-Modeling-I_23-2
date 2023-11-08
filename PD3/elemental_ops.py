import numpy as np

def swap(A, row1, row2):
    A = A.copy()
    temp = A.copy()[row1, :]
    A[row1, :] = A[row2, :]
    A[row2, :] = temp
    return A
def rowScale(A, row, k):
    A = A.copy()
    A[row, :] = k * A[row, :]
    return A
def addRowScaled(A, row, k, endRow):
    A = A.copy()
    temp = k * A[row, :]
    A[endRow, :] = A[endRow, :] + temp
    return A

A = np.array([[1, 2], [3, 4], [5, 6]])
A = addRowScaled(A, 1, 3, 0)
print(A)
