import math
print("teniendo en cuenta la funcion:f(x)= x^3+4x^2-10")
A=1
B=4
C=10

print("ingrese intervalos:  ")
a=int(input("a="))
b=int(input("b="))


def funcion1(a):
  x1=a ** 3
  x2=a ** 2
  fa=x1+4*x2-10
  return fa

def funcion2(b):
  x1=b ** 3
  x2=b ** 2
  fb=x1+4*x2-10
  return fb 


def Ec_Xi(a,b):
  Xi=float(1/2*(a + b))
  return Xi


def funcionXi(a,b):
  fx=Ec_Xi(a,b) ** 3+4*Ec_Xi(a,b) ** 2 -10
  return fx 


s1=0
s2=0
for i in range(1,15):
     
    if (funcion1(a)*funcion2(b))<0 and funcionXi(a,b)>0:
       print("\n -----ITERACION:",i)
       print(" a=",a,"\n b=", b,"\n f(a)=",funcion1(a),
       "\n f(b)=", funcion2(b),
       "\n Xi=",Ec_Xi(a,b),
       "\n f(Xi)=",funcionXi(a,b))
       a=a
       b=Ec_Xi(a,b)
       s1=s2
       s2=b
       
       s4=abs(s2-s1)
       print("\n s1=",s1,"\n s2=",s2,"\n |Sn-Sn-1|=",s4)
       if(10 ** -3 - s4>0):
          print("----solucion: ",s1) 
          break 


    else:
        print("\n -----ITERACION:",i)
        print(" a=",a,"\n b=",b,"\n f(a)=",funcion1(a),
        "\n f(b)=", funcion2(b),
        "\n Xi=",Ec_Xi(a,b),
        "\n f(Xi)=",funcionXi(a,b))
        a=Ec_Xi(a,b)
        b=b
        s1=s2
        s2=a
        s3=abs(s2-s1)
        print("\n s1=",s1,"\n s2=",s2,"\n |Sn-Sn-1|=",s3)
        if(10 ** -3 - s3>0):
           print("----solucion: ",s1)  
           break 

    
      





    