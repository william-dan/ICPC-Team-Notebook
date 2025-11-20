##############################
# 10. array & others (less common but handy)
##############################
from array import array

# Memory-compact numeric array
a = array('i', [0]) * n      # signed int
a[i] = 5

# operator: function versions of +, -, *, etc.
import operator as op
op.add(x, y)
op.mul(x, y)
