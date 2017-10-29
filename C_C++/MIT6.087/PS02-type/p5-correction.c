/*
 * Problem 5
 * 
 * Determine if the following statements have any errors. If so, highlight 
 * them and explain why.
 * (a) int 2nd value=10;
 * (b) Assume (x=0,y=0,alliszero=1). alliszero =(x=1) && (y=0);
 * (c) Assume (x=10,y=3,z=0;). y=++x+y;z=z−−>x;
 * (d) Assume that we want to test if last four bits of x are on. (int 
 *     MASK=0xF;ison=x&MASK==MASK)
 *
 * compile: gcc -Werror -g --std=c11 -O0 -o correct p5-correction.c
 *          gcc -Werror -g --std=c11 -o correct p5-correction.c
 * debug:   gdb correct
 *          valigrand -leak-check=full correct
 * usage:   ./correct
 *
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) 
{
    int value_2nd = 10;
    printf("(a) int 2nd value=10; -> int value_2nd = 10;\n");


    // (b) Assume (x=0,y=0,alliszero=1). alliszero =(x=1) && (y=0);
    int xb=0, yb=0, alliszero=1;
    alliszero = (xb=1) && (yb=0);
    printf("(b) sallzero = (x=1) && (y=0) -> %d\n", alliszero);

    // (c) Assume (x=10,y=3,z=0;). y=++x+y;z=z−−>x;
    int xc=10, yc=3, zc=0;
    yc = ++xc + yc;
    zc = zc--> xc;
    printf("(c) x=10,y=3,z=0; y=++x+y;z=z-->x; -> y = %d,  z = %d\n", yc, zc);

    // (d) int MASK=0xF;ison=x&MASK==MASK
    int MASK = 0xF, x = 0x7, ison1 = 0, ison2 = 0, ison3 = 0;
    ison1=x&MASK==MASK;
    ison2 = (x&MASK) == MASK;
    ison3 = x&(MASK == MASK);
    printf("(d) int MASK=0xF;ison=x&MASK==MASK   -> ison1 = %d, x = %d\n", ison1, x);
    printf("    int MASK=0xF;ison=(x&MASK)==MASK -> ison2 = %d, x = %d\n", ison2, x);
    printf("    int MASK=0xF;ison=x&(MASK==MASK) -> ison3 = %d, x = %d\n", ison3, x);

}