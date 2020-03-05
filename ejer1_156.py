#ejercicios mat_156 (python)
#el mayor de dos numeros
def max(arg1, arg2):
     if arg1>arg2:
         print("el mayor es: ", arg1)
     else:
        print("el mayor es: ", arg2)
arg1=float(input("introduce primer numero: "))
arg2=float(input("introduce segundo numero: "))

max(arg1,arg2)

#el mayor de tres numeros
A=float(input("ingrese un numero\n"))
B=float(input("ingrese el segundo numero\n"))
C=float(input("ingrese el tercer numero\n"))
def max_tres(arg1,arg2,arg3):
 if(arg1 > arg2 and arg1 > arg3):
    print("El numero mayor es: ", arg1)
 else:
    if(arg2 > arg1 and arg2 > arg3):
       print("El numero mayor es: ", arg2)
    else:
         print("El numero mayor es: ", arg3)
  
max_tres(A,B,C)  

#FACTORIAL DE UN NUMERO 
a=int(input("INGRESE UN NUMERO: "))
def fact(a):
 count=1
 z = 1
 while z <= a:
   count=count*z
   z = z + 1
 return count

print("el factorial es: ",fact (a)) 

 
#CONTADOR DE NUMEROS PARES Y SU SUMA ENTRE DOS VALORES
a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero mayor al anterior: "))
def cant_pares_sum(a,b):
 contar=0
 sum=0
 for a in range(a,b+1):
    if a%2!=0:
        contar=contar+1
        sum=a+sum
        # TODO: write code...
    # TODO: write code...
 print("cantidad de num. impares: ",contar)
 print("La suma es: ",sum)
 
cant_pares_sum(a,b) 

#CONVERTIR UN NUMERO DE BASE 10 A UN NUMERO A BASE 2
import math
a1=int(input("ingrese un numero a convertir: "))
def bin_a_dec(a1):
 binario = ""
 if (a1 > 0):
    while(a1 > 0):
        if (a1%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        a1 = int(math.floor(a1/2))
 return binario   
    
print("num.conv.binario: ", bin_a_dec(a1) ) 
