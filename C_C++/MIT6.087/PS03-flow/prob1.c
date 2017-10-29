/*
 * Code profiling and registers. In this problem, we will use some basic 
 * code profiling to examine the effects of explicitly declaring variables 
 * as registers. Consider the fibonacci sequence generating function 
 * fibonacci in prob1.c, which is reproduced at the end of this problem set 
 * (and can be downloaded from Stellar). The main() function handles the 
 * code profiling, calling fibonacci() many times and measuring the average 
 * processor time.
 * 
 * (a) First, to get a baseline (without any explicitly declared registers), 
 * compile and run prob1.c. Code profiling is one of the rare cases where 
 * using a debugger like gdb is discouraged, because the debugger’s overhead 
 * can impact the execution time. Also, we want to turn off compiler 
 * optimization. Please use the following commands to compile and run the 
 * program:
 * 	dweller@dwellerpc:~$ gcc -O0 -Wall prob1.c -o prob1.o
 * 	dweller@dwellerpc:~$ ./prob1.o
 * 	Avg. execution time: 0.000109 msec ← example output
 * 	dweller@dwellerpc:~$
 * How long does a single iteration take to execute (on average)?
 * 
 * (b) Now, modify the fibonacci() function by making the variables a, b, 
 * and c register variables. Recompile and run the code. How long does a 
 * single iteration take now, on average? Turn in a printout of your 
 * modified code (the fibonacci() function itself would suffice).
 * 
 * (c) Modify the fibonacci() function one more time by making the variable 
 * n also a register variable. Recompile and run the code once more. How 
 * long does a single iteration take with all four variables as register 
 * variables?
 * 
 * (d) Comment on your observed results. What can you conclude about using 
 * registers in your code?
 *
 * Compile: gcc -Wall -O0 prob1.c -o prob1
 * Usage: 	./prob1
 *
 */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define NMAX 25
static unsigned int results_buffer[NMAX];

void fibonacci()
{
	/* here are the variables to set as registers */
	// unsigned long long a = 0;
	// unsigned long long b = 1;
	// unsigned long long c;

	register unsigned long long a = 0;
	register unsigned long long b = 1;
	register unsigned long long c;

	// int n; 

	register int n;

	/* do not edit below this line */
	results_buffer[0] = a;
	results_buffer[1] = b;
	for (n = 2; n < NMAX; n++) {
		c = a + b;
		results_buffer[n] = c; /* store code in results buffer */
		a = b;
		b = c;
	}
}

/*
 * jharvard:PS03-flow$ ./prob1
 * Avg. execution time: 0.000188326 msec
 * 
 * jharvard:PS03-flow$ ./prob1
 * Avg. execution time: 0.000110291 msec
 *
 * jharvard:PS03-flow$ ./prob1
 * Avg. execution time: 8.12927e-05 msec

 * 
 */

int main(void) {
	
	long long n, ntests = 10000000;
	clock_t tstart, tend;
	double favg;

	/* do profiling */
	tstart = clock();
	
	for (n = 0; n < ntests; n++)
		fibonacci();

	tend = clock();
	/* end profiling */

	/* compute average execution time */
	favg = ((double)(tend - tstart))/CLOCKS_PER_SEC/ntests;

	/* print avg execution time in milliseconds */
	printf("Avg. execution time: %g msec\n",favg*1000);
	return 0;
}

