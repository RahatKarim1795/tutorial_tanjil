#include <stdio.h>
#include <stdlib.h>

int main() {
    // int students[20];
    // int *students;
    int num;
    // printf("How many students?\n");
    // scanf("%d", &num);
    

    int std[5];

    // Allocate memory for an students of 5 integers
    // int *students = (int *) malloc( num * sizeof(int) );

    // Check if memory allocation was successful
    // if (students == NULL) {
    //     printf("Memory allocation failed\n");
    //     return 1;
    // }

    // Initialize the students elements
    int std_num = 1;
    int mark;

    // for (int i = 0; i < num; i++) {
    //     printf("Mark for student %d: ", std_num);
        
    //     scanf("%d", &mark);

    //     students[i] = mark;

    //     std_num+=1;
    // }

    // Print the students elements
    // for (int i = 0; i < num; i++) {
    //     printf("student %d = %d\n", i+1, students[i]);
    // }

    // realloc(students,100);

    // for (int i = 0; i < num; i++) {
    //     printf("student mark = %d\n", students[i]);
    // }

    // Free the allocated memory
    // free(students);


    int *ptr1 = malloc(4);
    char *ptr2 = (char*) ptr1;
    // ptr1[0] = 1684234849;

    ptr2[0] = 'a';
    ptr2[1] = 'b';
    ptr2[2] = 'c';
    ptr2[3] = 'g';
    printf("%p is %c %c %c %c", ptr1, ptr2[0], ptr2[1], ptr2[2], ptr2[3]);

    printf("\naddress of ptr1: %p", &ptr1);
    printf("\naddress of ptr2: %p", &ptr2);
    printf("\naddress of ptr2[0]: %p", &ptr2[0]);
    printf("\naddress stored by ptr1: %p", ptr1);
    printf("\naddress stored by ptr2: %p", ptr2);

    free(ptr1);
    // free(ptr2);


    int **matrix;

    int row = 3;
    int col = 3;
    // int **matrix = (int**) malloc(row * sizeof(int*));
    // int *students_b = (int *) malloc(num * sizeof(int));

    // for (int i = 0; i < row; i++) {
    //     matrix[i] = (int*) malloc(col * sizeof(int));
    // }

    // matrix[0][0] = 439;


    // printf("%p", matrix);
    // printf("\n%p", *matrix);
    // printf("\n%d", **matrix);

    // printf("\n%p", &matrix[0][0]);
    // printf("\n%p", &matrix[0]);
    // printf("\n%p", &matrix);


    // free(matrix);

    return 0;
}
