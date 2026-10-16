#Numpy arithematic operator in array
import numpy as np
var=np.array([1,2,3,4,5])
varadd=var+3
print(varadd)


var=np.array([1,2,3,4,5])
varsub=var-3
print(varsub)


var=np.array([1,2,3,4,5])
varmul=var*3
print(varmul)


var=np.array([1,2,3,4,5])
vardiv=var/3
print(vardiv)


var=np.array([1,2,3,4,5])
varmod=var%3
print(varmod)

# iska ilawa isi kam ka lia hm functions b bna skta hai
var1=np.array([1,2,3,4,5])
var2=np.array([1,2,3,4,5])
varadd=np.add(var1,var2)
print(varadd)



#or ya b kar skta haii
var1=np.array([1,2,3,4,5])
var2=np.array([1,2,3,4,5])
varadd=np.add(var1,4)
print(varadd)# yha tak jitni bat huvi wo one dimentional array ki the


# two dimentional array
arr2=np.array([[1,2,3,4,5],[6,7,8,9,0]])
arr3=np.array([[1,2,3,4,5],[6,7,8,9,0]])
arradd=np.add(arr2,arr3)
print(arradd)
print()
# reciprocal function 
var=np.array([1,2,3,4,5])
varadd=np.reciprocal(var)
print(varmod)