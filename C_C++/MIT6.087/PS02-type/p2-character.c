/* 
 * Pratical Programming in C
 *
 * Check the type of input character
 * 
 * type of character: 
 *  lower case letter, upper case letter, digit, white space
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    while(true)
    {
        // input of character
        char character;
        if (scanf("%c", &character) != 1)
        {
            printf("Input should be a character");
        }

        // identify the character
        if ((character >= 'a') && (character <= 'z')) {
            printf("%c is a lower case letetr\n", character);
        } else if ((character >= 'A') && (character <= 'Z')) {
            printf("%c is a upper case letetr\n", character);
        } else if ((character >= '0') && (character <= '9')) {
            printf("%c is a digit\n", character);
        } else if (character == ' ' || character == '\t' ||
                character == '\n' || character == '\r') {
            printf("%c is a whitespace\n", character);
        } else {
            printf("%c is an unknow character\n", character);
        }
    }

    return 0;
}
