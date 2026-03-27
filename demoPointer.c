#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    int x;
}N;

void display(N** root){
    printf("In Fun root=%lu\n", root);
}
int main(){
    N* node=(N*)malloc(sizeof(N));
    node->x=5;
    N* root=node;
    

    printf("Main root=%lu\n", &root);
    display(&root);

}