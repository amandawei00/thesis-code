import numpy as np
from qutrits import gen_m

r12 = gen_m([0., 0., 0.34441171, 0.91115213, 0.0224759,  0.44814102, 0.68650592, 0.81013422, 0.74834805])
r13 = gen_m([0., 0., 0.89133587, 0.19062182, 0.24736693, 0.89141978, 0.96533478, 0.40336059, 0.00137088])

print(np.abs(np.matmul(np.asmatrix(r12).getH(), r13)))
