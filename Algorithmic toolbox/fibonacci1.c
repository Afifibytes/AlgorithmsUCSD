#include <stdio.h>
#include <stdlib.h>

/*
    better algorithm to print the n'th fibonacci number 
    more efficient, less running time.
*/

unsigned long fibonacci(int);

int main (int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./fibonacci1 n\n");
        return 1;
    }
    
    int n = atoi(argv[1]);
    
    if(n == 0)
    {
        printf("0\n");
    }
    else if (n == 1)
    {
        printf("1\n");
    }
    else
    {
        printf("%lu\n", fibonacci(n));
    }
}

unsigned long fibonacci(int n)
{
    unsigned long fibonacciArray[n];
        
    fibonacciArray[0] = 0;
    fibonacciArray[1] = 1;
    
    for(int i = 2; i < n; i++)
    {
        fibonacciArray[i] =  fibonacciArray[i-1] +  fibonacciArray[i-2];
    }
        
    return fibonacciArray[n-1] + fibonacciArray[n-2];
}