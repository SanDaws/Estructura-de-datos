#include <iostream>
#include <string>
#include <sstream>
#include <tuple>
using namespace std;
void sumareves() {
	int cantidadDatos;
	int  num;
	string datos;
	getline(cin, datos);
	stringstream(datos) >> cantidadDatos;
	tuple<int> listaDatos;
	getline(cin, datos);
	istringstream iss(datos);
	while (iss>>num)
	{
		listaDatos = make_tuple(num);
		
	}
	num = 0;
	for (int i = cantidadDatos-1; i == 0; i--)
	{
		num = num + get<0>(listaDatos);
	}


	
}