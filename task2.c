#include <stdio.h>

int main() 
{
    int a;
    printf("enter a number: ");
    scanf("%d",&a);
    if(a%2==0)
        {
            printf("the given number is even ");
        }
    else
        {
            printf("The given number is odd");
        }
    return 0;
    
}
