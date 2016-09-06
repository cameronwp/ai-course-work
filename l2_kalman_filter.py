#!/usr/bin/env python2

# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

def update(mean1, var1, mean2, var2):
    mean1 = float(mean1)
    var1 = float(var1)
    mean2 = float(mean2)
    var2 = float(var2)

    new_mean = (1. / (var1 + var2)) * (var2 * mean1 + var1 * mean2)
    new_var = 1. / ((1 / var1) + (1 / var2))
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    mean1 = float(mean1)
    var1 = float(var1)
    mean2 = float(mean2)
    var2 = float(var2)

    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sigma = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].

for m in range(len(measurements)):
    [mu, sigma] = update(mu, sigma, measurements[m], measurement_sig)
    [mu, sigma] = predict(mu, sigma, motion[m], motion_sig)

print [mu, sigma]