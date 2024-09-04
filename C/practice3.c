// Make a 2d array of size 3x3
// Fill the array with numbers taken as input from the user using a function called fillArray()
// Print the array using a function called printArray() in the following format:
// | 1 || 2 || 3 |
// | 4 || 5 || 6 |
// | 7 || 8 || 9 |
// Find the sum of all numbers in the array using a seperate function called sumArray()

// Make a pointer that points to the array
// Print the address and the value of the variable the pointer points to
// Which element of the array has this address?

void fillArray(int arr[3][3]){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("Number: ");
            scanf("%d", &arr[i][j]);
        }
    }
}

void printArray(int arr[3][3]){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("| %d |", arr[i][j]);
        }
        printf("\n");
    }
}

int sumArray(int arr[3][3]){
    int sum = 0;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            sum += arr[i][j];
        }
    }
    return sum;
}

void main(){
    int arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};

    // fillArray(arr);

    printArray(arr);

    int sum = sumArray(arr);
    printf("\nSum of array: %d", sum);

    // int (*ptr)[3] = arr;
    int *ptr = arr;
    printf("\nAddress: %p", ptr);
    printf("\nValue: %d", *ptr);

}