/*
    題目敘述

    寫一個涵式來計算一個金屬塊的價值。函式原型如下：

    ```cpp
    int value(int type, int width, int height, int length);
    ```
    一個金屬塊的價值由金屬類型及長、寬、高來決定。共有六種金屬：金、銀、銅、鉛、鐵以及鈦；
    六種金屬的價值依序為：30、10、4、5、3、9。一個金屬塊必須被切成同樣大小的正方體才能販售，
    並且不能有任何剩餘的金屬。例如，一個 4 x 8 x 2 大小的金屬塊只能被切成 2 x 2 x 2 
    或是 1 x 1 x 1 小的正方體。而金屬正方體的價值計算方式為其體積的平方乘以該金屬單位價值。
    因此，2 x 2 x 2 大小的正方體金塊價值為 8 x 8 x 30 = 1920；而4 x 8 x 2 
    的金塊，最高價值就是 1920 x 8 = 15360。

    現在，在給予金屬類型 (type)、長 (length)、寬 (width)、高 (height) 
    的狀況下，計算該金屬塊的最大價值為何。你只需要寫 value 函式，主程式在下面有提供。

    輸入格式
    type 這個參數將會表明該金屬塊為哪種金屬。若是 79，代表是金。而 47、29、82、26、22 
    分別代表銀、銅、鉛、鐵以及鈦。width、height、length 代表該金屬塊的長、寬、高。

    輸出格式
    涵式必須確認 type 參數。若 type 並非上述六種金屬，必須回傳 -1。接著，
    函式必須確認三個維度的長度。width、 height、 length 皆能以 int 
    變數儲存。然而任何一個維度的值為零或負時，必須回傳 -2。若參數都沒有問題，
    請計算並回傳輸入的金屬塊價值。我們保證金屬價值能用 int 變數儲存。

    輸入範例 1
    79 4 8 2

    輸出範例 1
    15360

    輸入範例 2
    100 -4 8 2

    輸出範例 2
    -1

    輸入範例 3
    79 0 8 2

    輸出範例 3
    -2

    注意事項

    請根據下列的 main () 函式為基礎，加上 value () 函式。

    ```cpp
    // add your value() based on this code
    #include <stdio.h>

    int main ()
    {
        int type, width, height, length;
        scanf ( "%d%d%d%d", &type, &width, &height, &length );
        printf ( "%d", value ( type, width, height, length ) );
        return 0;
    }
    ```
*/

/* add your value() based on this code */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define GOLD    79
#define GOLDP   30
#define SILVER  47
#define SILVERP 10
#define COPPER  29
#define COPPERP 4
#define IRON    26
#define IRONP   3
#define LED     82
#define LEDP    5
#define TITIUM  22
#define TITIUMP 9

int value(int, int, int, int);
int gcd(int, int);

int main ()
{
    int type, width, height, length;
    scanf ( "%d%d%d%d", &type, &width, &height, &length );
    printf ( "%d\n", value ( type, width, height, length ) );
    return 0;
}

/*
    一個金屬塊的價值由金屬類型及長、寬、高來決定。共有六種金屬：金、銀、銅、鉛、鐵以及鈦；
    六種金屬的價值依序為：30、10、4、5、3、9。一個金屬塊必須被切成同樣大小的正方體才能販售，
    並且不能有任何剩餘的金屬。例如，一個 4 x 8 x 2 大小的金屬塊只能被切成 2 x 2 x 2 
    或是 1 x 1 x 1 小的正方體。而金屬正方體的價值計算方式為其體積的平方乘以該金屬單位價值。
    因此，2 x 2 x 2 大小的正方體金塊價值為 8 x 8 x 30 = 1920；而 4 x 8 x 2 
    的金塊，最高價值就是 1920 x 8 = 15360。

    Pseduo cod:
    1. get gcd for width, length, and height
    2. calculate the total number of cubes based on the width, length, and 
        height
    3. calculate the value based on the type of metal, volume, and amount

    Arguments:
        type:   integer, type of metal
        width:  integer, width of the given metal
        height: integer, height of the given metal
        length: integer, length of the given metal

    Return: integer, value of the given metal
*/
int value(int type, int width, int height, int length)
{
    // check the metal type
    if (type != GOLD && type != SILVER && type != COPPER && \
        type != LED && type != IRON && type != TITIUM)
        return -1;

    // check the values of width, height, and length
    if (width <= 0 || height <= 0 || length <= 0)
        return -2;

    // get the largest possible cube 
    int size = gcd(width, gcd(height, length));
    // printf ("size = %d\n", size);

    // calculate the number of cubs
    int cubes = width * height * length / (size * size * size);
    int vol = size * size * size;

    // calculate the price
    switch (type){
        case GOLD:          // gold
            return cubes * vol * vol * GOLDP;
        case SILVER:        // silver
            return cubes * vol * vol * SILVERP;
        case COPPER:        // copper
            return cubes * vol * vol * COPPERP;
        case LED:           // led
            return cubes * vol * vol * LEDP;
        case IRON:          // iron
            return cubes * vol * vol * IRONP;
        case TITIUM:        // titium
            return cubes * TITIUMP;
        default:
            printf("Recheck program with type %d\n", type);
            return -1;
    }
}

/*
    calculate gcd of two intergers

    gcd(i, j) = 0,                  if i mod j = 0
              = gcd(i, i mod j),    otherwise

    Pseudo code:
    using recursive to get gcd
    1. if i mod j = 0, return j
    2. if i mod j <> 0, call itself with gcd(j, i mod j)

    Arguments:
        i: integer, the first integer
        j: integer, the second integer
*/
int gcd(int i, int j)
{
    if (i % j == 0)
    {
        return j;
    }
    else
    {
        return gcd(j, i % j);
    }
}