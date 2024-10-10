//  Suppose an array sorted in ascending order is rotated 
//  at some pivot unknown to you beforehand.Find the minimum element. 
//  You must solve it in O(log n) time.

#include<stdio.h>
int findMin(int* arr, int n) {
    int left = 0;
    int right = n - 1;

    for (; left < right;) {
        int mid = left + (right - left) / 2;
        if (arr[mid] > arr[right]) {
            left = mid + 1;
        } else {
            right = mid; 
        }
    }
    return arr[left];
}
int main() {
     int arr[] = {3, 4, 5, 1, 2};
    // int arr[] = {1,2,3,4,5};
    // int arr[] = {5,4,3,2,1};
    //int arr[] = {2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int minElement = findMin(arr, n);
    printf("%d\n", minElement);

    return 0;
}