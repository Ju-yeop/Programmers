class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right
        self.height = height

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n is None: return 0
        return n.height

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None: return Node(key, value, 1)
        if n.key > key: n.left = self.put_item(n.left, key, value)
        elif n.key < key: n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)

        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)

        return n


t = AVL()
t.put(75, 'apple')
t.put(80, 'grape')
t.put(85, 'lime')
t.put(20, 'mango')
t.put(10, 'strawberry')
t.put(50, 'banana')
t.put(30, 'cherry')
t.put(40, 'watermelon')
t.put(70, 'melon')
t.put(90, 'plum')