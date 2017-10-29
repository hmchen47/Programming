/* 
 * Using precedence rules, evaluate the following expressions and determine 
 * the value of the variables(without running the code). Also rewrite them 
 * using parenthesis to make the order explicit.
 *  (a) Assume (x=0xFF33,MASK=0xFF00).Expression: c=x & MASK ==0;
 *  (b) Assume (x=10,y=2,z=2;).Expression: z=y=x++ + ++y∗2;
 *  (c) Assume (x=10,y=4,z=1;).Expression: y>>= x&0x2 && z
 *
 * compile: gcc -Werror -g -O0 -o prec p4-precedence.c
 * debug:   gdb prec
 * memory:  valgrind -leak-check=full prec
 * usgae:   ./prec
 */

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // inputs
    int x, y, z, c, MASK;

    x = 0xFF33; MASK = 0xFF00;
    c = x & MASK == 0;
    printf("c = x & MASK == 0: x = %X->%X, c = %d->%d\n", 0xFF33, x, 0, c);

    x = 10, y = 2, z = 2;
    z = y = x++ + ++y * 2;
    printf("z = y = x++ + ++y * 2: x = %d->%d, y = %d->%d, z = %d->%d\n", \
        10, x, 2, y, 2, x);

    x = 10, y = 4, z = 1;
    y >>= x & 0x2 && z;
    printf("y >>= x & 0x2 && z: x = %d->%d, y = %d->%d, z = %d->%d\n", \
        10, x, 4, y, 1, z);

    return 0;
}