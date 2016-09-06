#!/usr/bin/env python2

# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

# new_mean = (1/(var1 + var2))*(var2*mean1 + var1*mean2)
# new_variance = 1/((1/var1) + (1/var2))

def update(mean1, var1, mean2, var2):
    mean1 = float(mean1)
    var1 = float(var1)
    mean2 = float(mean2)
    var2 = float(var2)

    new_mean = (1. / (var1 + var2)) * (var2 * mean1 + var1 * mean2)
    new_var = 1. / ((1 / var1) + (1 / var2))
    return [new_mean, new_var]

# print update(10.,8.,13., 2.)

if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:5]
    print update(*arguments)