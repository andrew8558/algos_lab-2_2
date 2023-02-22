fint = open('input.txt')
n = int(fint.readline())
fout = open('output.txt', 'w')


class Node:
    def __init__(self, value, left, right, height=0):
        self.val = value
        self.left = left
        self.right = right
        self.height = height


tree = []

for i in range(n):
    x = ([int(i) for i in fint.readline().split()])
    tree.append(Node(x[0], x[1]-1, x[2]-1))


for i in range(n-1, -1, -1):
    if tree[i].left != -1:
        l = tree[tree[i].left].height
    else:
        l = -1

    if tree[i].right != -1:
        r = tree[tree[i].right].height
    else:
        r = -1
    tree[i].height = max(l, r) + 1


if len(tree) == 0:
    fout.write(str(0))
else:
    fout.write(str(tree[0].height+1))


