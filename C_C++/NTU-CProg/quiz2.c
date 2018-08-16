/* 
    Quiz 2 

    題目敘述
        寫一個程式計算給定日期為星期幾。輸入會先告訴程式某年的 1 月 1 號為星期幾，例如範例中 2012 年的 1 月 1 號為星期日。接著程式會收到一些日期，並要計算出給定日期為星期幾，例如範例中程式將會收到 11 月 13 號，並計算出該日期為星期二。
        (閏年計算請參考wiki)

    輸入格式
        第一行包含一個西元年以及該年的一月一日為星期幾，如範例中 2012 0。注意，0 代表星期日，1 代表星期一，以此類推。第二行會告訴程式接下來將有 n 組日期需要計算。n 的範圍為 1 至 10。接下來的 n 行，每一行將會有一組需要計算的日期(月、日)，如範例中的 11 月 13 號。若輸入的「月」有誤請輸出 -1；若輸入的「日」有誤請輸出 -2。

    輸出格式
        共會輸出 n 個數字。我們用 0 代表星期日，1 代表星期一，以此類推。若輸入的「月」有誤請輸出 -1；若輸入的 「月」無誤但「日」有誤請輸出 -2。(數字間留一個空白)

    輸入範例
        2012 0
        5
        11 13
        11 14
        11 15
        13 1
        1 200
    輸出範例
    (請務必依照範例格式填寫，數字間留一個空白，否則系統將會判定答案錯誤)
        2 3 4 -1 -2
*/

#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    // read in the year and week day of the first day of the year
    int year = 0, day1st = 0;
    scanf("%d %d", &year, &day1st);

    // calculate leap day of the year
    int leapdays;
    if (year % 4 != 0)
    {
        leapdays = 28;
    }
    else if (year % 100 != 0)
    {
        leapdays = 29;
    }
    else if (year % 400 != 0)
    {
        leapdays = 28;
    }
    else
    {
        leapdays = 29;
    }

    printf ("lead days= %d\n", leapdays);

    // create dictionary for days of the month
    int daysOfMonth[12] = {31, leapdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // read number of inputs
    int inputNum = 0;
    scanf("%d", &inputNum);

    int record[inputNum];

    for (int cnt = 0; cnt < inputNum; cnt++)
    {
        int daysOfInput = 0, month = 0, date = 0;
        scanf("%d %d", &month, &date);

        if (month > 12 || month < 1)
        {
            record[cnt] = -1;
            continue;
        }

        if (date > daysOfMonth[month - 1] || date < 1)
        {
            record[cnt] = -2;
            continue;
        }

        // calculate the number of days form year start
        for (int monCnt = 0; monCnt < month - 1; monCnt++)
        {
            daysOfInput += daysOfMonth[monCnt];
        }

        daysOfInput += (date - 1 + day1st);

        // calculate and print the the week day
        record[cnt] = daysOfInput % 7;
    }

    // print results
    for (int cnt = 0; cnt < inputNum; cnt++)
    {
        printf("%d ", record[cnt]);
    }
    printf("\n");

    return 0;

}


/* 

1. Input
    1492 0
    7
    10 12
    -1 0
    12 -12
    8 3
    6 31
    4 9
    11 3

    Output: 5 -1 -2 5 -2 1 6

2. Inputs:
    1911 0
    8
    4 27
    2 29
    12 25
    7 -5
    11 6
    2 0
    10 10
    3 100

    Output: 4 -2 1 -2 1 -2 2 -2

3. Inputs: 
    2552 6
    6
    15 20
    8 30
    2 29
    11 31
    0 13
    9 19

    Output: -1 3 2 -2 -1 2

4. Input: 
    2005 6
    7
    -77 -132
    12 25
    8 31
    7 6
    1 1
    1024 122
    2 29

    Output: -1 0 3 3 6 -1 -2

5. Input:
    2000 6
    10
    2 29
    1300 1
    11 19
    6 1272
    8 31
    4 9
    9 23
    2 28
    1 1
    10 1

    Output: 2 -1 0 -2 4 0 6 1 6 0
*/