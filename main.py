import math

from optimization.engine import engine

func = lambda x, y: 10 * 2 + x ** 2 - 10 * math.cos(2 * math.pi * x) + y ** 2 - 10 * math.cos(2 * math.pi * y)

dim = 2
k = 100
num = 5000
local_wgh = 0.3
glb_wgh = 0.7

print(engine(func, num, k, dim, local_wgh, glb_wgh))
