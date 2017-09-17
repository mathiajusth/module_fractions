
def closerToZero(a,b):
    if abs(a) <= abs(b):
        return a
    else:
        return b

def gcd(a,b):
    # greatest common divisor
    div = rem = abs(closerToZero(a,b))
    while rem != 0:
        rem = (a % div) + (b % div)
        div = div - 1
    return div + 1

class frac:
    def __init__(self, top, bot):
        self.top = top
        self.bot = bot

    def __repr__(self):
        return "{}/{}".format(self.top, self.bot)

    def __add__(self,other):
        return self.bruteAdd(other).simplify()

    def __neg__(self):
        return frac(-self.top, self.bot).simplify()

    def __sub__(self,other):
        return (self + (-other)).simplify()

    def __mul__(self,other):
        return self.bruteMul(other).simplify()

    def __truediv__(self,other):
        return (self * other.swap()).simplify()

    def __floordiv__(self,other):
        return (self * other.swap()).simplify()

    def __abs__(self):
        return frac(abs(self.top),abs(self.bot)).simplify()

    def __le__(self, other):
        return self.top * other.bot <= self.bot * other.top

    def __ge__(self, other):
        return other <= self

    def __eq__(self, other):
        return self >= other and other >= self
 
    def __lt__(self, other):
        return not self >= other

    def __gt__(self, other):
        return not other >= self

    def __ne__(self, other):
        return not self == other

    def swap(self):
        return frac(self.bot,self.top)

    def simplify(self):
        top = self.top // gcd(self.top, self.bot)
        bot = self.bot // gcd(self.top, self.bot)
        if top * bot > 0:
            return frac(abs(top),abs(bot))
        else:
            return frac(-abs(top),abs(bot))

    def bruteAdd(self, other):
        top = (self.top * other.bot) + (other.top * self.bot)
        bot = self.bot * other.bot
        return frac(top, bot)

    def bruteMul(self, other):
        top = self.top * other.top
        bot = self.bot * other.bot
        return frac(top, bot)

#--------------TEST frac----------------


x = frac(3,-2)
y = frac(4,-2)
z = frac(5,0)
