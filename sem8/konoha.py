"""
Konoha, que significa aldea oculta de la hoja, es una aldea del país del fuego, que a su vez es una de las cinco grandes naciones shinobi (shinobi significa ninja).

1) Ahora sí, al problema. Llevar un conteo de la población debe ser fácil: se suma una unidad cuando hay un nacimiento y se resta una unidad cuando hay una muerte. 
Bueno, pues resulta que en Konoha esta tarea, aparentemente tan sencilla, no lo es tanto debido a dos situaciones:

2) En la oficina de registro civil no están sistematizados sino que simplemente tienen registros en papel. El problema es que a veces dichos registros están 
duplicados o contienen errores. Los que conocen de la historia sabrán que en las naciones shinobi los muertos no necesariamente se quedan muertos. Existen jutsus 
prohibidos (jutsu significa técnica) como el Edo-tensei que pueden hacer traer a un muerto de nuevo a la vida.

Miremos un ejemplo para clarificar lo complicado del asunto:

    Hay un registro de nacimiento con el respectivo documento de identidad de un habitante de Konoha: Uchiha Madara, por lo tanto sabemos que este habitante existe

    Luego hay un registro de fallecimiento para ese documento de identidad, por tanto sabemos que ese habitante murió

    Luego hay otro registro de fallecimiento para ese documento de identidad, pero él ya estaba muerto por tanto se trata de un registro duplicado

    Luego hay un registro de resucitación para ese documento de identidad. Como en efecto ese habitante estaba muerto, ahora sabemos que de nuevo está vivo

    Luego hay otro registro de fallecimiento para ese documento de identidad. Como en efecto ese habitante estaba vivo (revivido para ser exactos), 
    ahora sabemos que de nuevo está muerto 

En total, hay 5 registros para este habitante (en orden cronológico) pero finalmente la población de Konoha solo aumento en una unidad.
Input

La entrada contiene una serie de registros ordenados cronológicamente (hasta 50000). Cada registro, de a uno por línea, contiene el documento de identidad 
(un número entero positivo menor a 1x108) y puede ser de tres tipos (sin comillas):

    "B", un espacio en blanco y el documento para indicar un nacimiento

    "D", un espacio en blanco y el documento para indicar un deceso

    "R", un espacio en blanco y el documento para indicar una resucitación

Se debe considerar que:

    Registros de nacimiento duplicados para un mismo documento deben considerarse como errores. Un registro de nacimiento de un habitante muerto o 
    resucitado también debe considerarse error.

    Un deceso solo puede considerarse válido si el habitante está vivo (o resucitado). En caso contrario debe considerarse como error.

    Un habitante solo puede estar vivo o muerto en un determinado momento. Estar -resucitado significa estar vivo.

    Una resucitación solo puede considerarse válida si el habitante está muerto. Una resucitación de un habitante vivo (o resucitado) debe considerarse como error.

La entrada finaliza con una línea con el texto "E" (sin comillas)
Output

La salida debe contener una única línea indicando la población de Konoha partiendo de una cuenta de 0 antes de procesar los registros."""
"""
B 1001
B 1003
B 1002
D 1003
B 1001
D 1002
R 1003
E
"""
vivos,muertos=set(),set()

while True:
    datos=input().split()
    if datos[0].upper()=="E":break
    if datos[0].upper()=="B" and (datos[1] in muertos)== False: vivos.add(datos[1])
    elif datos[0].upper()=="R"and (datos[1] in muertos):
        vivos.add(datos[1])
        muertos.remove(datos[1])
    elif datos[0].upper()=="D" and (datos[1] in vivos):
        vivos.remove(datos[1])
        muertos.add(datos[1])
#     print(*vivos)
#     print(*muertos)
# print(*vivos)
print(len(vivos))

