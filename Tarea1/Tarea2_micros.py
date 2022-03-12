# coding=utf-8

import RPi.GPIO as GPIO
import time
import random
import threading
import argparse
GPIO.setwarnings(False)


parser = argparse.ArgumentParser()
parser.add_argument('--dato', type=int, default=0,help='Elige el tamaño de la lista')
args=parser.parse_args()

cantidad_de_datos = args.dato

#Configuración del pin 40 de la RPI como input
#y se asigna a la variable snl lo que se lea en
#este pin



GPIO.setmode(GPIO.BOARD)
btn = 40
GPIO.setup(btn, GPIO.IN)
snl = GPIO.input(btn)



#cantidad_de_datos = int(input("Ingrese la cantidad deseada de elementos: "))

#Cuando el botón se presiona se sale del
#bucle while, esto genera que el programa espere hasta
#presionar el botón para iniciarl el programa
print("Esperando a que se presione el botón para iniciar")
while True:
    if GPIO.input(btn):
        print("Botón presionado")
        break
    else:
        pass

#Esta funcion se encarga de sumar todos los numeros de la lista
def suma(lista):
    numero = 0
    for suma in lista:
        numero=numero+suma
        time.sleep(0.1)
    return numero
#Esta funcion solo crea la lista con los numeros randoms para ser trabajados
def array (x):
    lista = []
    i=1
    while i<=x:
        randnums=random.randint(1,26)
        lista.append(randnums)
        i=i+1
    return lista

lista_guardada=array(cantidad_de_datos)


start = time.time()
suma(lista_guardada)
end = time.time()
print ("La lista es ",lista_guardada)
print ("El resultado es: ",suma(lista_guardada))
print("El tiempo tiempo de cálculo fue de: ", end-start,"s")

numero_de_hilos = 4
lista_2=list()
lista_1=list()
lista_3=list()
lista_4=list()
lista_res = list()
resultado = 0
 
def funcion_hilos(indicador, inicio,fin): # Se toma la lista generada y se crea una nueva lista añadiendo solo los datos que le corresponde a cada hilo
    numero = 0
    while inicio<fin:   # y los suma
        if (indicador==0):
            lista_1.append(lista_guardada[inicio])
            inicio += 1
        elif(indicador==1):
            lista_2.append(lista_guardada[inicio])
            inicio += 1
        elif(indicador==2):
            lista_3.append(lista_guardada[inicio])
            inicio += 1

        elif(indicador==3):
            lista_4.append(lista_guardada[inicio])
            inicio += 1
            
    if (indicador==0):
        a=suma(lista_1)
        lista_res.append(a)
    elif(indicador==1):
        b=suma(lista_2)
        lista_res.append(b)
    elif(indicador==2):
        c=suma(lista_3)
        lista_res.append(c)
    elif(indicador==3):
        d=suma(lista_4)
        lista_res.append(d)
    return lista_res


#P define la cantidad de elementos que debe tener cada hilo
p = len(lista_guardada)//4
verificador = len(lista_guardada)/4
decimales = verificador%1


#diferentes inicios y diferentes finales
inicios = list()
fines = list()
inicio = 0
fin = p

if verificador ==int(verificador):   #Esta seccion es para saber si la lista contiene una cantidad multiplo de 4 para poder repartir los numeros y que no se pierda ninguno
    for i in range(numero_de_hilos): #Esto es para repartir equitativamente los datos y saber en qué posición de la lista empieza a tomar
        inicios.append(inicio)       #datos el hilo correspondiente, inicios[0] empiezan los datos del hilo 1 y terminan en fines[0]
        fines.append(fin)
        inicio +=p
        fin +=p
else:
    if(decimales==0.75):#Si no es multiplo de 4, los datos se reparten a los primero tres hilos como si fuera un multiplo de 4 al numero mas
        p= p+1                          #cercano y de mas valor y al ultimo hilo se reparte lo demas
        fin = p
        cont = 0
        for i in range(numero_de_hilos):
            inicios.append(inicio)
            fines.append(fin)
            inicio +=p
            if (i <2):
                fin +=p
            else:
                fin = len(lista_guardada)
    elif (decimales==0.25):
        p=p+1
        fin = p
        for i in range(numero_de_hilos): 
            inicios.append(inicio)
            fines.append(fin)
            inicio +=p
            p = len(lista_guardada)//4
            fin +=p
    elif (decimales==0.5):
        p=p+1
        fin = p
        contador = 0
        for i in range(numero_de_hilos):
            while (contador<2):
                inicios.append(inicio)
                fines.append(fin)
                inicio +=p
                fin +=p
                contador = contador + 1
                if (contador==2):
                    fin = fin -1
                    p = len(lista_guardada)//4
            inicios.append(inicio)
            fines.append(fin)
            inicio +=p
            fin +=p            
        
threads = list()
t0 = time.time()
for i in range(4):
    t = threading.Thread(target=funcion_hilos, args=(i,inicios[i], fines[i],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

resultado_final = 0
for i in lista_res:
        resultado_final=resultado_final+i
        time.sleep(0.1)
tf= time.time()-t0
print("\n")
print("El resultado de la suma es: ",resultado_final)
print("El tiempo total en 4 threads fue de: ", tf, "s")
print(threads)
