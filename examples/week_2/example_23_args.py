import sys

args = sys.argv

print("Got arguments: ")
for i, arg in enumerate(args):
    print(f'{i}: {arg} {type(arg)}')
