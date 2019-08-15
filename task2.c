#include <stdio.h>

int main() 
{
    int a;
    printf("enter a number: ");
    scanf("%d",&a);
    if(a>0)
    {
    if(a%2==0)
        {
            printf("the given number is even ");
        }
    else
        {
            printf("The given number is odd");
        }
    }
    else
    {
        printf("the given input is invalid");
    }
    return 0;
    
}


