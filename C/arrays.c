#include <stdio.h>
#include <string.h>

void stringgss(){
    char name[] = "Tanjil";
    printf("%s", name);

    char nbv = 'y';
}

int main() {

    int arr[5];

    // arr[0] = 3;
    // arr[1] = 5;
    // arr[2] = 7;
    // arr[3] = 9;
    // arr[4] = 11;

    // printf("%d ", arr[0]);
    int val = 3;
    
    for(int i=0; i<5; i++){
        arr[i] = val;
        val+=2;
    }

    // for(int i=0; i<5; i++){
    //     printf("%d ", arr[i]);
    // }

    // for(int i=4; i>=0; i--){
    //     printf("%d ", arr[i]);
    // }
    double number111;
    int myNumbers[] = {10, 25, 50, 75, 100};

    printf("%lu", sizeof(myNumbers));

    int length = sizeof(myNumbers) / sizeof(myNumbers[0]);

    printf("%d", length);  // Prints 5

    int matrix[3][3];
    int num;

    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("Number: ");
            scanf("%d", &num);

            matrix[i][j] = num;
        }
    }

    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("| %d |", matrix[i][j]);            
        }
        printf("\n");
    }
    // other way round
    for(int i=2; i>=0; i--){
        for(int j=2; j>=0; j--){
            printf("| %d |", matrix[i][j]);            
        }
        printf("\n");
    }

    printf("%d", matrix[1][1]);

    matrix[1][1] = 5;

    int matrix2[2][3] = { {1, 0, 2}, {3, 6, 8} };


    return 1;

}
