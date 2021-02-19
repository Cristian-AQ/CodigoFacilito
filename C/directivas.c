#include <stdio.h>
//#include "nombre del archivo"
#define CUBO(a) a*a*a // es una macro, es mas rapido que una funcion
#define PI 3.14159
int main(){
    float suma;
    int potencia = 3;
    suma = PI + 3;
    printf("LA SUMA ES: %f\n",suma);
    printf("LA POTENCIA ES: %d\n",CUBO(potencia));
    return 0;
}