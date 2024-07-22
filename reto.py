#ejercicio 1
nombre =input("Escriba su nombre:")
edad = int(input("Escriba su edad:"))
print(nombre)
print(edad)
print(edad+5)
#ejercicio 2
fruit= ["manzana", "pera", "sandia", "durazno", "uva"]
print(fruit[2])

num= int(input("ingresa un numero:"))
if num % 2==0:
    print("el numero{num}es par.")
else:
    print("el numero{num}es impar.")
    
#ejercicio 3    
nombre =input("Escriba su nombre:")
edad = int(input("Escriba su edad:"))
print(nombre)
print(edad)
if edad >=18:
    print("puede votar")
else:
    print("no puede votar")
#ejercicio 4

celsius=int(input("ingresa la temperatura:"))
if celsius>=100:
    print("gaseoso")
elif celsius>=1:
     print("liquido")
else:
     print("solido")

num=int(input("ingresa un numero:"))
if num>=1:
    print("positivo")
elif num>=0:
    print("su numero es 0")
else:
    print("no es un entero")
    
#ejercicio 5

nu1=int(input("ingresar un numero:"))
nu2=int(input("ingresar otro numero:"))

if nu1>=0 and nu2>=0:
    print("ambos- son positivos")
elif nu1>=0 and nu2<=-1:
    print("solo el primero positivo{nu1}")
elif nu1<=-1 and nu2>=0:
    print("solo segundo positivo {nu2}")
    
#ejercicio 6
edad=int(input("ingrese su edad:"))
id=input(" porta identificacion vigente ('yes' o 'no'):")

if edad>=18 and id=='yes':
    print("puede votar")
else:
    print("son positivos")
    
#ejercicio 9
Con=1
while Con<=10:
    print(Con)
    Con=Con +1 
#ejercicio 10
for x in range(1,11):
    print(x)