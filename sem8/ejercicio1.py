"""En la versión original había 150 pokemones, sin embargo a lo largo de los años dicho número fue creciendo 
y creciendo. En el año 2035, luego de la versión silver-omega-8 dicho número alcanzó los 100.000.
Bueno, resulta que Felipe y Vanesa son maestros pokemón y se tomaron muy a pecho lo de "hay que atraparlos todos"
por lo que cada uno tiene miles, sino decenas de miles. De hecho, de los que tienen, cuentan con hasta más de un 
espécimen. Felipe y Vanesa se van a poke-casar y no tienen espacio en su nueva poke-casa para tantas poke-bolas. 
Por esa razón han decidido juntar sus colecciones y quedarse únicamente con un espécimen de cada pokemon. Tu tarea 
es ayudarles a determinar cuántos pokemones diferentes tiene cada uno por separado y en total.


La entrada contiene una serie de líneas, no más de 100.000. Cada línea contiene dos valores separados entre sí por
 un espacio en blanco: una letra (F o V) para especificar si es un pokemon de Felipe o Vanesa respectivamente y un 
 valor entero positivo que corresponde a la identificación del pokemon. La entrada termina con una línea que contiene 
 el carácter '#'.

La salida debe contener una única línea con tres valores separados entre sí por un espacio en blanco: la cantidad de 
pokemones diferentes de Felipe, la de Vanesa, y la de la colección conjunta."""

"""
V 13
F 10
F 12
V 10
F 11
V 14
V 13
#
3 3 5
"""

_pokeVan=set()
_pokeFer=set()#creamos conjuntos
while True:
    linea= input()
    if linea=="#": break
    linea= linea.split()
    if linea[0].upper()=="F": 
        _pokeFer.add(linea[1])
    if linea[0]=="V": _pokeVan.add(linea[1])
_pokeRestantes= _pokeFer.union(_pokeVan)
print("{a} {b} {c}".format(a=len(_pokeFer),b=len(_pokeVan),c=len(_pokeRestantes)))




