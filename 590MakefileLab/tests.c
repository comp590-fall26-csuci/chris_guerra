#include <stdio.h>
#include "fibonacci.h"
#include "utest.h"

// constants used to evaluate the fibonacci() function
const int FIB_ARRAY[10] = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 };

UTEST( fibonacci, test1 )
{
    ASSERT_EQ( fibonacci(1), FIB_ARRAY[0] );
}

UTEST( fibonacci, test2 )
{
    ASSERT_EQ( fibonacci(2), FIB_ARRAY[1] );
}

UTEST( fibonacci, test3 )
{
    ASSERT_EQ( fibonacci(3), FIB_ARRAY[2] );
}

UTEST( fibonacci, test4 )
{
    ASSERT_EQ( fibonacci(4), FIB_ARRAY[3] );
}

UTEST( fibonacci, test5 )
{
    ASSERT_EQ( fibonacci(5), FIB_ARRAY[4] );
}

UTEST( fibonacci, test6 )
{
    ASSERT_EQ( fibonacci(6), FIB_ARRAY[5] );
}

UTEST( fibonacci, test7 )
{
    ASSERT_EQ( fibonacci(7), FIB_ARRAY[6] );
}

UTEST( fibonacci, test8 )
{
    ASSERT_EQ( fibonacci(8), FIB_ARRAY[7] );
}

UTEST( fibonacci, test9 )
{
    ASSERT_EQ( fibonacci(9), FIB_ARRAY[8] );
}

UTEST( fibonacci, test10 )
{
    ASSERT_EQ( fibonacci(10), FIB_ARRAY[8] );
}

UTEST_MAIN()
