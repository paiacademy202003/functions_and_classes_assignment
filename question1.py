#Do not import any libraries for this question
"""
Write a function that takes a list of numbers as input and returns the index location
within the list of the largest number. If there is more than one location within the
list that contains the largest number, then have the function return the LAST index
location. For example, f([1,2,3,2,3,1]) should return 4.

You can test your function by running "python question1.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""
def f(l):
    ##########YOUR CODE HERE##########
    pass
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f([1,2,3,4,5,4,3,4,5,3,2,1])
    if y == 8:
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been 8'.format(str(y)))
