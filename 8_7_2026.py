import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr[0,1])       
print(arr[1] + arr[2]) # row addition

print(arr.shape)       # shape
print(arr.size)        # size
print(arr.ndim)        # ndim
print(arr.dtype)       # dtype
print(np.max(arr))     # max
print(np.min(arr))     # min
print(np.mean(arr))    # mean
print(np.std(arr))     # std
print(np.sum(arr))     # sum
print(np.prod(arr))    # prod
print(np.transpose(arr)) # transpose
print(np.ravel(arr))   # ravel
print(np.reshape(arr,(1,9))) # reshape
print(np.unique(arr))  # unique
print(np.sort(arr))    # sort