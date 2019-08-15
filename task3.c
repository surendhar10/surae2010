  #include <stdio.h>
    int main()
    {
        char c;
        int lcase, ucase;
        printf("Enter an alphabet: ");
        scanf("%c",&c);
        
        lcase= (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
       
        ucase = (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
        
        if(c>='a' && c<='z')
        {
        
        if (lcase || ucase)
            printf("%c is a vowel.", c);
        else
            printf("%c is a consonant.", c);
        }
        else
        {
            printf("the given input is invalid");
        }
        return 0;
    }
