import math
print("teniendo en cuenta la funcion:f(x)= 2Xcos(2x)-(x-1)^2")
print("ingrese intervalos:  ")
a=int(input("a="))
b=int(input("b="))


def funcion1(a):
  fa=2*a*(math.cos(2*a))-pow((a+1), 2)
  return fa


def funcion2(b):
  x2=b 
  fb=2*x2*(math.cos(2*x2))-pow((b+1), 2)
  return fb 


def Ec_Xi(a,b):
  Xi=float(1/2*(a + b))
  return Xi


def funcionXi(a,b):
  fx=2*Ec_Xi(a,b)*(math.cos(2*Ec_Xi(a,b)))-pow((Ec_Xi(a,b)+1), 2)
  return fx 

print(funcion1(a))
print(funcion1(b))
print (Ec_Xi(a,b))
print(funcionXi(a,b))

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
       if((10 ** -3)-s4>0):
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
        if((10 ** -3)-s3>0):
           print("----solucion: ",s1)  
           break 
