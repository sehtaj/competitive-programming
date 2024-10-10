#include<stdio.h>
/*
  findnum: Given an array of integers representing numbers from 0 to n (with one missing),
  the function returns the missing number in the sequence.
 
  findnum: (Int[], Int) -> Int
  effects: None
 */

int findnum(int *arr , int n) {
    int totalSum = n * (n + 1) / 2;
    int arrSum = 0;
    for(int i = 0; i < n; i++) {
        arrSum = arrSum + arr[i];
    }
    return totalSum - arrSum;
}

int main() {
    int arr[] = {0, 1, 2, 3, 5};  // The array contains numbers 0 to 5, but 4 is missing.
    int n = 5;  // The size of the array (5 elements)
    
    // The function call should return 4 as it is the missing number.
    printf("Missing number: %d\n", findnum(arr, n)); 

    // Edge Case 1: Missing the smallest number 0
    int arr2[] = {1, 2, 3, 4, 5};
    n = 5;
    printf("Missing number: %d\n", findnum(arr2, n));  // Expected output: 0

    // Edge Case 2: Missing the largest number n
    int arr3[] = {0, 1, 2, 3, 4};
    n = 5; 
    printf("Missing number: %d\n", findnum(arr3, n));  // Expected output: 5

    // Edge Case 3: Only one element
    int arr4[] = {0};
    n = 1; 
    printf("Missing number: %d\n", findnum(arr4, n));  // Expected output: 1

    // Edge Case 4: Empty array
    int arr5[] = {};
    n = 0;
    printf("Missing number: %d\n", findnum(arr5, n));  // Expected output: 0

    return 0;
}

