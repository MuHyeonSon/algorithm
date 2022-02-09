#include<cs50.h>
#include<stdio.h>

void recursion(int h);

int main(void)
{
    int height = get_int("Height : ");

    recursion(height);
}

void recursion(int h)
{
    if(h == 0)
    {
        return;
    }
        
    recursion(h-1);

    for(int i = 0; i<h; i++)
    {
        printf("#");
    }
    printf("\n"); 
}

# recursion(재귀) : 함수가 본인 스스로를 호출해서 사용하는 것.
