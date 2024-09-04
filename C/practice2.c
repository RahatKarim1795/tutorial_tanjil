// make a function called isPrime()
// in main function ask the user to enter a number
// use the function to find out if the number is prime
// if it is prime keep taking input
// if the input is not a prime number break out of loop

// hint: isPrime will only return (1 or 0) OR (TRUE or FALSE)
// hint: use while loop
// hint: a number is a prime if it can be divided by only 1 and itself

#include <stdio.h>
#include <stdbool.h>

// 2,3,5,7,11
bool isPrime(int n){
    if(n==1){
        return false;
    }
    else if (n==2) {
        return true;
    }
    else if (n%2 == 0)
        return false;
    
    else {
        for(int i=3; i<n/2; i=i+2){
            if (n%i == 0){
                return false;
            }
        }
    }
    
    return true;
}

bool isPrime2(int n){
    // bool running = true;
    int i = 2;
    if (n==1)
        return false;
    else if (n==2)
        return true;
    else{
        while (i < n){
            if(n % i == 0){
                return false;
            }
            i++;
        }
    }
    return true;
}

void main(){
    int num;
    bool running = true;

    while(running == true){
        printf("Enter a number to find if it's a prime: ");
        scanf("%d", &num);

        if (isPrime2(num) == false){
            running = false;
            break;
        }
    }

}


// 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
// 20/2: if result = whole number/int, the number is not a prime = 10
// 20/3: if result = whole number/int, the number is not a prime = x
// 20/4: if result = whole number/int, the number is not a prime = 5
// 20/5: if result = whole number/int, the number is not a prime = 4
// 20/6: if result = whole number/int, the number is not a prime = x
// 20/7: if result = whole number/int, the number is not a prime = x
// 20/8: if result = whole number/int, the number is not a prime = x
// 20/9: if result = whole number/int, the number is not a prime = x
// 20/10: if result = whole number/int, the number is not a prime = 2
// 20/11: if result = whole number/int, the number is not a prime = x
// 20/12: if result = whole number/int, the number is not a prime 


// factors: 10,5,4,2