#include <stdio.h>
#include <stdbool.h>

const float PI = 3.14;

int sum(int a, int b){

    int c = a + b;

    return c;
}

void decimalPrecision() {

    float myFloatNum = 3.5;

    printf("%f\n", myFloatNum);   // Default will show 6 digits after the decimal point
    printf("%.1f\n", myFloatNum); // Only show 1 digit
    printf("%.2f\n", myFloatNum); // Only show 2 digits
    printf("%.4f", myFloatNum);   // Only show 4 digits

}

void main() {

    // printf ("Hello, World!\n");

    int in;
    int number;
    char sss;
    bool var = true;

    // printf("Enter a number: ");
    // scanf("%d", &in);
    
    // & signifies the address of the variable
    
    number = sum(in, 2);
    int nn = 2;


    printf ("yo %d! \nMy input %d\n", number, in);

    // printf ("my number %d", in);
    // function for sum
    float decimal = 1.223;

    char character = 'a';
    
    char stringVar[] = "Hello";
    // printf("%s", stringVar);

    // decimalPrecision();

    // if (number != nn){

    //     printf("%d", number);

    // }    

    // else if (number == nn) {

    //     printf("%d", number);

    // }

    // else {

    // }

    // switch (sum(number,nn)) {
    //     case 5:
    //         printf("%d", number);
    //         break;
    //     case 0:
    //         printf("sdhnd");
    //         break;
    // }

    // while loop

    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        //all code in loop
        i+=1;
    }



    int count = 0;

    while (count < 2) {
        printf("This will not print if count is 1 or more\n");
        count++;
    }
    count = 0;

    do {
        printf("This will print at least once\n");
        count++;
    } while (count < 2);

    // while loop
    i = 0;
    while (i < 5) {
        printf("%d\n", i);
        //all code in loop
        i++;
    }

    int times = 0;
    char clone = 'a';
    while (clone == 'a'){
        printf("make it double");
        times+=1;
        if (times > 5 ) clone = 'b';
    }


    // do while loop
    int j = 0;
    do {
        printf("%d\n", j);
        j++;
    } while (j < 5);

    // for loop
    int k; // declaration
    k = 1; // initialization

    for (int k = 0; k < 5; k++) {
        printf("%d\n", k);
        //all code
    }

    printf("\n\n\n");

    int myInput;
    myInput = 1;

    while (myInput != 0){
        scanf("%d", &myInput);
        printf("my input is: %d\n", myInput);
    }

    for (myInput = 1; myInput!=0; myInput++) {
        scanf("%d", &myInput);
        printf("my input is: %d\n", myInput);
        if (myInput == 0) {
            break;
        }
    }


}

// The general rules for naming variables are:

// Names can contain letters, digits and underscores
// Names must begin with a letter or an underscore (_)
// Names are case-sensitive (myVar and myvar are different variables)
// Names cannot contain whitespaces or special characters like !, #, %, etc.
// Reserved words (such as int) cannot be used as names


// Data types
// amount of space is defined for every data type
// int = 4 bytes
// float
// double (used for large numbers) = 8 bytes
// char
// bool
// void (used for functions that don't return a value)

// Basic Format Specifiers
// we will use these instead of writing variable names directly
// %d or %i	    integer
// %f 	        float
// %c 	        character
// %s 	        string
// %u           addresses
// %lu


// "e" to indicate the power of 10
// 35e3 == 35 to the power of 3



// Type conversion
// https://www.w3schools.com/c/c_type_conversion.php

// Constants
// const int NUMBER = 10; // cannot be changed
// NUMBER = 2222; // not possible
// const float PI = 3.14;
// norm: declare them with uppercase

// Arithmetic Operators

// + addition
// - subtraction
// %	Modulus
// ++	Increment by 1
// --	Decrement by 1
// +=, -=, *=, /=, %=

// a *= 2 means a = a * 2

// ==	Equal to
// !=	Not equal
// >	Greater than
// <	Less than
// >=	Greater than or equal to
// <=	Less than or equal to
// && 	Logical and
// ||	Logical or
// !	Logical not
