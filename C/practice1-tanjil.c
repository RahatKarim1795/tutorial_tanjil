// make a function called sum to add two numbers
// make a function called average to find the average of two numbers
// in main function ask the user to enter two numbers
// use the two functions to find out sum and average
// then show the output of these functions

#include <stdio.h>
int num1, num2;

int sum(num1, num2) {
    int num3 = num1 + num2;
    return num3;
}


float average(int num1, int num2) {
    float avg = (num1 + num2) / 2.0;
    return avg;
}



int main() {

    int num1, num2;

    printf("\nEnter a number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);

    int sum_answer = sum(num1, num2);

    float average_answer = average(num1, num2);


    printf("\nThe sum of the numbers is %d\n", sum_answer);
    printf("\nThe average of the numbers is %f\n", average_answer);


    return 0;

}