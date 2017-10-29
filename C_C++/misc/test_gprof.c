//test_gprof.c
/*
 * Compliation: gcc -Wall -pg test_gprof.c test_gprof_new.c -o test_gprof
 * 
 * Execution: ./test_gprof
 * 
 * Profile data: gprof test_gprof gmon.out > analysis.txt
 *
 * suppress declared function:
 *  gprof -a test_gprof gmon.out > analysis.txt
 * suppress verbose
 *  gprof -b test_gprof gmon.out > analysis.txt
 * flat profile only:
 *  gprof -p -b test_gprof gmon.out > analysis.txt
 * info related to specific function:
 *  gprof -pfunc1 -b test_gprof gmon.out > analysis.txt
 * suppress flat profile:
 *  gprof -P -b test_gprof gmon.out > analysis.txt
 * only call graph info using '-q':
 *  gprof -q -b test_gprof gmon.out > analysis.txt
 *  gprof -qfuync1 -b test_gprof gmon.out > analysis.txt
 * suppress call graph using '-Q'
 *  gprof -Q -b test_gprof gmon.out > analysis.txt
 *  gprof -Qfunc1 -b test_gprof gmon.out > analysis.txt
 *
 */

#include<stdio.h>

void new_func1(void);

void func1(void)
{
    printf("\n Inside func1 \n");
    int i = 0;

    for(;i<0xffffffff;i++);
    new_func1();

    return;test_gprof.c
}

static void func2(void)
{
    printf("\n Inside func2 \n");
    int i = 0;

    for(;i<0xffffffaa;i++);
    return;
}

int main(void)
{
    printf("\n Inside main()\n");
    int i = 0;

    for(;i<0xffffff;i++);
    func1();
    func2();

    return 0;
}