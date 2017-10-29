/* 
    將輸入做縮寫處理。比如說 "national"、"taiwan"、"university" 
    這三個字串的話，縮寫就是 "NTU"。注意，有四種字串必須直接省略，不納入縮寫中：
    "of"、 "and"、"the" 以及 "at"。例如"the"、"united"、"states"、"of"、
    "amarica" 將會被縮寫成 "USA"。

    輸入格式
    輸入會是一連串的小寫詞彙以及句號 (period '.')。要縮寫在一起的詞彙中，最後一個詞的
    結尾將會有一個句號。以前面舉的"NTU"為例，程式收到的輸入會是"national"、"taiwan" 
    以及 "university."。注意有一個句號在字串"university." 的結尾。你的程式將會一直 
    讀入輸入直到 EOF。我們保證輸入的最後一個詞彙的結尾一定會有句號； "of"、"and"、
    "the" 以及 "at" 不會是各個縮寫的最後一個詞彙，意即不會有"of."這樣的字串出現。我們
    也保證每個縮寫至少都會有一個字元。

    輸出格式
    你的程式必須在一行 (single line)內輸出所有的縮寫。(縮寫間留一個空白)

    輸入限制
    一個字彙(包含句號)的長度不會超過 127 個字元。一個縮寫的長度將不會超過 127 個字元。

    Pseudo Code:
        1. read inputs string-by-string into a given arrary origin[][127]
        2. create an array to store the abbrevations, abbrecv[][127]
        3. scan through the elements of the origin array to get the first
            characters, convert to upper case, and write to the abbrev array
        4. each abbrevation word ends with period (.) appearing in the 
            elements origin array
*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define WORDCOUNT    256
#define WORDLENLIMIT 128

int main(void)
{
    char origin[WORDCOUNT][WORDLENLIMIT];
    
    // read in the input and store in origin array
    char word[WORDLENLIMIT];
    int  wordCnt = 0;
    while (scanf("%s", word) != EOF)
    {
        // ignore 'at', 'of', 'the', and 'and'
        if (strcmp(word, "at") != 0 && strcmp(word, "of") != 0 && 
            strcmp(word, "the") != 0 && strcmp(word, "and") != 0)
        {
            strncpy(origin[wordCnt], word, strlen(word));
            wordCnt++;
        }
    }

    if (wordCnt >= WORDCOUNT)
    {
        printf("Input words exceeds the word limitation (256).\n");
        return 1;
    }

    // // print out the origin array
    // for (int i = 0; i < wordCnt; i++)
    //     printf("%s\n", origin[i]);

    // scan through the elements of the origin array and process
    int charIdx = 0;        // index of the array for the abbreviation
    char abbrev[WORDLENLIMIT];
    for (int idx = 0; idx < wordCnt; idx++)
    {
        char init = origin[idx][0];
        if (origin[idx][strlen(origin[idx]) - 1] == '.')
        {
            abbrev[charIdx] = toupper(init);
            abbrev[charIdx + 1] = '\0';
            charIdx = 0;
            printf("%s ", abbrev);
        }
        else
        {
            abbrev[charIdx] = toupper(init);
            charIdx++;
        }
    }

    printf("\n");

    return 0;
}


/* 輸入範例

the united states of american. taiwan high speed rail. national aeronautics and space administration. metropolitan rapid transit. north atlantic treaty organization. european union. university of hong kong. national chiao tong university. massachusetts institute of technology. united kingdom. national taiwan university. university of california at san diego. immigration and naturalization service.

輸出範例
USA THSR NASA MRT NATO EU UHK NCTU MIT UK NTU UCSD INS
*/