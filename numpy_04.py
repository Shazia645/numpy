# data  type in numpy array
# data type function
import numpy as np
var=np.array([1,2,34,5,6,6])
print("data type :",var.dtype)

var=np.array([1.1,3.4,6.7,8.9])
print("data type :",var.dtype)

var=np.array(["w","u","H"])
print("data type :",var.dtype)

var=np.array([1.1,3.4,6.7,8.9],dtype=np.int8)# asa hm dta type ko b change kr skta  hai
print("data type :",var.dtype)


x=np.array([1.1,3.4,6.7,8.9],dtype="f")# ap yaha pa hm type hi change kar skta haia jasa int ko float bna skta hai
print("data type :",x.dtype)#
# ap hm isi data type ka funtion b bna skta hai

x1=np.array([1.1,3.4,6.7,8.9])
new=np.float32(x1)
print("data type :",x1.dtype)
print("data type :",new.dtype)
print(x1)
print(new)


x1=np.array([1.1,3.4,6.7,8.9])
new=np.float32(x1)
new2=np.int_(x1)
print("data type :",x1.dtype)
print("data type :",new.dtype)
print("data type :",new2.dtype)
print(x1)
print(new)

x3=np.array([1,2,3,4,5])# ap is fuction ka zarya ham direct data type change kar skta hai
new_1=x3.astype(float)
print(x3)
print(new_1)


