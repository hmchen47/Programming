Final Quiz
==========

1.
以下何者為有效變數名稱?
A. 1926sum
B. _counter
C. 234@@
D. a&bdef

Ans: B 

2. 
如果我們在主程式內宣告一個整數變數 a 但是沒有給初值，那麼當我們第一次使用 a 的值為何?
A. 0
B. NULL
C. 任意值
D. 1

Ans: C

3. 
如果 if 的條件是 (-1)，則會執行何者?
A. then
B. 視作業系統而定
C. else
D. 視編譯器而定

Ans: A

4. 
一個陣列的宣告為 int array[10]; 則合法的註標範圍為何?
A. array[1] 到 array[9]
B. array[0] 到 array[10]
C. array[0] 到 array[9]
D. array[1] 到 array[10]

Ans: C

5. 
如果一個程式含有多個函式，則由哪個函式開始執行?
A. major 函式
B. start 函式
C. main 函式
D. begin 函式

Ans: C

6. 
以下程式片段的輸出為何?

```cpp
counter = 0;
for (i = 0; i < 10; i++)
    for (j = 0; j < 10; j++) {
       if (i == j)
          break;
       counter++;
    }
printf(“%d\n”, counter);
```
A. 90
B. 100
C. 45
D. 55

Ans: C

7. 
以下程式片段的輸出為何?

```cpp
counter = 0;
for (i = 0; i < 10; i++)
    for (j = 0; j < 10; j++) {
       if (i == j)
          continue;
       counter++;
    }
printf(“%d\n”, counter);
```
A. 55
B. 45
C. 90
D. 100

Ans: C

8. 
如果 a 的宣告是 int *a，則 a[i] 的意義等同於?
A. (&a) + i
B. (*a) + i
C. &(a + i)
D. *(a + i)

Ans: D

9. 
如果 a 的宣告是 int a[2][3]，則 &(a[i]) 的值等同於?
A. &(a[i][0])
B. &(a) + i * 3 * sizeof(int)
C. &(a + i) * 3
D. a + i * 2

Ans: A

10. 
下列何種迴圈保證至少執行一次?
A. 以上皆是
B. do while
C. for
D. while

Ans: B

11. 
如果 c 的型別為 int 且值為 10，則 c / 3 + c % 6 結果為何?
A. 7.333333
B. 6
C. 6.333333
D. 7

Ans: D

12. 
如果 a 的型別為 int 且值為 12，b 的型別為 int 且值為 5，d 的型別為 double 且值為 24.0，則 d / (a / b) 的型別及值為何?
A. int, 10
B. double, 10.0000
C. int, 12
D. double, 12.0000

Ans: D

13. 
"變數 a 的值為 5 或是 6" 應如何表示?
A. a == 5 && a == 6
B. a == 5 || == 6
C. a == 5 || a == 6
D. a = 5 || a = 6

Ans: C

14. 
在一個函式內使用 return 會
A. 跳出該函式
B. 跳到該函式的起點
C. 跳到該函式的下一個 return
D. 跳出目前所在的迴圈

Ans: A

15. 
字串可視為何者的陣列?
A. 整數
B. 字元
C. 浮點數
D. 倍準浮點數

Ans: B

16. 
一般字串函數如 strcmp 如何知道字串的結尾?
A. 字串永遠是固定長度的陣列，所以沒有結尾的問題。
B. 偵測該字串元素是否為有效記憶體位址。
C. 偵測字串元素為 '\0'。
D. 偵測該字串元素是否含值。

Ans: C

17. 
如何將一個英文字串 word 的字尾 ‘y’ 除去，再加上 "ies”? 例如將 “university” 改成 "universities”?

A.
word[strlen(word) - 1] = ‘\0’;
strcat(word, “ies”);
B.
word[strlen(word)] = ‘\0’;
strcpy(word, “ies”);
C.
word[strlen(word)] = ‘\0’;
strcat(word, “ies”);
D.
word[strlen(word) - 1] = ‘\0’;
strcpy(word, “ies”);

Ans: A

18. 
現有 char string[100]。如果所有字串操作均為合法記憶體位址，則下列何者恆為真?
A. strlen(string) 等於 sizeof(string)
B. strlen(string) 小於 sizeof(string)
C. strlen(string) 大於 sizeof(string)
D. 以上皆非

Ans: B

19. 
如果 void 出現在函式名稱前，則下列何者為真?
A. 編譯器不會對該函式進行優化
B. 編譯器不會檢查函式參數型別
C. 函式沒有回傳值
D. 函式不須參數

Ans: C

20. 
假設 a 為一任意型別變數，則下列何者恆為真?
A. *(*a) == a
B. &(&a) == a
C. *(&a) == a
D. &(*a) == a

Ans: C

