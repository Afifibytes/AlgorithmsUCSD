#include <stdio.h>
#include <stdlib.h>

//prototype
unsigned long fibonacci(int);

int main (int argc, char **argv)
{
    //check the input arguments
    if (argc != 2)
    {
        printf("Usage: ./fibonacci n\n");
    }
    else
    {
        int n = atoi(argv[1]);
        printf("%lu\n", fibonacci(n));
    }
}


//recursive function calculates the n'th fibonacci number
unsigned long fibonacci(int n)
{
    if(n == 0 || n == 1)
    {
        return n;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
