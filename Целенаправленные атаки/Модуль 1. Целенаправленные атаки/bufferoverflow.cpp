#include <string.h>
#include <string.h>
#include <cstdio>
int main(int argc, char *argv[])
{
        int a = 0xFFFFFFFF;
		char buf[20];
		int b = 0xEEEEEEEE;
		if(argv[1])
           		strcpy(buf, argv[1]);
		printf("a\t%p: %x\n", &a, a);
		printf("b\t%p: %x\n", &b, b);
        return 0;
}