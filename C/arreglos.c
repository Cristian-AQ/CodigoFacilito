#include <stdio.h>
int main(int argc, char const *argv[])
{
    int sizea,i;
    printf("INGRESE TAMAÑO DEL ARREGLO\n");
    scanf("%i",&sizea);
    int age[sizea];
    for(i = 0;i < sizea;i++)
    {
        printf("INGRESA EL VALOR: %i\n",i+1);
        scanf("%i",age[i]);
    }
    printf("LOS VALORES DEL ARREGLO SON: \n");
    for(i = 0; i < sizea; i++)
    {
        printf("%i\n",age[i]);
    }
    return 0;
}
