// Include necessary header files
#include  <stdio.h>
#include  <string.h>


// Define the size of the strings
#define SIZE 40

// Main function
int main(void)
{
  // Declare and initialize the source and destination strings
  char source[SIZE] = "Original text";
  char destination[SIZE] = "Final text";

  // Declare a character pointer for the return value of strcpy()
  char *return_string;

  // Print the original destination string
  printf("Original value of destination: \"%s\"\n", destination);

  // Use strcpy() to copy the content of source to destination, and store the result in return_string
  return_string = strcpy(destination, source);

  // Print the modified destination string after copying
  printf("Current value of destination after running strcpy: \"%s\"\n", destination);

  // Return 0 to indicate successful execution
  return 0;
}