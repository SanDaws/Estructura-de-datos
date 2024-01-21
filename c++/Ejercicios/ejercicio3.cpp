#include <iostream>
void sumatoriaPN() {
	int cont,p,n,resul;
	p = 0;
	n = 0;
	std::cin >> cont;
	for (int i = 0; i < cont; i++)
	{
		std::cin >> resul;
		resul = (resul < 0) ? n=n+resul:p=p+resul ;
	}
	std::cout << "positivos " << p << ", negativos " << n;
}