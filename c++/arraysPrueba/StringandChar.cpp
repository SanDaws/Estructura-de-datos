#include<string>
#include<iostream>
using namespace std;

struct entity
{
	
	//aqui hablaremos sobre String y char
	//un string es una cadena de caracteres
	const char* cadena = "esto es una cadena de caracteres";
	const char *otracadena = "esto es otra cadena";// el problema es que usamos un pointer, asi que la informacion almacenada no puede seralterada
	void whitarray() {
		const char sz[] = "hello";// esto tambien es una cadena, pero es dentro de un array, hace mas facil modificarla
	}
	//std:: esto significa estandar, hace que la libreria use un apartado estandar de creacion del elemento necesario
	string string = "esto ya es una cadena de caracteres creada";// incluir String trae ciertas funciones
	

	/*momento randonm*/
	
};