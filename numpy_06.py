#arithematic functions numpy
import numpy as np
var=np.array([1,2,3,4,5,3,2])
print("min :" ,np.min(var))
print("max :", np.max(var))


# ap isi ka idex numbr ka sat kaca laya
var=np.array([1,2,3,4,5,3,6,7])
print("min :" ,np.min(var),np.argmin(var))
print("max :", np.max(var),np.argmax(var))
print("sqrt :", np.sqrt(var))



var1=np.array([2,1,3],[2,6,7])
print(np.min(var1,axis=1))# idr axis  ka along print karna acces0 colum ut  axis1 row ka  alog kam kara gi



var1=np.array([2,1,3],[9,6,7])
print(np.min(var1,axis=0))

# ap valuue ka sin(@) kaca nikala
var2=np.array([1,2,3,4,5])
print(np.sin(var2))

var2=np.array([1,2,3,4,5])
print(np.cos(var2))
print(np.cumsum(var2))

#cumsum funtion
