//Write a program that calculates the mean and variance
//of an array of integers
#include <assert.h>
#include <stdio.h>

const double EPSILON = 0.01;

//Function to calculate Sum:
static int sum(const int a[], int len){
    int add = 0;
    for (int i = 0 ; i < len ; i++){
       add = add + a[i];
    }
    return add;   
}

//Function to Calculate Mean:

double mean(const int b[], int len){
    double ResultMean = (double)sum(b,len)/len;
    return ResultMean;
}
//Function to Calculate Variance:
double var(const int b[], int len){
    double variance = mean(b , len);
    double ResultVariance =  0;
    for (int i = 0 ; i < len ; i++){
        ResultVariance = ResultVariance + (b[i] - variance)*(b[i] - variance)/len;
    }
    return ResultVariance;
}
int main(void) {
    const int a[2] = {3, 2};
    const int b[3] = {1, 2, 3};
    
    printf("Mean: %.2f\n", mean(b, 2));  // Should print "Mean: 2.00"
    printf("Variance: %.2f\n", var(b, 2));  // Should print "Variance: 0.67" (approximately)
  return 0;
}
