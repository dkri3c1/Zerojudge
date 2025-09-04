#include <stdio.h>

int main()
{
    int a,b,c;
    scanf("%d %d",&a,&b);
    c = (a*2+b)%3;
    if (c == 0) printf("%s","普通");
    else if ( c == 1) printf("%s","吉");
    else printf("%s","大吉");
}