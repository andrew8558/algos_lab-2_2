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
    tree.append(Node(x[0], x[1], x[2]))


sorted_tree = []


def inorder(root):
    if root != -1:
        inorder(tree[root].left)
        sorted_tree.append(tree[root].val)
        inorder(tree[root].right)


def check_order(sorted_tree):
    for i in range(1, n):
        if sorted_tree[i] <= sorted_tree[i-1]:
            return False
    return True


if len(tree) != 0:
    inorder(0)
    if check_order(sorted_tree):
        fout.write('CORRECT')
    else:
        fout.write('INCORRECT')
else:
    fout.write('CORRECT')
