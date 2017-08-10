#include <stdio.h>
#include <stdlib.h>

unsigned long fibonacci(int);

int main (int argc, char **argv)
{
    if (argc > 2)
    {
        printf("ERORR!\n");
    }
    else
    {
        int number = atoi(argv[1]);
        unsigned long fibo = fibonacci(number);
        printf("%lu\n", fibo);
    }
}

unsigned long fibonacci(int number)
{
    if(number == 0 || number == 1)
    {
        return number;
    }
    else
    {
        return fibonacci(number - 1) + fibonacci(number - 2);
    }
}