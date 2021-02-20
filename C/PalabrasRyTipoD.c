#include <stdio.h>

int main(){
    int a = 80;
    float b = 23.5;
    float suma = a+b;
    printf("entero %d\n flotante %.2f\n double %.3f\n caracter %c\n",a, (float)a, (double)a, (char)a);
    printf("%.2f",suma);
    return 0;
}