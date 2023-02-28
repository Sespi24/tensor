import numpy as np
import matplotlib.pyplot as plt

x = 10
y = 10
Dx = 0.01
yPoints = []
xPoints = []

def givenFunction(x, y):
    return(x+y)/(x-y)

while y<0:
    y = y + Dx*givenFunction(x,y)
    x = x + Dx
    yPoints.append(round(y, 2))
    xPoints.append(round(x, 2))

yPoints = np.asarray(yPoints)
xPoints = np.asarray(xPoints)

plt.plot(xPoints, yPoints)
plt.show()