#include <stdio.h>

long factorial(long numero);
int main(int argc, char const *argv[])
{
    int numero,i;
    printf("INGRESA UN NUMERO\n");
    scanf("%d",&numero);
    for (i = 0; i <=numero; i++)
    {
        printf("%ld\n",factorial(i));
    }
    
    return 0;
}

long factorial(long numero){
    if (numero<=1)
    {
        return 1;
    }else
    {
        return(numero*factorial(numero-1));
    }
}
