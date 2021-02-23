#include <stdio.h>
#define resta(a) a-1
int suma(int x, int y);
int main(int argc, char const *argv[])
{
    int a,b;
    printf("INGRESE EL PRIMER VALOR: \n");
    scanf("%d",&a);
    printf("INGRESE EL SEGUNDO VALOR: \n");
    scanf("%d",&b);

    printf("LAS SUMA ES: %d\n",suma(a,b));
    return 0;
}

int suma(int x, int y){
    int suma = x+y;
    int r = suma - (resta(x));
    return r;
}
