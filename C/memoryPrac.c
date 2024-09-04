// Create a program that creates an array of item code (in integer)
// of items in a shop and another array that stores the 
// prices (in float) of the items
// The program will ask the user the no of items at the start
// and make the two arrays
// Use pointers and dynamic memory allocation to make the arrays
// The program will also ask if the no of items has changed
// If yes, input the new no of items and reallocate the memory for
// the new items and new prices

// Create two functions to take input into the two arrays

#include <stdio.h>
#include <stdlib.h>

void arr_input(int *arr1, float *arr2){

}

int main(){
    int num;
    printf("Number of items: ");
    scanf("%d", &num);

    int *code_arr = (int *) malloc(num * sizeof(int));
    float *price_arr = (float *) malloc(num * sizeof(float));

    if (code_arr == NULL && price_arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    free(code_arr);
    free(price_arr);
}