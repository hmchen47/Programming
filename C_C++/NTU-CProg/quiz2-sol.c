#include <stdio.h>

int main ()
{
   int y, d;
   int n;
   int month, day;
   int leap_year;
   int days;

   scanf ( "%d%d", &y, &d );
   scanf ( "%d", &n );

   // leap year or not
   leap_year = y % 400 == 0 || ( y % 100 && y % 4 == 0 );

   // calculate each input line
   for ( int i = 0; i < n; i++ ) {
      if ( i ) printf ( " " );

      days = d;
      scanf ( "%d%d", &month, &day );

      if ( month < 1 || month > 12 ) {
         printf ( "-1" );
         continue;
      }
      if ( day < 1 ) {
         printf ( "-2" );
         continue;
      }
      else {
         switch ( month ) {
            case 2:
               if ( ( leap_year && day > 29 ) ||
                    ( !leap_year && day > 28 ) ) {
                  printf ( "-2" );
                  continue;
               }
               break;
            case 4: case 6: case 9: case 11:
               if ( day > 30 ) {
                  printf ( "-2" );
                  continue;
               }
               break;
            default:
               if ( day > 31 ) {
                  printf ( "-2" );
                  continue;
               }
         }
      }

      for ( int m = 1; m < month; m++ ) {
         switch ( m ) {
            case 2:
               if ( leap_year ) days += 29;
               else days += 28;
               break;
            case 4: case 6: case 9: case 11:
               days += 30;
               break;
            default:
               days += 31;
         }
      }

      days += ( day - 1 );
      printf ( "%d", days % 7 );
   }

   return 0;
}