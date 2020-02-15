"""
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

"""


# My solution --------------------

def dig_pow(n, p):

    # Convereting string to a list of numbers
    digits =  [int(d) for d in str(n)]

    # variable to hold some of function, and variable to hold the intial exponet
    sum_num_power = 0
    i = p

    #function is done iteratively
    for digit in digits:
        print(digit)
        sum_num_power = sum_num_power + digit**(i)
        i = i + 1


    if sum_num_power%n == 0:
        return (sum_num_power/n)

    return -1


    # Top solution --------------------

def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1
