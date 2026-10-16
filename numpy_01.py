import numpy as np
import json
list=[1,2,3,4,5]
print(list)
print(type(list))
# numpy aray python list sa ziada fast kam karta hai ur space b kam lata hai
# data type storage (mtlb list  mai hm numbrs strings sab ek list mmai store kar skta hai)
#but in np.array mai ya properlly strring ka upper kam kary ga ya properly number ka upper
# %timeit[i**4 for i in rang(1,9)] 
# %timeit np.arrag[1,9]**
a= np.array([1,2,3,4,5,6,7])
print(a)
print(type(a))

num=[1,2,3,4,5,6,7]
x=np.array(num)
print(x)

l=[]

for i in range(1,6):
    int_1=int(input("enter:"))
    l.append(int_1)
    print(np.array(l))
    print(l.ndim)
    # yaha  output string form mai mila ga q ki input fuction mai jo b data mila ga wo string form mai hoga
    # one dimmantionl aryy [1,2,3],
    # two dimentional arry[[1,2,3]]
    # three dimentional arry[[[1,2,3,4]]]
    # HIGHER DIMENTIONAL ARRY
    # ap ya (.ndim)arrayy  konca hai btaya ga




ar2=np.array([[9,99,99,99],[1,5,7,9,8]])
print(ar2)
print(ar2.ndim)
ar3=np.array([[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3,]]])
print(ar3)
print(ar3.ndim)
arn=np.array([1,11,,1111,1,11,1],ndmin=10)
print(arn)
print(arn.ndim)