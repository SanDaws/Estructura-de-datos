#include <iostream>
// ejercicio los 4 fantasticos
void fantastic4() {
	int val;
	std::cin >> val;
	for (int n:{2,3,5,7,13})
	{
		if (n==13)
		{
			std::cout << "no es multiplo de ninguno de los primeros cuatro primos";
			break;
		}
		else if (val%n==0)
		{
			std::cout << "es multiplo de "<<n;
			break;
		}
	}

}