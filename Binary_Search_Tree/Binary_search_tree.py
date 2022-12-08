class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, key):
        if n is None: return None
        if n.key > key: return self.get_item(n.left, key)
        elif n.key < key: return self.get_item(n.right, key)
        else: return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None: return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self):
        if self.root is None: return None
        return minimum(self.root)

    def minimum(self, n):
        if n.left is None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root is None: return None
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, key):
        if self.root is None: return None
        self.root = self.del_node(self.root, key)

    def del_node(self, n, key):
        if n is None: return None
        if n.key > key:
            n.left = self.del_node(n.left, key)
        elif n.key < key:
            n.right = self.del_noe(n.right, key)
        else:
            if n.left is None:
                return n.right
            elif n.right is None:
                return n.left
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n

    def pre_order(self, n):
        if n is not None:
            print(n.key, end=' ')
            self.pre_order(n.left)
            self.pre_order(n.right)

    def in_order(self, n):
        if n is not None:
            self.in_order(n.left)
            print(n.key, end=' ')
            self.in_order(n.right)


if __name__ == '__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')

    print('전위: ', end='')
    t.pre_order(t.root)
    print('\n중위: ', end='')
    t.in_order(t.root)
    print('\n250: ', t.get(250))
    t.delete(200)
    print('200 삭제 후')
    print('전위: ', end='')
    t.pre_order(t.root)
    print('\n중위: ', end='')
    t.in_order(t.root)
