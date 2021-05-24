
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <unistd.h>

using namespace std;
void printResult(char * input){
    char buffer[30];
    strcpy(buffer, input);
}

int main(int argc, char *argv[])
{

	
	 

	// a prompt how to execute the program...
	if (argc < 2)
	{
			printf("strcpy() NOT executed....\n");
			printf("Syntax: %s <characters>\n", argv[0]);
			exit(0);
	}

	
	
    printResult(argv[1]);
    
	//printf("buffer content= %s\n", buffer);
    printf("function correctly executed...\n");

    //printResult();

	return 0;
}
