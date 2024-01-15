import os

a = 1
b = os.environ['VAR_TEST']

if a == b:
    print("A est pareil que B.")
else:
    print("A est différent de B.")
