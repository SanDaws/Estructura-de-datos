#include <iostream>
#include <String>
using namespace std;

/*primero hagamos un poco lo basico*/

void info() {
	int x;
	int* ptrx=&x;//nullpointer
	*ptrx = 5;
	std::cin >> *ptrx;
	int* arraya = new int[*ptrx];// arreglo dinamico
	const int h = 7;
	int arrayH[h] = { 12,32,41,56,280,6,255 };//arreglo tradicional, depende de una constante
	arrayH[2] = 0;//cambio de valores en un array


	int arrayY[5] = { 12,21,21 };// es obligatorio saber el tamaño que se reserbara en el array
	arrayY[3] = 57;	
	arrayY[4] = 823;// y seguir agregando elementos es probable



	for (int i = 0; i < h; i++)
	{
		std::cout << arrayH[i] << std::endl;

	}
}
void insertar() {
	int tempNum, tempval;
	int numeros[12] = { 12,42,57,84,5 };
	cin >> tempNum;
	cin >> tempval;
	numeros[tempNum] = tempval;
	for (int i : numeros) {
		cout << i << endl;

	}
}
//sandbox
int main(){
	



	



}