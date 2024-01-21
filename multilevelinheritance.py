#1. class defination is one time process
class A():
    #1. property/state/variable
    n1=1
    #2. constructor/esp.functions
    #3. function/method/behaviour
    pass
class B(A):
    #1. property/state/variable
    n2=1
    #2. constructor/esp.functions
    #3. function/method
    pass
class C(B):
    #1. property/variable
    n3=1
    #2. constructor/esp.functions
    #3. function/method
    pass
class D(C):
    #1. property/variable
    n4=1
    #2. constructor
    #3. function
    pass
class E(D):
    #1. property/variable
    n5=1
    #2. constructor
    #3. function
    pass
class F(E):
    #1. property/variable
    n6=1
    #2. constructor
    #3. function
    pass
class G(F):
    #1. property/variable
    n7=1
    #2. constructor
    #3. function
    pass
class H(G):
    #1. property/vairable
    n8=1
    #2. constructor
    #3. function
    pass
class I(H):
    #1. property/variable
    n9=1
    #2. constructor
    #3. function
    pass
class J(I):
    #1. property/variable
    n10=1
    #2. constructor
    #3. function
    pass
class K(J):
    #1. property/variable
    n11=1
    #2. constructor
    #3. function
    pass
class L(K):
    #1. property/variable
    n12=1
    #2. constructor
    #3. function
    pass
class M(L):
    #1. property/variable
    n13=1
    #2. constructor
    #3. function
    pass
class N(M):
    #1. property/variable
    n14=1
    #2. constructor
    #3. function
    pass

#2. create class external object is many time process
n1=N()
print(n1.n14+n1.n13+n1.n12+n1.n11+n1.n10+n1.n9+n1.n8+n1.n7+n1.n6+n1.n5+n1.n4+n1.n3+n1.n2+n1.n1      )