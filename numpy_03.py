#rand_funtion(the funtion is used to create a random value btw 0,1)
#RANDOM  rand(): is ma only positive
import numpy as np# ya to one dimention ka lia tha 
var=np.random.rand(6)
print(var)
# for two dimentional rand()array 
var_1=np.random.rand(6,6)
print(var_1)

#randn(): the function is used to generate random value close to zero
# this may return positive or negative valu as wel


#randn():
var_2=np.random.randn(6)
print(var_2)

#ranf(): this function is also used to give random value in numpy but
# it return an array of spicified shape and fil it with random floats inthe 
# half open interval[0.0,1.0)
var_3=np.random.ranf(6)
print(var_3)


#randint():this funtion is used to generate random number having range
var_4=np.random.randint(2,12,20)#(min,max,totle_value)
print(var_4)

