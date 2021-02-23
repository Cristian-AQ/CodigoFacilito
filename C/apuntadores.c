#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a = 2;
    int *apt=&a;
    printf("%x\n",*apt);
    return 0;
}
