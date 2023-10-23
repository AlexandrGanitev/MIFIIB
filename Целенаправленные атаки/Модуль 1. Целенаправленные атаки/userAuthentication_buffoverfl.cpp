// Задание .
// При помощи переполнения буфера в стеке
// добиться аутентификации пользователя.

# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <time.h>

char *a1 = "01234556789abcdef";

int main(int argc,char *argv[], char *envp[]){

char pass[16];
char name[16];
char pass2[15];

unsigned int i;

    srand(time(NULL));
    // цикл генерирует рандомный или случайный пароль
    for(i=0;i<16;i++){
        pass[i] = a1[rand()%16];
        }
    pass[15] = 0;
    // наша задача переполнить буфер, т.е. ввести больше чем char pass[16] позволяет,
    // 17 буковок "А", и тогда 17-я буковка станет новым паролем
    gets(name);
    gets(pass2);

    if(strcmp(pass,pass2) == 0)
        printf("Hello, legal user %s\n",name);
    else
        printf("Bad password\n");
    
    return 0;
}