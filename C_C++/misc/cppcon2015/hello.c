/* 
 * The program is based on the demo in CppCon 2015
 * Give me 15 minutes and I'll Change your view of GDB
 *
 * compile: gcc -g -o hello hello.c
 * usage:   hello
 */

#include <stdio.h>

int
main(void)
{
    int i = 0;
    printf("Hello, world!\n");
    printf("i is %d\n", i);
    i++;
    printf("i is now %d\n", i);

    return 0;
}
