/* The file represents the pop quiz II for MIT 6.087
 * in Lecture 2 (page 13)
 */

#include <stdio.h>

int main(void)
{
    int x = 017; int y = 12;
    // short int s=0XFFF12;
    char c = 01; 
    unsigned char uc = -1;
/*
    enum sz1 {
        S = 0, 
        L = 3, 
        XL
    };
    enum sz2 {
        S = 0, 
        L = -3, 
        XL
    };  

    sz1 sz1_xl = XL;
    sz2 sz2_xl = XL;
*/
    // puts("hel"+"lo"); 
    puts("hel""lo");

    printf("sizeof(short int) = %i\n", sizeof(short int));
    printf("x = %i and y = %i\n", x, y);

    // printf("s = %i\n", s);

    printf("c = %c,   uc = %c\n", c, uc);

    // printf("sz1 xl = %i, sz2 xl = %i\n", sz1_xl, sz2_xl);

    return 0;
}
