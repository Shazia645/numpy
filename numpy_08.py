#indexing and  slicing in numpy array
import numpy as np
v1=np.array([1,2,3,4])
# index      0,1,2,3
print(v1[0])
print(v1[1])
print(v1[2])
print(v1[3])
print()

# negative indexing -1,-2,-3,-4
print(v1[-1])
print(v1[-2])
print(v1[-3])
print(v1[-4])

print()
v2=np.array([[9,8,7],[5,4,3]])
print(v2)
print(v2.ndim)
print()
print(v2[0,2])# yaha pa ap 2d array ka andr sa  valu nikalna ka lia first ya btana hoga ki row numbr than first element like[0,1]


print()
#3d array
a=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a)
print(a.ndim)# ndim dimention btata hai 
print()
print(a[0,1,1])
# slicing
arr=np.array([1,2,3,4,5,6,7])
print(arr)
print(" 1 to 4:",arr[0:4])
print()
print(" start to last:",arr[0:])
print(" start to 7:",arr[:7])
print()
# ap agr muja data jump karta hua chaya to
print("stop :",arr[::2])# idr ap   2 means jump hai 1,3,5,7  asa print hoga
print("stop :",arr[1:4:2])# asa b hoskta tha





# agr two dimention arry ho to slicing  kaca kara
var=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(var)
print()
print(" 8 to 5:",var[1,1:])
# agr thee dimention arry mai slicing kara ga to asa hi comas  data hua karna hai


            

