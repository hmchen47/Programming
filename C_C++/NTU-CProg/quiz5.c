/* 
    用一個指標陣列 (array of pointer) 來代表牌組。排組內的每張牌都有一個 1 至 10000 
    的整數點數。陣列的第 i 個元素代表牌組中的第 i 張牌；也就是說，如果牌組的第 i 張牌的點數為 
    6，那麼陣列第 i 個指標所指到的值就會是 6。如果指標指到 `NULL` 代表那是牌組的末端 (end of 
    deck)，代表後面將不會有任何牌。我們保證牌組中最多只有 9999 張牌。

    Author: Fred Chen
*/
#include <stdio.h>

void shuffle(int *deck[]);
void print(int *deck[]);

int main()
{
    int card[10000];
    int *deck[10000];
    int index = 0;

    
    while (scanf("%d", &(card[index])) != EOF) {
      deck[index] = &(card[index]);
      index++;
    }
    
    // index = 5;
    // for (int idx = 0; idx < index; idx++)
    // {
    //     deck[idx] = &(card[idx]);
    // }

    deck[index] = NULL;
    shuffle(deck);
    print(deck); 

    return 0;
}

/* 
    首先先將 `n` 張牌分成兩組，第一組中包含了前半 `(n/2)` 的牌；第二組則包含剩下的牌。 例如有 9 
    張牌的話，分堆後第一組牌有 5 張牌，而第二組牌則有 4 張牌。接著我們將兩組牌合為一組，順序為：第一
    組的第一張牌、第二組的第一張牌、第一組的第二張牌、第二組的第二張牌，以此類推。也就是說，我們交替著擺
    ，將把兩組牌合為一組。

    Arguments:
        deck: integer pointer, an array of pointers that point to the card values

    Return: NULL
*/
void shuffle(int *deck[])
{
    // get the total uumber of the card in the deck
    int total = 0;
    int **deckPtr = deck;

    while (*deckPtr++ != NULL)
        total++;

    // declare a new deck to store shuffled cards
    int *newDeck[1000];

    // shuffle the cards
    for (int idx = 0, half = (total + 1) /2; idx < half; idx++)
    {
        if ((idx == (half - 1)) && (total % 2 == 1))
        {
            // printf("idx = %d\n", idx);
            newDeck[idx * 2] = deck[idx];
            newDeck[idx * 2 + 1] = NULL;
        }
        else
        {
            newDeck[idx * 2] = deck[idx];
            newDeck[idx * 2 + 1] = deck[half + idx];
        }
    }

    // copy the shuffled cards into the old card deck
    for (int idx = 0; idx < total; idx++)
    {
      deck[idx] = newDeck[idx];
    }

    return;
}


/*
    在一行 (single line) 內按照順序印出所有牌的點數，數字間留一個空白。提醒，根據牌組末端 (end 
    of deck) 就能知道所有的牌都已經印出了。 

*/
void print(int *deck[])
{
    // print the whole deck
    int **deckPtr = deck;

    do 
    {
        if (*deckPtr != NULL)
          printf ("%d ", **deckPtr);
    } while (*deckPtr++ != NULL);

    printf ("\n");

    return;
}


/* 
輸入範例
1 2 3 4 5

輸出範例
1 4 2 5 3


1. 
輸入
8 10 3 4 1 6 2 9 7 5

輸出
8 6 10 2 3 9 4 7 1 5

5. 
輸入
39 13 92 69 58 96 143 153 54 199 89 159 68 141 40 198 187 10 123 173 126 6 14 205 32 183 52 37 157 106 138 94 193 16 119 148 114 11 33 53 87 192 206 43 84 164 51 80 116 107 115 49 110 151 129 186 59 70 88 149 191 145 120 184 81 169 75 180 55 4 20 91 102 163 112 127 104 150 136 158 19 146 61 17 128 155 168 202 98 147 34 86 27 5 113 97 171 30 47 144 73 78 28 167 62 177 31 124 132 72 50 82 176 134 21 165 170 166 100 154 140 182 9 196 65 63 41 45 175 23 67 195 188 130 108 194 161 95 201 179 122 203 77 76 174 3 66 117 44 178 24 181 105 18 1 204 190 26 60 74 83 118 172 8 29 156 139 135 64 200 38 35 2 101 121 42 160 137 197 25 207 99 103 131 162 125 109 7 133 90 71 93 57 46 79 48 36 142 189 111 185 85 22 152 12 15 56

輸出
39 62 13 177 92 31 69 124 58 132 96 72 143 50 153 82 54 176 199 134 89 21 159 165 68 170 141 166 40 100 198 154 187 140 10 182 123 9 173 196 126 65 6 63 14 41 205 45 32 175 183 23 52 67 37 195 157 188 106 130 138 108 94 194 193 161 16 95 119 201 148 179 114 122 11 203 33 77 53 76 87 174 192 3 206 66 43 117 84 44 164 178 51 24 80 181 116 105 107 18 115 1 49 204 110 190 151 26 129 60 186 74 59 83 70 118 88 172 149 8 191 29 145 156 120 139 184 135 81 64 169 200 75 38 180 35 55 2 4 101 20 121 91 42 102 160 163 137 112 197 127 25 104 207 150 99 136 103 158 131 19 162 146 125 61 109 17 7 128 133 155 90 168 71 202 93 98 57 147 46 34 79 86 48 27 36 5 142 113 189 97 111 171 185 30 85 47 22 144 152 73 12 78 15 28 56 167
*/