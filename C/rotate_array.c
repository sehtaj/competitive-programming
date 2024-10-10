//Given an integer array nums and an integer k, rotate the array to 
//the right by k steps. Implement a solution that runs in O(n) time.

#include<stdio.h>
int rotate(int* arr, int n, int k) {
    k = k % n;
    
    for (int i = 0; i < k; i++) {
        int last = arr[n - 1]; 
        for (int j = n - 1; j > 0; j--) {
            arr[j] = arr[j - 1];
        }
        arr[0] = last; 
    }
}
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int k = 4;
    int n = sizeof(arr) / sizeof(arr[0]);
    rotate(arr, n, k);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}