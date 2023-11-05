"""
Quien haya visto la trilogía original de Star Wars recordará que el Ewokés era 
la lengua hablada por los Ewoks, una especie de peluditos (no confundir con los 
Wookiees como Chewbacca) que vivían en la luna boscosa de Endor. Lo que no mucha 
gente sabe es que los Ewoks aparecieron en otras películas de la franquicia: 
Caravan of Courage: An Ewok Adventure, y Ewoks: The Battle for Endor.

Volviendo al tema del Ewokés resulta que, pese a ser una lengua primitiva, C-3PO 
fue capaz de entenderla incorporando en su base datos un traductor Ewokés-Castellano.
Input

La entrada comienza con una línea que contiene un valor entero positivo N, que corresponde 
a la cantidad de palabras del Ewokés (hasta un millón). Luego siguen N líneas, cada una con 
dos strings separados entre sí por un espacio en blanco: la palabra o expresión en Ewokés a 
la izquierda y su traducción al Castellano a la derecha. Luego siguen una serie de consultas 
(hasta 100.000), cada una en una línea. Dichas consultas corresponden a una palabra o expresión 
que se desea traducir al castellano. La entrada termina con una línea que contiene el carácter 
'#' la cual no debe procesarse.
Output

Por cada una de las consultas de la entrada se debe mostrar en una única línea la traducción 
correspondiente al español, o el mensaje (sin comillas) "Entrada no encontrada".
"""
"""
5
Aargutcha Empujar
Acha De-acuerdo
Ah-ah Agua
Akeeata Oir
Allayloo Celebrar
Ah-ah
Aargutcha
Ah-ah
Bakte
#
"""
_disionario=dict()

for i in range(int(input())):
    word= input().split()
    _disionario.update({word[0]:word[1]})
while True:
    word=input()
    if word=="#":break
    print("Entrada no encontrada" if word not in _disionario else _disionario.get(word))