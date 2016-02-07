# -*- coding: cp1252 -*-
"""This is a doc string"""
class physFuncLib():

"""Class'ified so as to enable pynsource umlification"""
    def yfunc(t, v0):
        """Gives distance of descent over time t for initial velocity v0.
    doc strings can contain examples:

    >>> def yfunc(t, v0):
        g = 9.81
        return v0*t - 0.5*g*t**2

    >>> descent = yfunc(5,0)

    >>> print descent
    -122.625

    """
        g = 9.81
        return v0*t - 0.5*g*t**2

    descent = yfunc(5,0)
    print descent


    def yfunc(t, v0):
        """Again with argument value assignment eliminating the depency on arg sequence.
    """
        g = 9.81
        return v0*t - 0.5*g*t**2

    print yfunc(t=5,v0=0)


    def yfunc(t, v0):
        """To return the velocity of the ball as well
    """
        g = 9.81
        y = v0*t - 0.5*g*t**2
        dydt = v0 - g*t
        return y, dydt  #returns two variables so must be called with
                        #two variables on the left side of the assignment operator.
                        #The return value here is actually a tuple


    def makelist(start, stop, inc):
        """an iterative list math function given arguments start, stop, inc"""
        value = start #set value to start
        result = [] #initialize result array (list) to
                    #make it available to the rest of the function
        
        while value <= stop:  #*Enter while loop and loop as long as value is
                            #is less than or equal to stop
            result.append(value) #append value to list
            value = value + inc #increase value
        return result #return value




    def L(x, n):
        """a function for approximating ln(1 + x) for finite n
        intro to programming page 77-78"""
        s = 0
        for i in range(1, n+1):
            s += (1.0/i)*(x/(1.0+x))**i
            return s


    def L(x, n):
        """ln(x + 1) approx. with error information"""

        s = 0
        for i in range(1, n+1):
            s += (1.0/i)*(x/(1.0+x))**i
            value_of_sum = s
            first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
            from math import log
            exact_error = log(1+x) - value_of_sum
            return value_of_sum, first_neglected_term, exact_error

        
    def table(x):
        """a function that creates a table of error information for various values of n
    since there is no return function, python returns an invisible "return None"
    which is the equivalent to C's void func()"""

        print ’\nx=%g, ln(1+x)=%g’ % (x, log(1+x))
        for n in [1, 2, 10, 100, 500]:
            value, next, error = L(x, n)
            print ’n=%-4d %-10g (next term: %8.2e ’\
            ’error: %8.2e)’ % (n, value, next, error)


            
    from math import pi, exp, sin
    def f(t, A=1, a=1, omega=2*pi):
        """function for Ae^-at*sin(wt)
    """
        return A*exp(-a*t)*sin(omega*t)




    def L2(x, epsilon=1.0E-6):
        """#a function that returns a value within a certain tolerance defined as some
    #epsilon"""
        x = float(x)
        i = 1
        term = (1.0/i)*(x/(1+x))**i
        s = term
        from math import fabs # fabs(x) equals |x|
        while fabs(term) > epsilon:
            i += 1
            term = (1.0/i)*(x/(1+x))**i
            s += term
        return s, i

    def line(x0, y0, x1, y1):
        """
        Compute the coefficients a and b in the mathematical
        expression for a straight line y = a*x + b that goes
        through two points (x0, y0) and (x1, y1).
        x0, y0: a point on the line (floats).
        x1, y1: another point on the line (floats).
        return: coefficients a, b (floats) for the line (y=a*x+b).
        """
        a = (y1 - y0)/float(x1 - x0)
        b = y0 - a*x0
        return a, b


    def diff2(f, x, h=1E-6):
        """Computes the second order derivative of a function f(x)
    Application:

    def g(t):
        return t**(-6)
        
    t = 1.2
    d2g = diff2(g, t)
    print "g’’(%f)=%f" % (t, d2g)

    Beware of round off errors at h<10^-8
    """
        r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
        return r

    """Here is an example of a function for polynomials of 2nd degree:"""

    # function definition:
    def quadratic_polynomial(x, a, b, c):
        value = a*x*x + b*x + c
        derivative = 2*a*x + b
        return value, derivative
    # function call:
    x = 1
    p, dp = quadratic_polynomial(x, 2, 0.5, 1)
    p, dp = quadratic_polynomial(x=x, a=-4, b=0.5, c=0)

"""Intro to progra. ~/random/Deck.py"""
class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [s+r for s in suits for r in ranks]
        random_number.shuffle(self.deck)

    def hand(self, n=1):
        """Deal n cards. Return hand as list."""
        hand = [self.deck[i] for i in range(n)]  # pick cards
        del self.deck[:n]                        # remove cards
        return hand

    def deal(self, cards_per_hand, no_of_players):
        """Deal no_of_players hands. Return list of lists."""
        return [self.hand(cards_per_hand) \
                for i in range(no_of_players)]

    def putback(self, card):
        """Put back a card under the rest."""
        self.deck.append(card)

    def __str__(self):
        return str(self.deck)

#Monte carlo integration (Intro to Prog chapt 10)

    def MCint(f, a, b, n):
        s = 0
        for i in range(n):
            x = random_number.uniform(a, b)
            s += f(x)
        I = (float(b-a)/n)*s
        return I

    from numpy import *

    def MCint_vec(f, a, b, n):
        x = random.uniform(a, b, n)
        s = sum(f(x))
        I = (float(b-a)/n)*s
        return I

    def MCint2(f, a, b, n):
        s = 0
        # store the intermediate integral approximations in an
        # array I, where I[k-1] corresponds to k function evals.
        I = zeros(n)
        for k in range(1, n+1):
            x = random_number.uniform(a, b)
            s += f(x)
            I[k-1] = (float(b-a)/k)*s
        return I

    def MCint3(f, a, b, n, N=100):
        s = 0
        # store every N intermediate integral approximations in an
        # array I and record the corresponding k value
        I_values = []
        k_values = []
        for k in range(1, n+1):
            x = random_number.uniform(a, b)
            s += f(x)
            if k % N == 0:
                I = (float(b-a)/k)*s
                I_values.append(I)
                k_values.append(k)
        return k_values, I_values

    def f1(x):
        return 2 + 3*x

    a = 1; b = 2; n = 1000000; N = 10000
    k, I = MCint3(f1, a, b, n, N)
    from scitools.std import plot
    error = 6.5 - array(I)
    plot(k, error, title='Monte Carlo integration',
         xlabel='n', ylabel='error', hardcopy='tmp.eps')

