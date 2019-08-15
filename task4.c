 #include <stdio.h>
    void main()
    {
        char c;
         printf("Enter an alphabet: ");
         scanf("%c",&c);
         if(c>='a' && c<='z')
         {
             printf("It is a alphabet");
         }
         else
         {
             printf("It is not a alphabet");
         }
    }
