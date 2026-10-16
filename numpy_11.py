# joining and spliting two arrays
import numpy  as np
var=np.array([1,2,3,4,5,6])
var1=np.array([7,8,94,5,6])
# idr ap dakho yaha pa two arrays to addd karna ka lia  concrete funtion ka use kary kary ga
ar=np.concatenate((var,var1))
print(ar)
print()
var=np.array([[1,2,3,4,5,6],[1,2,4,5,6,7]])
# split function





#what are numpy array function

arr = np.array([10, 20, 30, 40])
new_arr = np.insert(arr, 2, 25)
print(new_arr)


# yaha mai  multilpe values b insert kr skti hu
arr = np.array([10, 20, 30, 40])
new_arr = np.insert(arr, 2, [25, 26])
print(new_arr)


# array sa valu dlet krna
arr = np.array([10, 20, 30, 40])
new_arr = np.delete(arr, 2)
print(new_arr)




