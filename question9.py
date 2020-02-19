import os
#Do no import any other libraries
"""
Write a function that takes a path to a directory as input and returns a list of all the immediate subdirectories within that
directory. Making use of the os library will be helpful here. See https://docs.python.org/3/library/os.html for details. Some of the
built in os functions that may be helpful for this problem are os.listdir(), os.path.join(), os.path.isdir(), and os.getcwd(). For
example, there is a directory within this repository called test_dir. Within this directory there are 2 files called f1.txt and
f2.txt, and also a subdirectory called test_subdir. Given the path to test_dir (which will change depending on where in your
computer you downloaded the repository), the function should return the list ['test_subdir']. f1.txt and f2.txt are files, not
subdirectories. Return your list sorted in alphabetical order.

You can test your function by running "python question8.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

def f(path):
    ##########YOUR CODE HERE##########
    pass
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f('test_dir')
    if y == ['test_subdir']:
        print('Test passed')
    else:
        print("Test failed, y = {} when it should have been ['test_subdir']".format(str(y)))
