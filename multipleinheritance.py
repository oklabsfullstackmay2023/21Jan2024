#1 class defination is one time process
class P1():
    #1. property/variable
    n1=10
    #2. constructor/esp.function
    #3. function/method
    pass
class P2():
    #1. property/variable
    n2=20
    #2. constructor/esp.functions
    #3. function/method
    pass
class P3():
    #1. property/variable
    n3=30
    #2. constructor/esp.functions
    #3. function/method
    pass
class C(P1,P2,P3):
    pass
#2. create class external object is many time process
c1=C()
print(c1.n1+c1.n2+c1.n3)