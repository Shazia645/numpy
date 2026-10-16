# numpy mai iteration kaca kary function sa
# iteration in numpy
import numpy as np
v1=np.array([1,2,3,4,5,6])
print(v1)
print()
for i in v1:
    print(i)
    # agr 2d array hai to
    var=np.array([[1,2,3,4],[5,6,7,8]])

print(var)
print()
for j in var:
    print(j)
print()# agr ham chaha  muja row  mai ni chay data har eelement alag sa chay phr iterationka andr ireration karna hopoga
for k in (var):# ap ya dusra tarika hai asa sara elements alg sa mila ga
    for l in k:
        print(l)



# yahi case agr ham 3d array ka lia kara to
#  waha pa pjir hamy 3 bar loop laga na parada ga
k=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(k)
print()
for i in k:  
  for l in i:
    for s in l:
        print(s)



# agr ham chaha  ki bara bar for loop na lag kr  is ka lia ek funtion bnaya ur 
# nditer()ya     ek funtion ha
k=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(k)
print(k.ndim)
print()
for i in  np.nditer(k):
   print(i)

   
k=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(k)
print(k.ndim)
print()
for i,d in  np.ndenumerate(k):# ap ya niter ko hata ka ndinumertor funtion ds ga
   print(i,d)# agr ham chata hai ki data ka ast uski index valu b print ho to  ur ek funtion use karna  hoga
