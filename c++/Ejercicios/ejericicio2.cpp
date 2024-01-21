#include <iostream>

void HWBilingue() {
	int val;
	std::cin >> val;
	for (int i = 0; i < val; i++) {
		const char* resul= (i % 2 != 0) ? "Hello world" : "Hola mundo";
		std::cout << resul<< std::endl;
			
	}
}