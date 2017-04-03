#include <iostream>

using namespace std;

int main()
{
	
	int nome;

	cout << "Digite um numero de 1 a 5" <<  '\n' << endl;
	cin >> nome;

	if( nome == 1 )
		cout << "Jefersson" << '\n' << endl;

	else if(nome == 2)
		cout << "Janaina" << '\n' << endl;

	else if(nome == 3)
		cout << "Adriana" << '\n' << endl;

	else if(nome == 4)
		cout << "Betinho" << '\n' << endl;

	else if(nome == 5)
		cout << "Hevellyn" << '\n' << endl;

	return 0;
}