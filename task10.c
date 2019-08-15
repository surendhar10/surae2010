#include <stdio.h>

int main()
{
	int a,tNum,c=0;

	printf("Enter a number: ");
	scanf("%d",&a);
	tNum=a;

	while(tNum>0)
	{
		c++;
		tNum/=10;
	}

	printf("Total numbers of digits are: %d ",c);
	
	return 0;
}
