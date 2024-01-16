import os, numpy

c = int(os.environ["A"]) + int(os.environ["B"])
d =  numpy.log(int(os.environ["A"]) * int(os.environ["B"]))
e =  numpy.log(int(os.environ["A"])) + numpy.log(int(os.environ["B"]))
print(c)
print(d)
print(e)