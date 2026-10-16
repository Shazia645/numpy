# copy vs view in numpy
# both are use to copy but agr jab copy mai data ko  kabi chang karty hai to
# original data mai koi chage nazar ni aya ga but jab view mai chages karty hai to changes orignial data mai banzar aya gre
import numpy as np
var=np.array([1,2,3,4,5])
co=var.copy()
# var[1]=40
print("var",var)
print()
print("copy",co)


# know view
x=np.array([1,2,3,4,5])
vi=x.view()
# x[1]=40
print(x)
print()
print("x :",x)
print("view",vi)

