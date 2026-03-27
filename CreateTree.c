#include<stdio.h>
#include<stdlib.h>
#include<time.h>
typedef struct node{
    int data;
    struct node* left;
    struct node* right;
}N;

void createArray(int array[], int size);
void dispalyArray(int array[], int size);
N* createBinarayTree(int array[], int size, int index);
void exportTree(N** root);
void writeInDotFile(FILE* pf, N** root);

int main(){
    srand(time(NULL));
    printf("Enter Array Size: ");
    int size;
    scanf("%d",&size);
    int array[size];
    createArray(array, size);
    // dispalyArray(array, size);

    N* root=createBinarayTree(array, size, 0);
    printf("Done\n");
    exportTree(&root);
    

    return 0;
}

void createArray(int array[], int size){
    for(int i=0; i<size; i++){
        array[i]=rand()%500;
    }
}

void dispalyArray(int array[], int size){
    for(int i=0; i<size; i++){
        printf("%d,", array[i]);
    }
    printf("\n");
}

N* createBinarayTree(int array[], int size, int index){
    if(index>=size) return NULL;
    N* node=(N*)malloc(sizeof(N));
    node->data=array[index];
    node->left=createBinarayTree(array, size, index*2+1);
    node->right=createBinarayTree(array, size, index*2+2);
    return node;
}

void exportTree(N** root){
    FILE* pf=fopen("tree.dot", "w");
    fprintf(pf, "digraph BinaryTree {\n");
    writeInDotFile(pf, root);
    fprintf(pf, "}\n");
}

void writeInDotFile(FILE* pf, N** root){
    if(*root==NULL)return;
    else{
        if((*root)->left){
            fprintf(pf, "%lu -> %lu;\n", root, &((*root)->left));
            writeInDotFile(pf, &(*root)->left);
        }
        if((*root)->right){
            fprintf(pf, "%lu -> %lu;\n", root, &((*root)->right));
            writeInDotFile(pf, &(*root)->right);
        }
    }
}

