#include <stdio.h>

struct perro
{
    char nombre[30];
    int edadMeses;
    float peso;
}perro1={"chikorita",10,3.50};

int main(int argc, char const *argv[])
{
    printf("LOS DATOS DE MI MASCOTA SON: \n NOMBRE: %s\n EDAD: %d\n PESO: %.2f\n",perro1.nombre,perro1.edadMeses,perro1.peso);//%s usado para cadena de caracteres
    return 0;
}
