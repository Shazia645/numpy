# spiceal numpy arrays
# zero array
# craeating numpy arry using numpy function
import numpy as np
ar_zero=np.zeros(5)# one dimentional array
ar_zero1=np.zeros((4,3))# two dimentional array
ar_zero2=np.zeros(((4,5)))#three dimentionall array
print(ar_zero)
print()
print(ar_zero1)
print()
print(ar_zero2)
# ones funtion
ar_one=np.ones(4)
ar_one1=np.ones((2,3))
ar_one2=np.ones(((4,4)))
print(ar_one)
print()
print(ar_one1)
print()
print(ar_one2)



#empty array funtion
ar_empty=np.empty(5)
print(ar_empty)

ar_arrang=np.arange(3)
print(ar_arrang)

# array digonal metrics fill with one
ar_dia=np.eye(6)
print(ar_dia)# is mai agr hm chaha kabi ki 3,4 ki matric bnana cha to
ar_dia=np.eye(3,4)
print(ar_dia)

#linspace 

ar_lin=np.linspace(1,10,num=5)
print(ar_lin)
ar_lin=np.linspace(0,12,num=6)
print(ar_lin)
