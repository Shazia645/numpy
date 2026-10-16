#shape and reshapin numpy array
import numpy as np
var=np.array([[1,2,3],[4,5,6]])
print(var)
print()
print(var.shape)
#ndmin means multi dimentional array
var2=np.array([1,2,3,4,5,6])
x=var2.reshape(3,2)
print(x)

print(x.ndim)# dimentio

#brodcastiny numpy
a=np.array([1,2,3,4,5])# agar elements barabr na hoto broadcasting error aya ga
b=np.array([6,7,8,9,5])# yaha pa agr kisi array mai ek b value kam ho to error da ga blzz ya stisfy ni krya broadcast error ga ag
print(a+b)


v1=np.array([1,2,3])
print(v1.shape)
# yaha pa numbrs of row one hai ur numbr of colum 3 hai
# kisi b  arrays ko add karna ka alia unka dimensions same hona chaya 
# second rule  ya hai ki agr dimention alg hai to kisi ek ka pass valu same honi chaya like(1*3) ur(3*1) mai 1

