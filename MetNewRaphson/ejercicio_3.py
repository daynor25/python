import sympy
from sympy import Symbol
from scipy.misc import derivative
import math
from sympy import sin,cos,exp
print("Teniendo en cuenta la funcion: f(x)= e^x+2^-x+2cos(x)-6 en \nel intervlo [1,2],con Xo=2")
erroru=float(input('introduce el error:'))
X0=2
x=Symbol('x')

print("\nf'(x)= ",sympy.diff(exp(x)+2**-x+2*cos(x)-6,x))
print("\n==== Evaluamos f(x) y f'(x) en Xo ====")
def funcion(x):
    f0=math.exp(x)+2**-x+2*math.cos(x)-6
    return (f0)
i=0
error=1
while abs(error)>erroru:
    print ("\n*=*=*=*=ITERACION=",i)  
    f0=funcion(X0)
    print ("f(",X0,")=",f0)
    f=lambda x:exp(x)+2**-x+2*cos(x)-6
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
