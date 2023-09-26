"""Supongamos que tenemos un conjunto cambiante de números enteros positivos.
 Es cambiante porque pueden ingresar nuevos números, no necesariamente diferentes
 (usaremos para esto el comando "A"). Supongamos además que en un momento dado 
 queremos saber cuál es la sumatoria de todos los números de ese conjunto que
 son múltiplos de un valor M (usaremos para esto el comando "M")"""

_num=list()

#funcion de buscar multiplos
def buscarMultiplos(buscador,buscado):
   suma=0
   for n in buscado:
      if n%buscador==0:suma+=n  
   return suma
while True:
    _codigo=input()
    if _codigo=="E":break #rompe el codigo antes de continuar
    s,r=_codigo.split()
    if s=="A":
      _num.append(int(r))
    if s=="M":
       print(buscarMultiplos(int(r),_num))
       
