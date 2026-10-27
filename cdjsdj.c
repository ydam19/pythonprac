#include <stdio.h>

int main(void)
{
    printf("값을 입력하세요 : ");
    int a, b;
    
    scanf("%d %d", &a, &b);
    printf("%d\n", a+b);
    return 0;
}