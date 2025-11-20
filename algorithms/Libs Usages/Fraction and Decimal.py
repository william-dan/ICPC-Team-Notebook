##############################
# 7. fractions / decimal (exact / high precision)
##############################
from fractions import Fraction

f = Fraction(1, 3) + Fraction(2, 5)    # exact rational arithmetic
f.numerator, f.denominator

# decimal (if you really need precise decimals; slower than float)
from decimal import Decimal, getcontext
getcontext().prec = 50
x = Decimal('0.1') + Decimal('0.2')
