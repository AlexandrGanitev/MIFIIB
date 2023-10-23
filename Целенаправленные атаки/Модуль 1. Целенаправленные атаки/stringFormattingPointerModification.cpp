// Модификация указателя на функцию с отладочной печатью

# include <stdio.h>
# include <string.h>

void fun1(void){

    printf("fun1 execute\n");

    return;
}

void fun2(void){

    printf("fun2 execute\n");

    return;
}

int main(int argc,char *argv[],char **envp){

void (*fun)(void) = fun1;
char buf[16];

    if(argv[1])
        strcpy(buf,argv[1]);
    
    printf("fun %08p = %08p\n",&fun,fun);
    printf("buf %08p\n",buf);

    printf("fun1 %08p\n",fun1);
    printf("fun2 %08p\n",fun2);

    fun();

    return 0;

}