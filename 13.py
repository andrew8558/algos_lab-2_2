f = open('input.txt')
n = int(f.readline())
fout = open('output.txt', 'w')


class Node:
    def __init__(self, value, left, right, height=0, balance=0, parent=-1):
        self.val = value
        self.left = left
        self.right = right
        self.height = height
        self.balance = balance
        self.parent = parent


tree = []


for i in range(n):
    x = ([int(i) for i in f.readline().split()])
    tree.append(Node(x[0], x[1]-1, x[2]-1))


def search_height(root):
    if root != -1:
        l = search_height(tree[root].left)
        r = search_height(tree[root].right)
        tree[root].height = max(l, r)+1
        tree[root].balance = r-l
        return max(l, r)+1
    else:
        return -1


def left_turn(root, right):
    if tree[right].balance == -1:
        right_turn_2(right, tree[right].left)
    tree[root].right, tree[right].left = tree[right].left, tree[root].right
    tree[root].height -= 2
    tree[root].balance, tree[right].balance = 0, 0
    tree[root], tree[right] = tree[right], tree[root]


def right_turn_2(root, left):
    tree[root].left, tree[left].right = tree[left].right, tree[root].left
    tree[root].height, tree[left].height = tree[left].height, tree[root].height
    tree[root], tree[left] = tree[left], tree[root]
    tree[root].balance = 1
    if tree[left].left == -1 and tree[left].right == -1:
        tree[left].balance = 0
    elif tree[left].left == -1:
        tree[left].balance = tree[tree[left].left].height
    elif tree[left].right == -1:
        tree[left].balance = tree[tree[left].right].height
    else:
        tree[left].balance = tree[tree[left].right].height - tree[tree[left].left].height


def func(root):
    if root != -1:
        left = tree[root].left
        right = tree[root].right
        child_left = func(left)
        child_right = func(right)
        if child_left:
            tree[root].left = child_left
        if child_right:
            tree[root].right = child_right
        if left != -1 and left < root:
            tree[left], tree[root] = tree[root], tree[left]
            tree[left].left = root
            return left
        if right != -1 and right < root:
            tree[right], tree[root] = tree[root], tree[right]
            tree[right].right = root
            return right


def search_parent(root=0):
    left = tree[root].left
    right = tree[root].right
    if left != -1:
        tree[left].parent = root
    if right != -1:
        tree[right].parent = root
    if left != -1:
        search_parent(left)
    if left != -1:
        search_parent(right)


search_height(0)
left_turn(0, tree[0].right)
search_parent()

for i in range(1, n):
    while i < tree[i].parent:
        parent = tree[i].parent
        if tree[parent].left == i:
            tree[parent].left = parent
        else:
            tree[parent].right = parent
        tree[i].parent = i
        tree[i], tree[parent] = tree[parent], tree[i]

        left = tree[parent].left
        right = tree[parent].right
        if left != -1:
            tree[left].parent = parent
        if right != -1:
            tree[right].parent = parent

        left = tree[i].left
        right = tree[i].right
        if left != -1:
            tree[left].parent = i
        if right != -1:
            tree[right].parent = i

        new_parent = tree[i].parent
        if tree[new_parent].left == parent:
            tree[new_parent].left = i
        else:
            tree[new_parent].right = i

fout.write(str(len(tree))+'\n')
for i in tree:
    if i:
        fout.write(f"{i.val} {i.left+1} {i.right+1}\n")
