#include <stdio.h>

int main(int argc, char const *argv[])
{
    int casos;
    printf("INGRESA UN NUMERO: \n");
    scanf("%d",&casos);
    switch (casos)
    {
    case 1:
        printf("ELEGISTE EL PRIMER CASO\n");
        break;
    case 2:
        printf("ELEGISTE EL SEGUNDO CASO\n");
        break;
    case 3:
        printf("ELEGISTE EL TERCER CASO\n");
        break;
    default:
        printf("CASO NO ENCONTRADO\n");
        break;
    }
    return 0;
}
