#include <stdio.h>

void printvar(int var){
    printf("%d", var);

}

code_array = [001, , , , ]
price_array = [283.75, , , , ]


void user_input(int *code_array, int product_quantity, float *price_array) {
    
    int user_input1;

    float user_input2;

    for (int i=0; i<product_quantity; i++) {

        printf("Code of each product: ");
        scanf("%d", &user_input1);

        code_array[i] = user_input1;

        printf("Price of each product: ");
        scanf("%f", &user_input2);

        price_array[i] = user_input2;
    }
}

void main(){
    int var;
    char var2;
    printvar(var);
}