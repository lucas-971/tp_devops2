import os

a = 1
b = os.environ['VARIABLE']

if a == b:
    print("A est pareil que B.")
else:
    print("A est différent de B.")
