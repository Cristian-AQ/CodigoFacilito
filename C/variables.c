#include <stdio.h>

int main(){
    char a = 'A';// 1 bytes
    int b = 5;// 2 bytes
    short c = -1; // 2 bytes
    unsigned int d = 10;// 2 bytes; el unsigned espara positivos
    long l = 5932;// 4 bytes
    float e = 72.532;// 4 bytes
    double g = 12323.877658;// 8 bytes
    printf("%c\n",a);
    printf("%d\n",d);
    printf("%f\n",e);// tanto para float como double se utiliza %f
    printf("%.2f\n",e);//redondeo a dos decimales
    return 0;
}