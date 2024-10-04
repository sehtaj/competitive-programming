#include<stdio.h>




/*Problem: Write a function that prints all pairs of elements in an array.
    Input: nums = [1, 2, 3]
    Output: (1, 2), (1, 3), (2, 3)
*/
void pairing(int *arr , int n){
    for (int i = 0 ; i < n ; i++){
        for (int j = i + 1; j < n ; j++){
            printf("pairs are %d,%d \n" , arr[i] , arr[j]);
        }
    }
}
int main(){
    int arr[] = {1,2,3,4};
    int n = 4;
    pairing(arr , n);
    return 0;
}