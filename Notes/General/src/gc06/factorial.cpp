/* factorial.cpp */
#include <iostream>

int factorial(int n) {
  int i, fac = 1;
  if (n != 1) {
    for (i=1; i<=n; i++)
      fac *=  i;
    return fac;
  }
  else
    return 1;
}

