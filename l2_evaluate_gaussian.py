#!/usr/bin/env python2

# f(x) = 1/sqrt(2*pi*sigma^2)*exp((-1/2)*(x-mu)^2/sigma^2)

from math import exp
from math import pi
from math import pow
from math import sqrt

def evaluate_gaussian(mu, sigma_sqrd, x):
    x = float(x)
    sigma_sqrd = float(sigma_sqrd)
    mu = float(mu)

    constant = 1 / sqrt(2 * pi * sigma_sqrd)
    exponent = exp(-0.5 * (pow((x - mu), 2) / sigma_sqrd))
    return constant * exponent

if __name__ == "__main__":
    import sys
    print evaluate_gaussian(sys.argv[1], sys.argv[2], sys.argv[3])