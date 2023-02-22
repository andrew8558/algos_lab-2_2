import sys
sys.setrecursionlimit(1000000)

f = open('input.txt')
n = int(f.readline())
fout = open('output.txt', 'w')


class Node:
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right


tree = []

for i in range(n):
    x = ([int(i) for i in f.readline().split()])
    tree.append(Node(x[0], x[1]-1, x[2]-1))


def check_correctness(node, left, right):
    if node == -1:
        return True
    if left != -1 and tree[node].val <= left:
        return False
    if right != -1 and tree[node].val >= right:
        return False
    if not check_correctness(tree[node].left, left, tree[node].val):
        return False
    if not check_correctness(tree[node].right, tree[node].val, right):
        return False
    return True


if len(tree) != 0 :
    if check_correctness(0, -(10**10), 10**10):
        fout.write('YES')
    else:
        fout.write('NO')
else:
    fout.write('YES')
