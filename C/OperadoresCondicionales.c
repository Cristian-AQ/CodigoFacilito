#include <stdio.h>

int main(){
    int edad;
    printf("Ingrese su edad: \n");
    scanf("%d",&edad);
    if (edad>=18)
    {
        printf("eres mayor de edad\n");
    }else{
        printf("eres menor de edad\n");
    }
    return 0;
}