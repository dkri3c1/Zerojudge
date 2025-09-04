#include <stdio.h>

int main()
{
    int year;
    while (scanf("%d",&year) != EOF)
    {
        if (year % 4 == 0)
        {
            if (year % 400 == 0)
            {
                printf("%s\n","閏年");
            }
            else if (year % 100 == 0)
            {
                printf("%s\n","平年");
            }
            else
            {
                printf("%s\n","閏年");
            }
        }
        else
        {
            printf("%s\n","平年");
        }
        
    }
}


