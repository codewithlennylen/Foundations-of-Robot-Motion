import modern_robotics as mr
import numpy as np


# print(help(mr.RotInv))


R = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]])

invR = mr.RotInv(R)

print (invR)