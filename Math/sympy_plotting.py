#%% 
from sympy import *    
from sympy.plotting import plot_parametric
from sympy.plotting import plot3d_parametric_line
import math

#%%

t = symbols('t')
x = cos(t)
y = sin(t)
plot_parametric(x, y, (t, 0, 2*pi))
# %%
x = t + 0.5 * cos(10*t)
y = t + 0.5 * sin(10*t)
plot_parametric(x, y, (t, -2*pi, 2*pi))
# %%
x = 4*t + 4
y = t + 2
plot_parametric(x, y, (t, -10, 10))


# %%
# 3d - Example 1 
x = cos(t)
y = sin(t)
z = t

plot3d_parametric_line(x, y, z, (t, 0, 6*math.pi))
# %%
# 3d - Example 2
x = t*cos(t)
y = t*sin(t)
z = t

plot3d_parametric_line(x, y, z, (t, 0, 6*math.pi))
# %%
