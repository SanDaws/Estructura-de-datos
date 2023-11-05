"""Supongamos que en el futuro la raza humana no habita el planeta tierra. ¿Se habrá extinto? ¿se habrá mudado a otros planetas? 
Eso posiblemente será tema de otro ejercicio.
El asunto es que el planeta es habitado ahora por robots que tienen una particularidad: son capaces de reproducirse. 
Estrictamente hablando, lo que ocurre es que dos robots pueden formar pareja y usar la chatarra que abunda en el planeta para crear un "descendiente".
Siendo robots, no tienen un nombre como "Mario", o como "María", en cambio tienen un número entero positivo único que los identifica. 
Cuando dos robots con identificaciones M y N forman un descendiente, su nombre será M+N. Sin embargo, en caso que ya exista un robot con ese nombre, 
se le sumará a ese valor de a una unidad hasta encontrar un número disponible.
Obviamente, a medida que pasan las generaciones los nombres (los números) se hacen más y más largos. Si conocemos la población inicial de robots 
y todos los registros de nacimientos son fidedignos, el problema consiste en determinar si en un determinado momento algún número corresponde o 
no al nombre de algún robot.
Por cierto, los robots son inteligentes por lo que, una vez se llegue una cantidad máxima de especímenes, ya no se reproducirán más.

Input
La entrada comienza con una línea que contiene un valor entero positivo mayor a 1 que corresponde a la cantidad F de robots de la población inicial. 
Dichos robots tienen como nombre los números enteros del 1 al F. Luego sigue una serie de líneas, no más de diez mil, donde cada corresponde a un 
registro de nacimiento o una consulta. Mas específicamente, cada línea puede ser (sin las comillas):

- "new" y los valores de M y N separados por un espacio en blanco

- "search", un espacio en blanco, y un número a buscar

La entrada finaliza con una línea con el texto "#" (sin comillas)
Output

Por cada línea de entrada que comience con "search" debe haber una línea en la salida con el mensaje (sin comillas) "existe" o "no existe" según sea el caso."""