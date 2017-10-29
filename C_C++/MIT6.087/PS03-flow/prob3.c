/* 
 * Both the for loop and the do-while loop can be transformed into a simple 
 * while loop. For each of the following examples, write equivalent code 
 * using a while loop instead.
 * 
 * compile: gcc -Wall -g --std=c11 -o prob3 prob3.c
 * debug:   gdb prob3
 *          valgrind --leak-scheck=full ./prob3
 * usage:   ./prob3
 * 
 */

#include <stdio.h>
#include <stdlib.h>

int factorialF(int n) 
{
    int i , ret = 1;

    for (i = 2; i <= n; i++)
        ret *= i ;

    return ret;
}

int factorialW(int n)
{
    int i = 2, ret = 1;

    while (i <= n) {
        ret *= i;
        i++;
    }

    return ret;
}

double rand_double( ) {

    /* generate random number in [0, 1) */
    double ret = (double) rand();

    return ret / (RAND_MAX + 1.0);
}

int sample_geometric_rv(double p) {
    double q;
    int n = 0;

    do {
        q = rand_double( );
        // printf("q = %f\n", q);
        n++;
    } while (q >= p);

    return n;
}

int sample_geometric_rv_W(double p) {
    // double q;
    int n = 1;

    while (rand_double() >= p) {
        n++;
    }

    return n;
}


int sample_geometric_rv_F(double p) {
    double q;
    int n;

    q = rand_double();
    // printf("q = %f\n", q);

    for (n = 1; q >= p; n++)
    {
        q = rand_double();
        // printf("q = %f\n", q);
    }

    return n;
}

int main(void) 
{
    // problem 3-a
    int n = 10;

    printf("Problem 3-a: ");
    if (factorialF(n) == factorialW(n))
        printf("factorail - converted correctly\n");
    else
        printf("factorial - Not converted correctly\n");

    // probelm 3-b
    double p = 0.01;

    printf("Problem 3-b: \n");
    srand(1);
    printf("    do while loop result: %d\n", sample_geometric_rv(p));
    srand(1);
    printf("    while    loop result: %d\n", sample_geometric_rv_W(p));


    return 0;
}