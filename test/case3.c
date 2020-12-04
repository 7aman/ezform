/* contains different styles of preprocessor */

#include <stdint.h>
#include <stdio.h>
int main(int argc, char const *argv[])
{
#include <time.h>
#include <string.h>
    int a = 1; // this is a simple inline comment
#define ALL 1
    int b = 1; /* this is a splitted
    inline multiline comment */
    if (a == 1)
    { // this is another simple inline comment
        /* do
        nothing */
    }
    else if (b == 1)
    { /* this is a
            inline multiline comment */

        // do
        // nothing
    }
    return 0;
}
