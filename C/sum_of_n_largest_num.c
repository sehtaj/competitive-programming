//Write a program to calculate the sum of
// n largest elements in an array of integers

#include<stdio.h>
#include<stdlib.h>
int compare(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);  // Sort in descending order
}
int largest_sum(const int arr[], int size, int n) {
    if (n <= 0) {
        return 0;
    }
    if (n > size) {           // Edge Cases
        n = size; 
    }
int *arr_copy = malloc(size * sizeof(int));
    if (arr_copy == NULL) {
        printf("Failed to allocate memory");
    }
    for (int i = 0; i < size; i++) {
        arr_copy[i] = arr[i];
    }

    // Sort the copied array in descending order
    qsort(arr_copy, size, sizeof(int), compare);
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr_copy[i];
    }
    free(arr_copy);
    return sum;
}

int main() {
    const int arr[] = {10,3,6,5,1,8};
    int n = 5;
    int size = sizeof(arr) / sizeof(arr[0]);

    int result = largest_sum(arr, size, n);
    printf("%d\n",result);

    return 0;
}