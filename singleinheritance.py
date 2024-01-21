#1. class defination is one time process
class A():
    #1. property/variable/state
    n1=10
    #2. constructor/esp.function
    #3. function/method
    pass

class B(A):
    #1. property/state
    n2=20
    #2. constructor/esp.function
    #3. function/method
    pass

#2. create class external object is many time process
b1=B()
print(b1.n1 + b1.n2)