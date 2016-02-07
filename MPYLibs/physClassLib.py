""" math and physics class definitions from Introduction to Programming,
although most of these are perfectly well managed by SumPy functions."""

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    #def __eq__(self, other):
        """The function float_eq found in
        the module scitools.numpytutils (if you do not already have float_eq from
        a from scitools.all import *), see also Exercise 2.49, is an easy-to-use tool
        for comparing float objects."""
        #return self.x == other.x and self.y == other.y
    def __eq__(self, other):
        return float_eq(self.x, other.x) and float_eq(self.y, other.y)
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def __ne__(self, other):
        return not self.__eq__(other) # reuse __eq__
##    def __len__(self):
##        """the absolute value of a vector is mathematically the same as the length of the
##vector."""
##        # reuse implementation of __abs__
##        return abs(self) # equiv. to self.__abs__()

class Rocket:
    """Tsiolkovsky Rocket equation per xkcd"""
    def __init__(self, vexhaust, deltav,mstart):
        self.vexhaust = vexhaust #usually between 2.5 and 4.5 km/s
        self.deltav = deltav
        self.mstart = mstart
        self.vescape = 13 #kilometers per second
    def shiptofuel(self.vescape,vexhaust):
        #how many kilos of fuel for how many kilos of ship
        ratio = exp(vescape,vexhaust)
        return ratio
    #Need equations for fuel-to-energy ratios, etc.


"""Tangent:  New stupid ideas for launch mechanisms:

a.  We unfurl a huge light said in space tethered to ships on the ground and use either solar wind or lasers to send it aloft.

b.  We use tethers to "hook" the moon and pull the space ships into space as the mooon passes over, disconnect at the desired tangent.

"""
class SpacePoint:
    """This could be really cool for representing vertices in a mesh or rgb values"""
    counter = 0
    def __init__(self, x, y, z):
        self.p = (x,y,z)
        SpacePoint.counter +=1

class Gravity:
    """Gravity force between two physical objects.  IntroToProg, pg 470 """

    def __init__(self, m, M):
        self.m = m           # mass of object 1
        self.M = M           # mass of object 2
        self.G = 6.67428E-11 # gravity constant, m**3/kg/s**2

    def force(self, r):
        G, m, M = self.G, self.m, self.M
        return G*m*M/r**2

    def visualize(self, r_start, r_stop, n=100):
        from scitools.std import plot, linspace
        r = linspace(r_start, r_stop, n)
        g = self.force(r)
        title='Gravity force: m=%g, M=%g' % (self.m, self.M)
        plot(r, g, title=title)


"""intervalmath:  for calculating with quantities that include uncertainties.  found in IntervalMath.py"""
    

"""Sketches of ideas about physics problem class development"""

class PhysicsProblem:
    def __init__(self)
    """Text from either homework or tests"""
    self.problemStatement = problemstatement
    self.knowns = knowns
    self.unknowns
    
    
    