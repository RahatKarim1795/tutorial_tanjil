// For each question make a seperate function e.g.:
// q1ans 
// void evenOrOdd(){}

// then call the functions appropriately in main()

// Q1
// Even or Odd:
// Write a C program that takes an integer as input and checks if it is even or odd using an if-else statement.


// Q2
// Factorial Calculation:
// Write a C program to calculate the factorial of a number entered by the user.
void fact(){
    int num;
    int result = 1;
    printf("num: ");
    scanf("%d", &num);
    for(int i = num; i>1; i--){
        result = result * i;
    }
    printf("Fact: %d", result);
}

// 1st loop:
// i = 4
// res = 1 * 4 = 4

// 2nd loop:
// i = 3
// res = 4 * 3 = 12

// 3rd loop:
// i = 2
// res = 12 * 2 = 24


// Q3
// Find the Largest Number:
// Write a C program that takes three integers as input and finds the largest among them using if-else statements.

// Q4
// Reverse a Number:
// Write a C program to reverse the digits of an integer. For example, if the input is 1234, the output should be 4321.

// Q5
// Check for Prime Number:
// Write a C program to check if a given number is prime. A prime number is only divisible by 1 and itself.

// Q6
// Sum of Digits:
// Write a C program that takes an integer as input and calculates the sum of its digits. For example, the sum of the digits of 1234 is 1 + 2 + 3 + 4 = 10.

// Q7
// Fibonacci Series:
// Write a C program to generate the first n numbers of the Fibonacci series, where n is provided by the user. The Fibonacci series is defined as follows: 0, 1, 1, 2, 3, 5, 8,....

//Q8
// Tree structure:
// Write a c program that will give the following 2 formatted outputs:

// a)

// *
// * *
// * * *
// * * * *

// b)

//     *
//    * *
//   * * *
//  * * * *  



int main(){
    //only call the functions here nothing else
    fact();
}