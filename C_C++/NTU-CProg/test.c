#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // int arr[2][2][3] = {{{1, 2}, {3, 4}}, {{11, 12}, {13, 14}}};

    int arr[2][2][3] = {{{0}}};

    // addresses
    printf("Addresses:\n");
    printf("arr           = %p\n", arr);
    printf("arr + 1       = %p\n", arr + 1);
    printf("arr[0]        = %p\n", arr[0]);
    printf("arr[0] + 1    = %p\n", arr[0] + 1);
    printf("arr[0][0]     = %p\n", arr[0][0]);
    printf("arr[0][0] + 1 = %p\n", arr[0][0] + 1);

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 3; k++)
                printf("%3d ", arr[i][j][k]);

    // values
    /*
    printf("Values:\n");
    int *ptr = (int *) arr;
    for (int idx = 0; idx < 8; idx++)
    {
        int value = *ptr++;
        printf("idx = %d, addr = %p, value = %d\n", idx, ptr, value);
    }
    */
    printf("\n");
    //printf("arr           = %d\n", *(arr[0]));
}

