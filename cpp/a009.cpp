#include <bits/stdc++.h>
using namespace std;

int main()
{
    string n;
    string temp;
    cin >> n;
    for (int i = 0 ; i < n.size() ; i++)
    {
        temp += char(n[i]-7) ;
    }
    cout << temp << '\n';
}