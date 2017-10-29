/*
 * Program to test the size of different data types and their max and min 
 * values.
 *
 * data types: 
 *  char, unsigned char, short, unsigned short, 
 *  short int, unsigned short int, int, unsigned int, 
 *  long, unsligned long, float, double
 * 
 * Check the files: limits.h, float.h, and values
 * 
 * compile: gcc -Wall -g -O0 --std=c11 -o pa21-limit pa21-limits.c
 * debug: gdb pa21-limit
 * memory: valfrind -leack-checl=full ps21-limit
 * usage: ./pa21-limit
 *
 * ref: http://en.cppreference.com/w/c/types/limits
 */

#include <stdio.h>
#include <limits.h>
#include <float.h>
#include <stdint.h>
#include <wchar.h>
#include <math.h>

int main(void)
{
    printf("\ncahr-related types: \n");
    printf("  SIGNED CHAR: size - %d byte \n    min = %d, max = %d\n", \
        sizeof(signed char), SCHAR_MIN, SCHAR_MAX);
    printf("  UNISGNED CHAR: size - %d byte \n    min = %d, max = %d\n", \
        sizeof(unsigned char), 0, UCHAR_MAX);
    printf("  CHAR: size - %d byte \n     min = %u, max = %u\n", \
        sizeof(char), SCHAR_MIN, SCHAR_MAX);

    printf("\nshort-related types: \n");
    printf("  SIGNED SHORT INT: size - %d byte \n    min = %d, max = %d\n", \
        sizeof(signed short int), SHRT_MIN, SHRT_MAX);
    printf("  UNSIGNED SHORT INT: size - %d byte \n    min = %u, max = %u\n", \
        sizeof(unsigned short int), 0, USHRT_MAX);
    printf("  SIGNED SHORT: size - %d byte \n    min = %d, max = %d\n", \
        sizeof(signed short), SHRT_MIN, SHRT_MAX);
    printf("  UNSIGNED SHORT: size - %d byte \n    min = %u, max = %u\n", \
        sizeof(unsigned short), 0, USHRT_MAX);

    printf("\nint-related types: \n");
    printf("  SIGNED INT: size - %d byte \n    min = %d, max = %d\n", \
        sizeof(signed int), INT_MIN, INT_MAX);
    printf("  UNSIGNED INT: size - %d byte \n    min = %u, max = %u\n", \
        sizeof(unsigned int), 0, UINT_MAX);

    printf("\nlong-related types: \n");
    printf("  SIGNED LONG INT: size - %d byte \n    min = %ld, max = %ld\n", \
        sizeof(signed long int), LONG_MIN, LONG_MAX);
    printf("  UNSIGNED LONG INT: size - %d byte \n    min = %u, max = %lu\n", \
        sizeof(unsigned long int), 0, ULONG_MAX);
    printf("  SIGNED LONG: size - %d byte \n    min = %ld, max = %ld\n", \
        sizeof(signed long), LONG_MIN, LONG_MAX);
    printf("  UNSIGNED LONG: size - %d byte \n    min = %u, max = %lu\n", \
        sizeof(unsigned long), 0, ULONG_MAX);

    printf("\nlong long-related types: \n");
    printf("  SIGNED LONG INT: size - %d byte \n    min = %lld, max = %lld\n", \
        sizeof(signed long long int), LLONG_MIN, LLONG_MAX);
    printf("  UNSIGNED LONG INT: size - %d byte \n    min = %u, max = %llu\n", \
        sizeof(unsigned long long int), 0, ULLONG_MAX);
    printf("  SIGNED LONG: size - %d byte \n    min = %lld, max = %lld\n", \
        sizeof(signed long long), LLONG_MIN, LLONG_MAX);
    printf("  UNSIGNED LONG: size - %d byte \n    min = %u, max = %llu\n", \
        sizeof(unsigned long long), 0, ULLONG_MAX);

    printf("\nfloat-related types: \n");
    printf("  float: size - %d byte \n    min = %f\n    max = %f\n", \
        sizeof(float), FLT_MIN, FLT_MAX);
    printf("  float: size - %d byte \n    min = %d\n    max = %d\n", \
        sizeof(float), FLT_MIN_EXP, FLT_MAX_EXP);

    printf("\ndouble-related types: \n");
    printf("  double: size - %d byte \n    min = %f\n    max = %f\n", \
        sizeof(double), DBL_MIN, DBL_MAX);
    printf("  double: size - %d byte \n    min = %d\n    max = %d\n", \
        sizeof(double), DBL_MIN_EXP, DBL_MAX_EXP);

    printf("\nLimits of library types: \n");
    printf("  PTRDIFF_MIN    = %td\n", PTRDIFF_MIN);
    printf("  PTRDIFF_MAX    = %+td\n", PTRDIFF_MAX);
    printf("  SIZE_MAX       = %zu\n", SIZE_MAX);
    printf("  SIG_ATOMIC_MIN = %+jd\n",(intmax_t)SIG_ATOMIC_MIN);
    printf("  SIG_ATOMIC_MAX = %+jd\n",(intmax_t)SIG_ATOMIC_MAX);
    printf("  WCHAR_MIN      = %+jd\n",(intmax_t)WCHAR_MIN);
    printf("  WCHAR_MAX      = %+jd\n",(intmax_t)WCHAR_MAX);
    printf("  WINT_MIN       = %jd\n", (intmax_t)WINT_MIN);
    printf("  WINT_MAX       = %jd\n", (intmax_t)WINT_MAX);    
    printf("\n");


    printf("Limits of integer types: \n");
    printf("  CHAR_BIT   = %d\n", CHAR_BIT);
    printf("  MB_LEN_MAX = %d\n", MB_LEN_MAX);
    printf("\n");
 
    printf("  CHAR_MIN   = %+d\n", CHAR_MIN);
    printf("  CHAR_MAX   = %+d\n", CHAR_MAX);
    printf("  SCHAR_MIN  = %+d\n", SCHAR_MIN);
    printf("  SCHAR_MAX  = %+d\n", SCHAR_MAX);
    printf("  UCHAR_MAX  = %u\n",  UCHAR_MAX);
    printf("\n");
 
    printf("  SHRT_MIN   = %+d\n", SHRT_MIN);
    printf("  SHRT_MAX   = %+d\n", SHRT_MAX);
    printf("  USHRT_MAX  = %u\n",  USHRT_MAX);
    printf("\n");
 
    printf("  INT_MIN    = %+d\n", INT_MIN);
    printf("  INT_MAX    = %+d\n", INT_MAX);
    printf("  UINT_MAX   = %u\n",  UINT_MAX);
    printf("\n");
 
    printf("  LONG_MIN   = %+ld\n", LONG_MIN);
    printf("  LONG_MAX   = %+ld\n", LONG_MAX);
    printf("  ULONG_MAX  = %lu\n",  ULONG_MAX);
    printf("\n");
 
    printf("  LLONG_MIN  = %+lld\n", LLONG_MIN);
    printf("  LLONG_MAX  = %+lld\n", LLONG_MAX);
    printf("  ULLONG_MAX = %llu\n",  ULLONG_MAX);
    printf("\n");

    printf("Limits of floating point types: \n");
    printf("  FLT_RADIX    = %d\n", FLT_RADIX);
    printf("  DECIMAL_DIG  = %d\n", DECIMAL_DIG); // C99
    printf("  FLT_MIN      = %e\n", FLT_MIN);
    printf("  FLT_MAX      = %e\n", FLT_MAX);
    printf("  FLT_EPSILON  = %e\n", FLT_EPSILON);
    printf("  FLT_DIG      = %d\n", FLT_DIG);
    printf("  FLT_MANT_DIG = %d\n", FLT_MANT_DIG);
    printf("  FLT_MIN_EXP  = %d\n",  FLT_MIN_EXP);
    printf("  FLT_MIN_10_EXP  = %d\n",  FLT_MIN_10_EXP);
    printf("  FLT_MAX_EXP     = %d\n",  FLT_MAX_EXP);
    printf("  FLT_MAX_10_EXP  = %d\n",  FLT_MAX_10_EXP);
    printf("  FLT_ROUNDS      = %d\n",  FLT_ROUNDS);
    printf("  FLT_EVAL_METHOD = %d\n",  FLT_EVAL_METHOD); // C99
    printf("  FLT_HAS_SUBNORM = %d\n",  FLT_HAS_SUBNORM);   // C11
    printf("\n");

    printf("Limits of floating point types: \n");


    return 0;
}


/*
cahr-related types: 
  SIGNED CHAR: size - 1 byte 
    min = -128, max = 127
  UNISGNED CHAR: size - 1 byte 
    min = 0, max = 255
  CHAR: size - 1 byte 
     min = -128, max = 127

short-related types: 
  SIGNED SHORT INT: size - 2 byte 
    min = -32768, max = 32767
  UNSIGNED SHORT INT: size - 2 byte 
    min = 0, max = 65535
  SIGNED SHORT: size - 2 byte 
    min = -32768, max = 32767
  UNSIGNED SHORT: size - 2 byte 
    min = 0, max = 65535

int-related types: 
  SIGNED INT: size - 4 byte 
    min = -2147483648, max = 2147483647
  UNSIGNED INT: size - 4 byte 
    min = 0, max = -1

long-related types: 
  SIGNED LONG INT: size - 4 byte 
    min = -2147483648, max = 2147483647
  UNSIGNED LONG INT: size - 4 byte 
    min = 0, max = -1
  SIGNED LONG: size - 4 byte 
    min = -2147483648, max = 2147483647
  UNSIGNED LONG: size - 4 byte 
    min = 0, max = -1

long long-related types: 
  SIGNED LONG INT: size - 8 byte 
    min = -9223372036854775808, max = 9223372036854775807
  UNSIGNED LONG INT: size - 8 byte 
    min = 0, max = -1
  SIGNED LONG: size - 8 byte 
    min = -9223372036854775808, max = 9223372036854775807
  UNSIGNED LONG: size - 8 byte 
    min = 0, max = -1

float-related types: 
  float: size - 4 byte 
    min = 0.000000 byte 
    max = 340282346638528859811704183484516925440.000000
  float: size - 4 byte 
    min = -125
    max = 128

double-related types: 
  double: size - 8 byte 
    min = 0.000000 byte 
    max = 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000
  double: size - 8 byte 
    min = -1021
    max = 1024
*/