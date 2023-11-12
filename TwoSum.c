#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *aux=(int*)malloc(2*sizeof(int));
    if(aux==NULL){//if memory allocation fails
        *returnSize=0;
        return NULL;
    }
    for(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                aux[0]=i;
                aux[1]=j;
                *returnSize=2;
                return aux;
            }
        }
    }
    *returnSize=0;
    free(aux);
    return NULL;
}
