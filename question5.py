#Do not import any libraries for this question
"""
Write a function that returns both the sample mean and sample standard deviation of a list of numbers. Your function will calculate
the mean and standard deviation separately and the last line of your function should look something like

return m, sd

where m is the mean, and sd is the standard deviation. Make sure to return them in that order. See
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
for the equations to calculate the sample standard deviation. Make sure you use the sample standard deviation and not the population
standard deviation.

You can test your function by running "python question5.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

def f(l):
    ##########YOUR CODE HERE##########
    pass
    ###########END CODE###############

#Do not edit the code below
if __name__ == '__main__':
    l = [round(x,4) for x in f([2,6,4,1,4,6,4,3,3,7,5,2,3,6,3,8])]
    if l[0] == 4.1875 and l1 == 1.9738:
        print('Test passed')
    else:
        print('Test failed, m = {} and sd = {} when they should have been 4.1875 and 1.9738'.format(str(l[0]), str(l[1])))
