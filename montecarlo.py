import numpy as np
import matplotlib.pyplot as plt
import random
import math

def points(x1,x2,y1,y2,h):
  x = []
  y = []
  p = []
  for i in range(h):
    x.append(random.random()*(x2-x1)+x1)
    y.append(random.random()*(y2-y1)+y1)
  for i in range(h):
    p.append((x[i],y[i]))
  return p, x, y



def monte_carlo(m,b,e,x1,x2,y1,y2,h,booleen):
  """m, b, e : y = m*x^e+b
  x1, x2, y1, y2 : corners of outer rectangle
  h : amount of points
  booleen : True to graph, False to not graph"""
  r = []
  nr = []
  f = lambda m,b,e,x : m*x**e+b
  f2 = lambda x : math.sqrt(1+x**2)
  p = points(x1,x2,y1,y2,h)[0]
  for co in p:
    if f(m,b,e,co[0]) >= co[1]:
      r.append(co)
    else:
      nr.append(co)
  if booleen == True:
    x = np.linspace(x1, x2, 100)
    plt.plot(x, m*x**e+b, linestyle='solid')
    plt.scatter(points(x1,x2,y1,y2,h)[1], points(x1,x2,y1,y2,h)[2], 10000/h)
    plt.xlabel("Aire = " + str((len(r)/len(p))*(y2-y1)*(x2-x1)))
    plt.show()
  return len(r)/len(p)
print(monte_carlo(-1,9,2,-5,5,-15,9,10000,True))

