#do not import any libraries for this question
"""
Given 2 two dimensional points (x1,y1) and (x2,y2), there exists a line that connects the 2 points that will have
a corresponding equation y = mx + b where m is the slope of the line and b is the y intercept. Write a function that
takes in 4 values x1, y1, x2, y2 in that order as input and returns m and b, the slope and y intercept of the connecting
line. In other words your function will calculate the values m and b, and the last line of your function should
look something like

return m, b

Note: you may run into cases where the line connecting the 2 points is a vertical line. In these cases, have your function
return None, None. (The keyword None, not the string 'None')

You can test your function by running "python question3.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

def f(x1, y1, x2, y2):
    ##########YOUR CODE HERE##########
    pass
    ###########END CODE###############

#Do not edit the code below
if __name__ == '__main__':
    m, b = f(1,5,4,2)
    if m == -1 and b == 6:
        print('Test passed')
    else:
        print('Test failed, m = {} and b = {} when they should have been -1 and 6'.format(str(m), str(b)))
