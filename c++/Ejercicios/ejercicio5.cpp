#include <iostream>
#include <math.h>
double logbasen(double numero,double n) {
	return log(numero) / log(n);
	/*el logaritmo base n de un numero x, es igual a :
				log(b)
		logn(b)=--------
				log(n)
	*/
}
void Maxpotencia() {
	double val, ren ;
	unsigned int long resul ;
	std::cin >> val;
	std::cin >> ren;
	resul = logbasen(ren, val);
	for (int i = 1; i <= resul; i++)
	{
		std::cout << pow(val,i) << std::endl;
	}
	
	
}