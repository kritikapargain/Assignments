#creating function with zero parameters
def f(): 
    print(s)      # free occurrence of s in f
    
s = "Python"
f()

#creating function with three parameters
def return_sum(x, y ,z):

    c = x + y + z
    return c

res = return_sum(4, 5, 1)
print(res)

#creating function with four parameters
def multiply(x,y,z,a):

    b = x*y*z*a
    return b
mul = multiply(1,2,3,4)
print(mul)
