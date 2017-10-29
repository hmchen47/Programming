/* 
 * Problem 2.3
 * Consider int val=0xCAFE; Write expressions using bitwise operators that 
 * do the following:
 *  (a) test if atleast three of last four bits (LSB) are on
 *  (b) reverse the byte order (i.e., produce val=0xFECA)
 *  (c) rotate fourbits (i.e., produce val=0xECAF)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    int var = 0xCAFE;

    // (a) test if atleast three of last four bits (LSB) are on
    int tmp1 = 0xF & var;
    if ((tmp1 == 0x7) || (tmp1 == 0xB) || (tmp1 == 0xD) || (tmp1 == 0xE)) {
        printf("Last four bits of 0x%04X containg at least three bits are on\n", var);
    } else {
        printf("Last four bits of 0x%X NOT containg at least three bits are on\n", var);        
    }

    // (b) reverse the byte order (i.e., produce val=0xFEAC)
    tmp1 = ((var << 8) & 0xFF00) | ((var >> 8) & 0xFF);
    tmp1 = ((var & 0xFF) << 8) | (var >> 8);
    printf("reversed hexdecimal of 0x%X: 0x%X\n", var, tmp1);

    // (c) rotate fourbits (i.e., produce val=0xECAF)
    tmp1 = ((var >> 4) & 0x0FFF) | ((var << 12) & 0xF000);
    tmp1 = (var >> 4) | ((var & 0xF) << 12);
    printf("rotate fourbits of 0x%X: 0x%X\n", var, tmp1);

    return 0;
}

