// we will make 3 functions
// function 1 main
// function 2 sum
// function 3 take input from 
// user and show output

#include <stdio.h>

int sum(int num1,int num2) {

    int num3 = num1 + num2;

    return num3;
}

void func() {
    int in;
    printf("Enter a number: ");
    scanf("%d", &in);
    printf("\nYour number is %d \n", in);
}

int main() {
    int num1 = 4;
    int summation = sum(234,25);
    func();
    printf("%d",summation);

    return 0;
}