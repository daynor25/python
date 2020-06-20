import math
f=float(input("ingrese numero:  "))

m=float(f*2)
pDecimal,pEntera=math.modf(m)
n=0
e=int(pEntera)
e1=0
punto=0
w=True
while n!=8:
    if e==0 and w==True:
        punto= punto+1
    else:
        w=False
    #print("e: ",e,"  n: ",n)
    #print (round(pEntera),"---",pDecimal,"----- e1: ",e1)
    #e=int(pEntera)
    if e==0:
        
        e=10
        e1=(e1)*e
        n=n+1
    else:
        #e=10
        e1=(e1*10**1)+e
        
    print("num. binario: ",e1)
    print("--------------------------------------------")
    
#print(e1)
    m=pDecimal*2
    pDecimal,pEntera=math.modf(m)
 
    e=int(pEntera)


#ent=int(cadena,base=2)
cadena=str(e1)
ent=int(cadena,base=2)
print(ent)
print("num.de ceros a la izq:",punto)    
print("num. binario: 0,",e1,"*2^-",bin(punto))

 
