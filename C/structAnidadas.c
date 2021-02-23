#include <stdio.h>
#define length 2

struct owner
{
    char nombre[20];
    char direccion[30];
};

struct dog
{
    char nombre[20];
    int edadMeses;
    struct owner ownerDog;
}dogs[length];

int main(int argc, char const *argv[])
{
    int i;
    for ( i = 0; i < length; i++)
    {
        printf("%i. NOMBRE DEL PERRO: \n",i+1);
        scanf("%s",&dogs[i].nombre);
        printf("%i. EDAD DEL PERRO EN MESES: \n",i+1);
        scanf("%d",&dogs[i].edadMeses);
        printf("%i. NOMBRE DEL DUEÑO: \n",i+1);
        scanf("%s",dogs[i].ownerDog.nombre);
        printf("%i. DIRECCION DEL DUEÑO DEL PERRO: \n",i+1);
        scanf("%s",dogs[i].ownerDog.direccion);
    }
    for ( i = 0; i < length; i++)
    {
        printf("%i. NOMBRE DEL PERRO: %s\n ",i+1,dogs[i].nombre);
        printf("%i. EDAD DEL PERRO EN MESES: %d\n",i+1,dogs[i].edadMeses);
        printf("%i. NOMBRE DEL DUEÑO: %s\n",i+1,dogs[i].ownerDog.nombre);
        printf("%i. DIRECCION DEL DUEÑO DEL PERRO: %s\n",i+1,dogs[i].ownerDog.direccion);
    }
    
    return 0;
}
