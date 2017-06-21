import math
'''
Created on 18/04/2013

@author: Leeecher
'''
'''1. Media, Varianza y Varianza estandar
Entrada: Dos numeros y una lista: Un numero para la seccion del menu y otro para la cantidad de variables a utilizar en la lista. En caso de la lista, se insertaran las "segundo numero" variables que el usuario desee
Salida: Si el numero insertado en el menu es 1, se retorna la media de la tupla; si es un 2, se retorna la varianza de la tupla y si se inserta un 3, se retorna la varianza estandar. Ademas, si se inserta un 4, se sale de la funcion 
Restriccion: Ninguna'''
def menufuncion():
    menucondicion=False #Condicion en caso de que el usuario inserte caracteres distintos a numeros
    while not menucondicion: #Mientras la condicion sea falsa, se repite lo siguiente
        print "Elija una de las siguientes opciones:\n1. Calcular la media\n2. Calcular la varianza\n3. Calcular la desviacion estandar\n4. Salir" #Menu de seleccion
        try: #Se inserta un try para evitar errores en el programa en caso de que se inserten caracteres invalidos
            menu=input("Cual opcion desea elegir: ") #Se pregunta por opcion
            if menu not in [1,2,3,4]: #Si lo insertado anteriormente no esta dentro del rango de 1,2,3 o 4, se envia mensaje de error
                return "Error: Entrada invalida"
            else: #Si no se cumple las condiciones anteriores, la condicion se hace True, evitando el while
                menucondicion=True
        except: #Si se insertan caracteres invalidos, se envia mensaje de error
            return "Error: Datos insertados no son numeros"
    if menu==4: #Si lo insertado por el usuario fue un 4, se envia mensaje de despedida 
        return "Hasta luego"
    else: #Si fue otro numero distinto a 4, se cumple lo siguiente
        try: #Se inserta el try en caso de insertar caracteres invalidos, para evitar errores
            numeros=input("Favor digitar los numeros en una tupla (separado entre comas): ") #Se pide al usuario insertar una tupla con las variables deseadas
        except: #Si lo insertado es invalido, se manda mensaje de error
            return "Error, digitos invalidos."
    cantvariab=len(numeros) #La cantidad de variables se determina por la cantidad de elementos en la tupla
    if menu==1: #Si el usuario inserto en el menu un 1, se retorna la funcion recursiva de media de la cantidad de variables, 0 y numeros (con asterisco en caso de tupla) dividido entre la cantidad de variables
        return mediaaux(cantvariab, 0, *numeros)/cantvariab
    elif menu==2: #Si el usuario inserto en el menu un 2, se retorna la funcion recursiva de varianza de la cantidad de variables, el resultado de la funcion recursiva de media con las variables insertadas, 0 y numeros (con asterisco en caso de tupla) dividido entre la cantidad de variables
        media=mediaaux(cantvariab, 0, *numeros)/cantvariab
        return varianzaaux(cantvariab, media, 0, *numeros)/cantvariab
    else: #Si el usuario inserto un 3 (ultima variable posible):
        media=mediaaux(cantvariab, 0, *numeros)/cantvariab #Variable media es igual a la funcion recursiva de media de la cantidad de variables, 0 y numeros (con asterisco en caso de tupla) dividido entre la cantidad de variables
        varianza=varianzaaux(cantvariab, media, 0, *numeros)/cantvariab #Varianza es igual a la funcion recursiva de varianza de la cantidad de variables, la variable media, 0 y numeros (con asterisco en caso de tupla) dividido entre la cantidad de variables
        return int(math.sqrt(varianza)) #Se retorna el valor entero de la raiz cuadrada de varianza
    
def mediaaux(cantidad, posicion,*numeros):
    if cantidad==0: #Si la cantidad es igual a 0, se para la funcion recursiva retornando un 0
        return 0
    else: #Si no se cumple lo anterior se retorna numero de la posicion mas la funcion recursiva de media con cantidad menos 1, posicion mas 1 y numeros
        return numeros[posicion]+mediaaux(cantidad-1,posicion+1,*numeros)
    
def varianzaaux(cantidad, media, posicion,*numeros):
    if cantidad==0: #Si la cantidad es igual a 0, se para la funcion recursiva retornando un 0
        return 0
    else: #Si no se cumple lo anterior se retorna numero de la posicion menos la media, todo eso elevado a la dos mas la funcion recursiva de varianza con cantidad menos 1, media, posicion mas 1 y numeros
        return (numeros[posicion]-media)**2+varianzaaux(cantidad-1,media,posicion+1,*numeros)

'''2. Cercanos
Entrada: Dos numeros, los cuales se calculara si ambos son cercanos
Salida: Un booleano que indica True por si son cercanos o False por si no lo son
Restriccion: Ninguna'''
def cercanos():
    numcondicion=False #Condicion en caso de que el usuario inserte caracteres distintos a numeros
    while not numcondicion: #Mientras la condicion sea falsa, se repite lo siguiente
        try: #Se inserta un try para evitar errores en el programa en caso de que se inserten caracteres invalidos
            num1=input("Favor insertar un numero: ") #Se pide al usuario insertar un numero
            num2=input("Favor insertar numero para comparar si son cercanos: ") #SE pide otra vez al usuario insertar un numero de referencia para comparar si son cercanos o no
            numcondicion=True #Si lo insertado fueron numeros, la condicion se vuelve True para evitar el while
        except: #Si lo insertado anteriormente era invalido, se retorna mensaje de error
            return "Error: Datos insertados no son numericos"
    numAux1=num1 #Se crea variable numAux1 y se le iguala a num1 para modificarla en caso que cumpla con ciertas condiciones
    numAux2=num2 #Se crea variable numAux2 y se le iguala a num2 para modificarla en caso que cumpla con ciertas condiciones
    if numAux1<0 or numAux2<0: #Si numAux1 o numAux2 o ambas son menores a 0, se realiza lo siguiente:
        numAux1=abs(numAux1) #numAux1 se convierte en valor absoluto de numAux1
        numAux2=abs(numAux2) #numAux2 se convierte en valor absoluto de numAux2
    if isinstance(numAux1, float) or isinstance(numAux2, float): #Si numAux1 o numAux2 o ambas son numeros reales, se realiza lo siguiente:
        numAux1=math.trunc(numAux1) #numAux1 se convierte en valor truncado de numAux1
        numAux2=math.trunc(numAux2) #numAux2 se convierte en valor truncado de numAux2
    if numAux1==0 or numAux2==0: #Si numAux1 o numAux2 o ambas son iguales a cero, la funcion retorna un falso, porque ambos numeros no tienen multiplos
        return False
    else: #Si no se cumple lo anterior, se retorna respuesta de numAux1 y numAux2
        return respuestacercanos(numAux1, numAux2)

def cercanosaux(num, divisor):
    if num==divisor: #Si num es igual a divisor, se para la funcion recursiva retornando 0
        return 0
    if num%divisor==0: #Si el residuo entre num y divisor es igual a 0, se retorna la suma de divisor mas la funcion auxiliar de cercanosaux de num y divisor mas 1
        return divisor+cercanosaux(num, divisor+1)
    else: #Si no se cumple lo anterior, se retorna la funcion auxiliar de cercanosaux de num y divisor mas 1
        return cercanosaux(num, divisor+1)

def respuestacercanos(num1, num2):
    if cercanosaux(num1, 1)==cercanosaux(num2, 1): #Si la funcion auxiliar de cercanos de num1 y 1 es igual a la funcion auxiliar de cercanos de num2 y 1, se retorna True
        return True
    else: #Si no se cumple lo anterior, se retorna False
        return False

'''3. Cuenta digitos
Entrada: Un numero al cual se le contara sus digitos
Salida: Un numero indicando la cantidad de digitos que contiene el numero insertado
Restriccion: Ninguna'''
def cuentadigitos():
    numcondicion=False #Condicion en caso de que el usuario inserte caracteres distintos a numeros
    while not numcondicion: #Mientras la condicion sea falsa, se repite lo siguiente
        try: #Se inserta un try para evitar errores en el programa en caso de que se inserten caracteres invalidos
            num=input("Favor insertar numero: ") #Se pide al usuario insertar un numero
            numcondicion=True #Si lo digitado fueron numeros, la condicion se vuelve True, evitando el while
        except: #Si lo insertado anteriormente era invalido, se retorna mensaje de error
            print"Error: Datos no son validos"
    numAux=num #Se crea variable numAux y se le iguala a num para modificarla en caso que cumpla con ciertas condiciones
    if numAux==0: #Si numAux es igual a cero, se retorna un 1
        return 1
    if numAux<0: #Si numAux es menor a 0, numAux se convierte en el valor absoluto de numAux
        numAux=abs(numAux)
    if isinstance(numAux,float): #Si numAux es un numero real, se cumple lo siguiente:
        numAux1=int(numAux) #numAux1 se iguala al valor entero de numAux
        numAux2=numAux-numAux1 #numAux2 se iguala a la resta de numAux menos numAux1
        return cuentadigitosaux(numAux1)+decimal(numAux2) #Se retorna la suma de la funcion auxiliar de cuentadigitos de numAux1 mas la funcion decimal de numAux2
    else: #Si lo anterior no se cumple, se retorna la funcion auxiliar de cuentadigitos de numAux
        return cuentadigitosaux(numAux)

def decimal(num):
    if int(num*10)%10==0: #Si el residuo de el valor entero de num por 10 entre 10 es igual a 0, se retorna la funcion auxiliar de cuentadigitos del valor entero de num 
        return cuentadigitosaux(int(num))
    else: #Si no se cumple lo anterior, se retorna funcion decimal de num a la 10 
        return decimal(num*10)
     
def cuentadigitosaux(num):
    if num==0: #Si num es igual a 0, se para la funcion recursiva retornando un 0
        return 0
    else: #Si lo anterior no se cumple, se retorna 1 mas la funcion auxiliar de cuentadigitos de num entre 10
        return 1+cuentadigitosaux(num/10)
    
'''4. Apariciones
Entrada: Dos numeros: Un numero que indica el digito a investigar y otro numero como el numero donde se buscara la cantidad de "primer numero" digitos que contiene
Salida: Un numero indicando la cantidad de "primer numero" digitos en el segundo numero
Restriccion:Ninguna'''
def apariciones():
    numcondicion=False #Condicion en caso de que el usuario inserte caracteres distintos a numeros
    while not numcondicion: #Mientras la condicion sea falsa, se repite lo siguiente
        try: #Se inserta un try para evitar errores en el programa en caso de que se inserten caracteres invalidos
            num1=input("Favor insertar digito a investigar: ") #Se pide al usuario insertar un digito al cual investigar
            if num1 not in [0,1,2,3,4,5,6,7,8,9]: #Si el numero insertado no es un digito, es decir no se encuentra en el rango del 0 al 9, se retorna mensaje de error
                return "Error: Digito no valido"
            else: #Si lo anterior no se cumple, sucede lo siguiente
                num2=input("Favor insertar numero de referencia: ") #Se pide numero de referencia, en el cual se buscara el digito que inserto el usuario 
                numcondicion=True #Si lo insertado por el usuario fueron numeros, la condicion se vuelve True, evitando el while
        except: #Si lo insertado anteriormente era invalido, se retorna mensaje de error
            return "Error: Datos no son numericos"
    numAux2=num2 #Se crea variable numAux2 y se le iguala a num2 para modificarla en caso que cumpla con ciertas condiciones
    if numAux2<0: #Si numAux es menor a 0, numAux2 se iguala al valor absoluto de numAux2
        numAux2=abs(numAux2)
    if isinstance(numAux2, float): #Si el numero es real, numAux2 se convierte en el valor truncado de numAux2
        numAux2=math.trunc(numAux2)
    return aparicionesaux(num1, numAux2) #Se retorna la funcion auxiliar de apariciones de num1 y numAux2

def aparicionesaux(digito, num):
    if num==0: #Si num es igual a 0, se retorna 0
        return 0
    if num%10==digito: #Si el residuo de num entre 10 es igual a digito, se retorna la suma de 1 mas la funcion auxiliar de apariciones de digito y num entre 10
        return 1+aparicionesaux(digito, num/10)
    else: #Si no se cumple lo anterior, se retorna la funcion auxiliar de apariciones de digito y num entre 10
        return aparicionesaux(digito, num/10)