# -*- coding: utf-8 -*-
"""
Ali Khandwalla, November 9th, 2025
Domain Coloring Visualizer
"""

import numpy as np
import matplotlib.pyplot as plt
from mpmath import cplot
import mpmath as mp

# ask the user for the function once
expr = input("Enter a function of z (example: z**2 + 36, 1/z, z+5): ")

# define the function for cplot
def f(z):
    return eval(expr, {"z": z, "mp": mp, "np": np, "__builtins__": {}})

# plot it
cplot(f, re=[-10, 10], im=[-10, 10], points=2000, color="default")

plt.title(f"Domain coloring of f(z) = {expr}")
plt.show()
