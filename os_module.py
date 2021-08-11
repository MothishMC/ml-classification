import os

## absolute path from root directory
print(os.path.abspath(__file__))

## absolute path 1 step before
print(os.path.dirname(os.path.abspath(__file__)))

## absolute path 2 steps before
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))