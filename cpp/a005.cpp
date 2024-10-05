#include <iostream>
using namespace std;

int main() {
	int n,a,b,c,d,e;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b >> c >> d ;
		if (b - a == d - c) {
			e = d + (b - a);
			cout << a << " " << b << " " << c << " " << d << " " << e << '\n';
		}
		else if (b/a==d/c){
			e = d * (b / a);
			cout << a << " " << b << " " << c << " " << d << " " << e << '\n';
		}
	}

}