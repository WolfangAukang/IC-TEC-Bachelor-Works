from Persona import *
lp=[]
for i in range(4):
	p=Persona()
	p.setIden(raw_input("Identificacion: "))
	p.setNombre(raw_input("Nombre: "))
	p.setFechaNac(raw_input("Fecha de Nacimiento: "))
	lp.append(p)

for i in lp:
	print (i.toString())
