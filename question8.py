#do not import any libraries for this question
"""
Write a function that takes a path to a text file as input and returns a list of strings, where each string shows one of the lines in the
file. The strings should be ordered by the order that they appeared in the text. Each line in the text file will contain some empty whitespace
and the end of the line, and possibly at the beginning depending on the file you are working with. Before appending the lines to the list
being returned, you should remove this whitespace. The build in strip() method may be helpful. For example, there is a text file called text_text.txt.
Your function should open this file given its path and return the list ['Roses are red,', 'Violets are blue,', 'Sugar is sweet,', 'And so are you.'].
See https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python for an intro to file processing.

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
    y = f('test_text.txt')
    if y == ['Roses are red,', 'Violets are blue,', 'Sugar is sweet,', 'And so are you.']:
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been the list written above'.format(str(y)))
