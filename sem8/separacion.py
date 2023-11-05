"""Una separación es un proceso por el cual una pareja sentimental determina la ruptura de la relación. En el imaginario de la mayoría de 
las personas dicho proceso involucra llantos, gritos, rupturas de vajilla, y otros elementos de drama. En la realidad, al menos cuando no 
hay hijos o mascotas de por medio, este proceso suele ser bastante civilizado y solo presenta algunos inconvenientes a la hora de repartir 
los bienes que la pareja adquirió de manera conjunta.

El caso de Fernando y Gustavo fue super civilizado, más aún porque los bienes adquiridos se limitaban a libros. Ambos son lectores 
empedernidos y adquirieron bastante mientras fueron pareja. La repartición fue bastante simple, cada quien se quedó con los libros 
que compró cada uno y con los libros comprados entre ambos llegaron a esta solución: para ser equitativos definieron que aquellos 
con ISBN par serían para Fernando y aquellos con ISBN impar serían para Gustavo. ISBN es la sigla de International Standard Book 
Number y básicamente es un identificador numérico único para libros.

Si tenemos un registro de los libros comprados por cada uno y en conjunto, ¿ayudarías a determinar con cuántos se queda cada quién?
Input

La entrada contiene una serie de líneas, no más de cien mil. Cada línea corresponde al registro de un libro y consiste en dos 
valores separados entre sí por un espacio en blanco. El primero corresponde al ISBN y por simplicidad asumiremos que es un valor 
entero positivo de no más de 13 dígitos. El segundo corresponde a una letra mayúscula que define al respectivo comprador: F para Fernando 
y G para Gustavo. Si un libro fue comprado por ambos aparecerá como dos registros, uno con cada letra. La entrada termina con una línea 
que contiene el valor 0 y que no corresponde a un ISBN.
Output

La salida debe contener una única línea con dos valores separados entre sí por un espacio en blanco: la cantidad de libros con que se queda Fernando y Gustavo. """
"""
1002 F
1005 G
1003 G
1004 G
1001 F
1002 G
1005 F
"""
def datotastico(a):
    
    if int(a[-1])% 2== 0: return 1
    else :return 0
f,g=set(),set()
while True:
    dato=input(). split()
    if "0" in dato and not (("G"  in dato) or ("F" in dato)): break
    if "F" in dato  : f.add(dato[0])
    elif "G"  in dato : g.add(dato[0])
    if (dato[0]in f) and(dato[0] in g):
        if datotastico(dato[0])==1: g.remove(dato[0])
        else: f.remove(dato[0])

fr=len(f.difference(g))
gr=len(g.difference(f))
print(fr,gr)



