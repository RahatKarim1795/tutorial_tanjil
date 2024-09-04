// Make 2 1d arrays of size 10
// Fill array1 with these
// hardcoded numbers = {74,2,34,11,45,133,5,66,63,93}
// Fill array2 with sorted (increasing order 1,2,3) inputed numbers 
// using a seperate function called arrayInput()
// Now, check if the arrays are sorted in 
// increasing order using another function called isSorted()

#include <stdio.h>
#include <stdbool.h>

void arrayInput(int arr[]){
    
    int num;
    // int length = sizeof(arr) / sizeof(arr[0]);

    for(int i=0; i<10; i++){
        printf("Number: ");
        scanf("%d", &num);

        arr[i] = num;
    }
}

void isSorted(int arr[]){
    bool sorted = true;

    // int length = sizeof(arr) / sizeof(arr[0]);
    
    int check = arr[0];

    for(int i=1; i<10; i++){

        if(check>arr[i]){
            sorted = false;
            break;
        }
        else if(check<arr[i]){
            continue;
        }
        check = arr[i];
    }

    if(sorted == true){
        printf("Array is sorted!\n");
    }
    else{
        printf("SCUM OF THE EARTH! NOT SORTED!\n");
    }
}

void isSorted2(int arr[]){

    bool sorted = true;

    // int length = sizeof(arr) / sizeof(arr[0]);
//  arr = [5,10,10,20,25,30.,,,,,,30,12]   
    for(int i=0; i<9; i++){

        if(arr[i]>arr[i+1]){
            sorted = false;
            printf("SCUM OF THE EARTH! NOT SORTED!\n");
            break;
        }
        else if (arr[i]<=arr[i+1]){
            continue;
        }
    }

    if(sorted == true){
        printf("Array is sorted!\n");
    }

}


int main(){
    int arr1[10] = {74,2,34,11,45,133,5,66,63,93};
    int arr2[10];

    arrayInput(arr2);

    isSorted(arr1);
    isSorted(arr2);

    isSorted2(arr1);
    isSorted2(arr2);

    return 1;
}