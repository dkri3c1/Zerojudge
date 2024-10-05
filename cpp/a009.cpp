#include <iostream>
using namespace std;;
#include <string>


int main()
{
	string a;
	while (getline(cin,a))
	{
		for (int i = 0; i < a.length(); i++) {
			cout << char(int(a[i]-7));
		}
		cout << '\n';
	}
}