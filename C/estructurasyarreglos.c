#include <stdio.h>

struct perro
{
    char nombre[30];
    int edadMeses;
    float peso;
}perros[3];

int main(int argc, char const *argv[])
{
    int i;
    for ( i = 0; i < 3; i++)
    {
        printf("%i. INGRESA EL NOMBRE DEL PERRO: \n",i+1);
        scanf("%s",&perros[i].nombre);
        printf("%i. INGRESE LA EDAD EN MESES DEL PERRO: \n",i+1);
        scanf("%d",&perros[i].edadMeses);
        printf("%i. INGRESE EL PESO DEL PERRO: \n",i+1);
        scanf("%f",&perros[i].peso);
    }

    for ( i = 0; i < 3; i++)
    {
        printf("%i. EL NOMBRE DEL PERRO ES: %s\n",i+1,perros[i].nombre);
        printf("%i. LA EDAD DEL PERRO ES: %d\n",i+1,perros[i].edadMeses);
        printf("%i. EL PESO DEL PERRO ES: %.2f\n",i+1,perros[i].peso);
    }
    
    return 0;
}
