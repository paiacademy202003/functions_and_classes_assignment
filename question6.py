#do not import any libraries for this question
"""
Write a function that takes a string as input. The function should replace all the lower case characters with their upper case
characters, replace all the upper case letters with their lower case letters, and should leave any characters that are not English
letters unchanged. For example, f('Hello World 12') should return 'hELLO wORLD 12'

You can test your function by running "python question6.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

def f(s):
    ##########YOUR CODE HERE##########
    pass
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f('Hello World 12')
    if y == 'hELLO wORLD 12':
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been hELLO wORLD 12'.format(str(y)))
