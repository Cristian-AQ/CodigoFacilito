#include <stdio.h>

int main(){
    int num1;
    int num2;
    int resultado;

    printf("Ingrese el primer valor: \n");
    scanf("%d",&num1);//tinene dos argumentos el tipo de dato y la variable

    printf("Ingrese el segundo valor: \n");
    scanf("%d",&num2);

    resultado = num1+num2;

    printf("El resultado de la suma es:%d ",resultado);

    return 0;
}