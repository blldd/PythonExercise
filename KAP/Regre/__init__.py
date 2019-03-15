import sys

import os

print(sys.path)


path = os.path.abspath(os.curdir)
r1 = "/".join(path.split("/")[:-1])
r2 = "/".join(path.split("/")[:-2])
sys.path.append(r1)
sys.path.append(r2)

print(sys.path)

