//Модификация буферов при переполнении буфера в стеке.

#include <stdio.h>
#include <string.h>

int main(int argc,char *argv[], char *envp[]){

char buf1[16];
char buf2[16];
char buf3[16];
unsigned int i = 0;

    memset(buf1,0,sizeof(buf1));
    memset(buf2,0,sizeof(buf2));
    memset(buf3,0,sizeof(buf3));

    strcpy(buf1,"Test string");

    if(argv[1])
        strcpy(buf2,argv[1]);

    if(argv[2]){
        while(argv[2][i]){
            buf3[i] = argv[2][i];
            i++;
        }
    }

    printf("buf1 %08p: %s\n",buf1,buf1);
    printf("buf2 %08p: %s\n",buf2,buf2);
    printf("buf3 %08p: %s\n",buf3,buf3);

    return 0;
}