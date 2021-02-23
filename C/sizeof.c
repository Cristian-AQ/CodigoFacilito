#include <stdio.h>

size_t getsize();
int main(int argc, char const *argv[])
{
    float arreglo[20];
    printf("EL NUMERO DE BYTES EN EL ARREGLO ES: %lu\n",sizeof(arreglo));
    //lu permite imprimir el valor en bytes
    printf("EL NUMERO DE BYTES DEVUELTOS POR GETSIZE ES: %lu\n",getsize(arreglo));
    return 0;
}

size_t getsize(float *ptr){
    return sizeof(ptr);
}
