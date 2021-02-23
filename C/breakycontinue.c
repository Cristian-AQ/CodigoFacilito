/*
    break termina el ciclo
    continue continua el ciclo
*/
#include <stdio.h>
int main(int argc, char const *argv[])
{
    int num=0;
    while (num<=7)
    {
        if (num==2)
        {
            break;
        }
        printf("%d\n",num);
        num++;
    }
     
    return 0;
}
