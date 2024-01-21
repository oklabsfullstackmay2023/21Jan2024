#1. class defination is one time process
#class Child(Parent)
class P():
    #1. property/variable
    n1=5
    #2. constructor/esp.function
    #3. function/method
    pass
#class Child(Parent)
class C1(P):
    #1. property/variable
    n2=10
    #2. constructor/esp.function
    #3. function/method
    pass
#class Child(Parent)
class C2(C1):
    #1. property/variable
    n3=15
    #2. constructor/esp.function
    #3. function/method
    pass
#class Child(Parent)
class C3(C2):
    #1. property/variable
    n4=20
    #2. constructor/esp.function
    #3. function/method
    pass
class C4(C3):
    pass
#2. class create external object is many time process
c4=C4()
print(c4.n1+c4.n2+c4.n3+c4.n4)




