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


#%% 
# %matplotlib widget
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
  
# creating random dataset
xs = [14, 24, 43, 47, 54, 66, 74, 89, 12,
      44, 1, 2, 3, 4, 5, 9, 8, 7, 6, 5]
  
ys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3,
      5, 2, 4, 1, 8, 7, 0, 5]
  
zs = [9, 6, 3, 5, 2, 4, 1, 8, 7, 0, 1, 2, 
      3, 4, 5, 6, 7, 8, 9, 0]
  
# creating figure
fig = plt.figure()
ax = Axes3D(fig)
  
# creating the plot
plot_geeks = ax.scatter(xs, ys, zs, color='green')
  
# setting title and labels
ax.set_title("3D plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
  
# displaying the plot
plt.show()
# %%
import plotly
import plotly.graph_objs as go
#%% 
trace = go.Scatter3d(
    x=[1, 2, 3],  # <-- Put your data instead
    y=[4, 5, 6],  # <-- Put your data instead
    z=[7, 8, 9],  # <-- Put your data instead
    mode='markers',
    marker={'size': 10, 'opacity': 0.8}
    )

layout = go.Layout(margin={'l': 0, 'r': 0, 'b': 0, 't': 0})

data = [trace]

plot_figure = go.Figure(data=data, layout=layout)
plot_figure
# plotly.offline.iplot(plot_figure)
# %%
# creating 3d plot using matplotlib 
# in python
  
# for creating a responsive plot
# %matplotlib widget
  
# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
  
# creating random dataset
xs = [14, 24, 43, 47, 54, 66, 74, 89, 12,
      44, 1, 2, 3, 4, 5, 9, 8, 7, 6, 5]
  
ys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3,
      5, 2, 4, 1, 8, 7, 0, 5]
  
zs = [9, 6, 3, 5, 2, 4, 1, 8, 7, 0, 1, 2, 
      3, 4, 5, 6, 7, 8, 9, 0]
  
# creating figure
fig = plt.figure()
ax = Axes3D(fig)
  
# creating the plot
plot_geeks = ax.scatter(xs, ys, zs, color='green')
  
# setting title and labels
ax.set_title("3D plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
  
# displaying the plot
plt.show()
plotly.offline.iplot(plot_figure)
# %%
from sympy import symbols
from sympy.plotting import plot3d
x, y, z = symbols('x y z')

plot3d(x*y, (x, -5, 5), (y, -5, 5))
# %%
from sympy import plot_parametric, symbols, cos, sin
u = symbols('u')
plot_parametric((cos(u), sin(u)), (u, -5, 5))
# %%
from sympy import symbols, cos, sin
from sympy.plotting import plot3d_parametric_line
u = symbols('u')
plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))
# %%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
  
# creating random dataset
xs = [14, 24, 43, 47, 54, 66, 74, 89, 12,
      44, 1, 2, 3, 4, 5, 9, 8, 7, 6, 5]
ys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3,
      5, 2, 4, 1, 8, 7, 0, 5]
zs = [9, 6, 3, 5, 2, 4, 1, 8, 7, 0, 1, 2, 
      3, 4, 5, 6, 7, 8, 9, 0]
# creating figure
fig = plt.figure()
ax = Axes3D(fig)
# creating the plot
plot_geeks = ax.scatter(xs, ys, zs, color='green')  
# setting title and labels
ax.set_title("3D plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
# displaying the plot
plt.show()

# %%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = [74, 74, 74, 74, 74, 74, 74, 74, 192, 74]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
z =  np.zeros(10)
dx = np.ones(10)*10
dy = np.ones(10)
dz = [1455, 1219, 1240, 1338, 1276, 1298, 1292, 1157, 486, 1388]

fig = plt.figure()
ax = fig.add_Scatter3d()
bar3d = ax.bar3d(x, y, z, dx, dy, dz, color='C0')

ax.set_title("Data Analysis ")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
# %%
from sympy import symbols, cos, sin
from sympy.plotting import plot3d_parametric_line
u = symbols('u')

plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))
# %%
