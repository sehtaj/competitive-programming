// Write a function that moves all zeros in an integer 
// array to the end, while maintaining the relative order of the non-zero elements.
#include<stdio.h>
#include<string.h>
void movingzero(int *arr , int n){
//printf("%d", n);
		  int new[n];
      memset(new, 0, sizeof(new));  // Initialize all elements of new[] to 0

    int index = 0; // index for new 
    for(int i = 0; i < n ; i++){
        if(arr[i] != 0){
            new[index] = arr[i]; 
            index++;
        }
    }
    for(int i = 0 ; i < n ; i++){
        arr[i] = new[i];
    }
}
int main(){
    int arr[] = {1,0,2,3,0,4};
    int n = 6;
    movingzero(arr, n);
    //printf("%d",arr[3]);
    //printf("%d",arr[5]);
    return 0;
}