#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define lenght 2

int size;
struct dog
{
    char name[20];
    char *P_name;
}dogs[lenght];


int main(int argc, char const *argv[])
{
    int i;
    for ( i = 0; i < lenght; i++)
    {
        printf("INGRESE EL NOMBRE DEL PERRO:\n");
        scanf("%s",dogs[i].name);
        size = strlen(dogs[i].name);
        printf("%d\n",size);
        dogs[i].P_name = malloc(size * sizeof(char));
        if (dogs[i].name==NULL)
        {
            printf("ERROR AL ASIGNAR MEMORIA\n");
        }else
        {
            strcpy(dogs[i].P_name,dogs[i].name);
        }
    }
    for ( i = 0; i < lenght; i++)
    {
        printf("EL NOMBRE DEL PERRO ES %s\n",dogs[i].P_name);
    }
    return 0;
}
