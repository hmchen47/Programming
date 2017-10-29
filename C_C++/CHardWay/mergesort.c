#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>


typedef struct array {
    int     len;        // length of the array
    double  *array;     // pointer to double array
} array;

// a typedef creates a fake type, in this case for a function pointer
typedef double (*compare_cb)(double a, double b);

struct array *mergeSort(struct array*);
struct array *merge(struct array*, struct array*, compare_cb);
double sorted_order(double, double);
double reverse_order(double, double);


int main(void)
{
    struct array vector;
    struct array *result;

    vector.len = 6;
    double tmp[6] = {10, 45, 3, 9, 5, 4};
    vector.array = tmp;

    result = mergeSort(&vector);

    int idx;
    for (idx = 0; idx < result->len; idx++)
    {
        printf("%.2f ", result->array[idx]);
    }
    printf("\n");

    // free memory block
    free(result->array); free(result);

    return 0;
}

struct array *mergeSort(struct array* vector)
{
    // base case
    if (vector->len < 2) {
        struct array *new = (struct array*) malloc(sizeof(struct array));
        new->len = vector->len;
        new->array = (double*) malloc(sizeof(double));
        new->array[0] = vector->array[0];
        return new;
    }
    else{
        // generate left half array
        struct array *left = (struct array*) malloc(sizeof(struct array));
        left->len = vector->len / 2;
        left->array = (double *) malloc(left->len * sizeof(double));
        memcpy(left->array, vector->array, sizeof(double) * left->len);

        // generate right left array
        struct array *right = (struct array*) malloc(sizeof(struct array));
        right->len  = vector->len - left->len;
        right->array = (double *) malloc(right->len * sizeof(double));
        memcpy(right->array, vector->array + left->len, \
            sizeof(double) * right->len);

        // recursively separate the array
        struct array *newleft, *newright;
        newleft = mergeSort(left);
        newright = mergeSort(right);

        // free memory blocks
        free(left->array); free(left); 
        free(right->array); free(right);
        // free(vector->array); free(vector); 

        // merge the left and right array with sorting
        return merge(newleft, newright, reverse_order);
    }
}

struct array *merge(struct array* left, struct array* right, compare_cb cmp)
{
    // decending order

    // create new sorted merged array
    struct array *new = (struct array*) malloc(sizeof(struct array));
    new->len = left->len + right->len;
    new->array = (double*) malloc(sizeof(double) * new->len);

    // move the larger elements into new array 
    int i = 0, j = 0, k = 0;
    while((i < left->len) && (j < right->len))
    {
        if (cmp(left->array[i], right->array[j]) < 0)
        {
            new->array[k] = left->array[i];
            i++, k++;
        }
        else
        {
            new->array[k] = right->array[j];
            j++, k++;
        }
    }

    // move nn-empty left array into new array
    while(i < left->len)
    {
        new->array[k] = left->array[i];
        i++, k++;
    }

    // move non-empty right array into new array
    while(j < right->len)
    {
        new->array[k] = right->array[j];
        j++, k++;
    }

    // free memeory block
    free(left->array); free(left);
    free(right->array); free(right);

    return new;
}

double sorted_order(double a, double b)
{
    return a - b;
}

double reverse_order(double a, double b)
{
    return b - a;
}
