#include <stdio.h>



void main(){
    int myAge = 43;
    int* ptr = &myAge;  // A pointer variable, with the name ptr, that stores the address of myAge


    // Output the value of myAge (43)
    printf("%d\n", myAge);
    
    // Output the memory address of myAge (0x7ffe5367e044)
    printf("%p\n", &myAge);

    // Output the memory address of myAge with the pointer (0x7ffe5367e044)
    printf("%p\n", ptr);

    // Output the value of the variable ptr is pointing at (43)
    printf("%d\n", *ptr);


    int myNumbers[4] = {25, 50, 75, 100};
    int *ptr2 = myNumbers;

    // Get the memory address of the myNumbers array
    printf("%p\n", myNumbers);

    // Get the memory address of the first array element
    printf("%p\n", &myNumbers[0]);

    // Get the value of the first element in myNumbers
    printf("%d\n", *myNumbers);

    printf("%d\n", *(myNumbers+1));

}
