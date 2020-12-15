import numpy as np
""" 
numpy.argsort() function is used to perform an indirect sort along the given axis using the algorithm specified by the kind key
It returns an array of indices of the same shape as arr that that would sort the array.
Syntax : numpy.argsort(arr, axis=-1, kind=’quicksort’, order=None)

Parameters :
arr : [array_like] Input array.
axis : [int or None] Axis along which to sort. If None, the array is flattened before sorting. The default is -1, which sorts along the last axis.
kind : [‘quicksort’, ‘mergesort’, ‘heapsort’]Selection algorithm. Default is ‘quicksort’.
order : [str or list of str] When arr is an array with fields defined, this argument specifies which fields to compare first, second, etc.

Return : [index_array, ndarray] Array of indices that sort arr along the specified axis.If arr is one-dimensional then arr[index_array] returns a sorted arr.
"""

list2=[
    [3,2,1],
    [7,8,9],
    [4,5,6] 
]

print(list2)

print('Along the row : ')
print(*np.argsort(list2,axis=1))

print('Along the column : ')
print(*np.argsort(list2,axis=0))