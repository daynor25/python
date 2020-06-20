import sympy
from sympy import Symbol
from scipy.misc import derivative
import math
print("Teniendo en cuenta la funcion: f(x)= x^3-4x^2-2 en \n el intervlo [4,5],con Xo=5")
erroru=float(input('introduce el error:'))
X0=5
x=Symbol('x')
a=0
b=0
c=0
print("\nf'(x)=",sympy.diff(x**3-4*x**2-2,x))
print("\n==== Evaluamos f(x) y f'(x) en Xo ====")
def funcion(x):
    f0=x**3-4*x**2-2
    return (f0)
i=0
error=1
while abs(error)>erroru:
    print ("\n*=*=*=*=ITERACION=",i)  
    f0=funcion(X0)
    print ("f(",X0,")=",f0)
    f=lambda x:x**3-4*x**2-2
    f1=derivative(f,X0,dx=1e-8)
    print ("f'(",X0,")=",f1)

    print("\n==== calculamos Xi= Po-(f(Po)/f'(Po)) ====")
    Xi=X0-(f0/f1)
    print("Xi=",Xi)
    aux=X0
    X0=Xi
    T=abs(aux-X0)
    error=((aux-X0)/aux)
    print("===|Xi-Xi-1|=",T)
    if(i==0):
        a=Xi
    else:
        if(i==1):
            b=Xi
        else:
            if(i==2):
                c=Xi
    i=i+1

print("\n*=*=solucion:",X0)
