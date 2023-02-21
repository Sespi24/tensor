import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
plt.plot(x, np.sin(x))

plt.title("The Seth Coaster")
plt.xlabel("Length of roller coaster")
plt.ylabel("Height of hills")

plt.show()

print ("hello world")