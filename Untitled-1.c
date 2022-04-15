#include <stdio.h>
int main()
{
    int km;
 float m,cm,foot,inch;
printf("the distance between two places in km");
scanf("%d %f %f %f %f", &km,&m,&cm,&foot,&inch);
m=(1000)*km;
cm=(100000)*km;
foot=(3280.84)*km;
inch=(39370.1)*km;
printf("result is = %f",m\n,cm\n,foot\n,inch\n);
getch();
return 0;
}