// gcc -g bitcount.c -o bc

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    unsigned int v = atoi(argv[1]); 
    unsigned int c;
    unsigned int cnt = 0;

    // v =atoi( argv[1] );

    printf("v = 0x%x\n", v);

    for (c = 0; v; c++)
    {
        v &= v - 1;
        cnt ++;
        printf("%d: v = 0x%x\n", c, v);
    }

    printf("bit count= %d\n", cnt);

    return 0;
}
