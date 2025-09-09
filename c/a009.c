#include <string.h>
#include <stdio.h>

int main()
{
    char input[10000]; char temp[10000] = {'0'};
    scanf("%s",input);
    for (int i = 0 ; i < strlen(input) ; i++)
    {
        temp[i] = input[i] - 7;
    }
    temp[strlen(input)] = '\0';
    printf("%s\n",temp);
}

// remember to initial the array & using += Before Think about The Initial Value XD

