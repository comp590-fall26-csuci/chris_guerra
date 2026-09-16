# this script prints the first 25 numbers in the fibonacci sequence to a file in a local directory named output
# 2 methods are provided: one that prints iteratively, and another that prints recursively

# directory for output files
DIR = 'output'

# filename for output file
NAME = 'fibonacci.txt'

# number of fibonacci numbers to print
LIM = 25

from pathlib import Path

def main():
    #fib_iter()
    fib_rec()

def fib_iter():
    """
    Prints the fibonacci numbers iteratively to the screen and to a file in the output directory.
    """
    # delete the output file for clean environment
    del_file(DIR, NAME)

    # intialize the first two numbers
    val1 = 0
    val2 = 1

    # iteratively calculate the fibonacci numbers and print them
    for i in range(LIM):
        # print to screen
        print(val1)

        # print to file
        write_file(DIR, NAME, f"{val1}\n")

        # save values for the next iteration
        next = val1 + val2
        val1 = val2
        val2 = next

def fib_rec():
    """
    Prints the fibonacci numbers recursively to the screen and to a file in the output directory.
    """
    # delete the output file for clean environment
    del_file(DIR, NAME)

    # call the recursive function to print the fibonacci numbers
    fib_rec_helper(0, 1, 1)

def fib_rec_helper( first, second, iter ):
    """
    prints the fibonacci numbers until iter reaches the given limit
    """
    if iter == LIM:
        return
    print( first )
    write_file(DIR, NAME, f"{first}\n")
    fib_rec_helper(second, first + second, iter + 1)

def del_file( path, file ):
    """
    Deletes a file in the specified path if it exists.
    """
    file_path = Path(path) / file
    if file_path.is_file():
        file_path.unlink()

def write_file( path, file, text ):
    """
    Appends the given text to the file in the specified path.
    """
    file_path = Path(path) / file
    with open(file_path, 'a') as f:
        f.write(text)


if __name__ == "__main__":
    main()