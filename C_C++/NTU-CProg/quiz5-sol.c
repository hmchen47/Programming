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
  deck[index] = NULL;
  shuffle(deck);
  print(deck);  
  return 0;
}


void shuffle ( int *deck[] )
{
    int i = 0;
    int buf[10000];
    while ( deck[i] ) {
        buf[i] = *deck[i];
        i++;
    }

    int sec_s = i / 2 + i % 2;
    int fir = 0, sec = sec_s, deck_p = 0;

    while ( deck[deck_p] ) {
        *deck[deck_p++] = buf[fir++];
        if ( buf[sec] )
            *deck[deck_p++] = buf[sec++];
    }
}

void print ( int *deck[] )
{
    int i = 0;
    while ( deck[i] ) {
        if ( i ) printf ( " " );
        printf ( "%d", *deck[i++] );
    }
}