/* contains line with simple inline commects */

int main(int argc, char const *argv[])
{
    int a = 1; // this is a simple inline comment
    int b = 1; /* this is a inline multiline comment */
    if (a == 1) { // this is another simple inline comment
        /* do nothing */
    } else if (b == 1) { /* this is a inline multiline comment */
        // do nothing
    }
    return 0;
}
