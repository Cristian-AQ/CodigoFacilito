#include <stdio.h>

void cubo();
int main(int argc, char const *argv[])
{
    int num = 5;
    printf("EL PRIMER VALOR ES: %d\n",num);
    cubo(&num);
    printf("EL NUEVO VALOR ES: %d\n",num);
    return 0;
}
void cubo(int *a){
    *a = *a * *a * *a;
}