/*

You are tasked with writing a C function that computes the minimum, maximum, and sum of an array of integers. The results should be stored in a structure that holds these three values.

### Structure Definition:

Define a structure `struct statistics` that holds three fields:

- `min`: an integer representing the smallest element in the array.
- `max`: an integer representing the largest element in the array.
- `sum`: an integer representing the sum of all elements in the array.


*/

#include <stdio.h>

struct statistics {
    int min;
    int max;
    int sum;
};
void stats(const int *a, int len, struct statistics *s) {
    s->min = a[0];
    s->max = a[0];
    s->sum = 0;
    for (int i = 0; i < len; i++) {
        if (a[i] < s->min) {
            s->min = a[i];
        }
        if (a[i] > s->max) {
            s->max = a[i]; 
        }
        s->sum =  s->sum + a[i];
    }
}
int main(void) {
  int array1[] = {2, 2};
  struct statistics s1 = {};
  stats(array1, 2, &s1);
  printf("Min: %d, Max: %d, Sum: %d\n", s1.min, s1.max, s1.sum);  // Output: Min: 2, Max: 2, Sum: 4

  int array2[] = {2, 2, 1, 6, 4, 0};
  struct statistics s2 = {};
  stats(array2, 6, &s2);
  printf("Min: %d, Max: %d, Sum: %d\n", s2.min, s2.max, s2.sum);  // Output: Min: 0, Max: 6, Sum: 15

  return 0;
}
