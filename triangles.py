
#   1 
#  1 2
# 1 2 3 
#1 2 3 4


def triangles(n):
    for row in range(1, n + 1):
        spaces = n - row
        # print(spaces)
        print(" " * spaces, end="")
        for i in range(1, row + 1):
            print(str(i) + " ", end="")
        print()

triangles(4)


