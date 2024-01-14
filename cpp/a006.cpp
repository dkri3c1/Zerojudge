#include <iostream>
#include <math.h>
using namespace std;;


int main()
{
	int a, b, c,solve1,solve2;
	cin >> a >> b >> c;
	solve1 = (-b + sqrt(b * b - 4 * a * c))/(2*a);
	solve2 = (-b - sqrt(b * b - 4 * a * c))/(2*a);
	if (b * b - 4 * a * c > 0) {
		cout << "Two different roots x1="<<solve1<<" , x2="<<solve2<<'\n';
	}
	else if (b * b - 4 * a * c == 0) {
		cout << "Two same roots x="<<solve1<<'\n';
	}
	else {
		cout << "No real root" << '\n';
	}
}
