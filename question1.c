#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
int main()
{
    pid_t pid;
    pid = fork();
    if (pid < 0)
    {
        printf("Error!");
    }
    if (pid == 0)
    {
        pid = fork();
        if (pid < 0)
        {
            printf("Error!");
        }
        if (pid==0)
        {
            printf("C\n");
        }
        else if (pid > 0)
        {
            printf("B\n");
        }
    }
    else if (pid >0)
    {
        printf("A\n");
    }
    return 0;
}