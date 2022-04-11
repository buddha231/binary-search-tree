class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def replace_with(self, node):
        if node == node.parent.right:
            node.parent.right = node.right
        else:
            node.parent.left = node.right
        node.left = self.left
        node.right = self.right
        node.parent = self.parent
        if self == self.parent.right:
            self.parent.right = node
        else:
            self.parent.left = node
        del(self)


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, key, value):
        node = _Node(key, value)
        if self._root is None:
            self._root = node
            self._size += 1
            return

        x = self._root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if node.key < y.key:
            y.left = node
        else:
            y.right = node
        self._size += 1

    def search(self, key):
        node = self._search(key, self._root)
        return node.value if node else False

    def _search(self, key, node):
        if node is None:
            return False
        if key < node.key:
            return self._search(key, node.left)
        elif key > node.key:
            return self._search(key, node.right)
        else:
            return node

    def inorder_walk(self):
        walk = list()
        self._inorder_walk(self._root,  walk)
        return walk

    def _inorder_walk(self, node, walk):
        if node is None:
            return
        self._inorder_walk(node.left, walk)
        walk.append(node.key)
        self._inorder_walk(node.right, walk)

        return walk

    def postorder_walk(self):
        walk = list()
        self._postorder_walk(self._root,  walk)
        return walk

    def _postorder_walk(self, node, walk):
        if node is None:
            return
        self._postorder_walk(node.left, walk)
        self._postorder_walk(node.right, walk)
        walk.append(node.key)

        return walk

    def preorder_walk(self):
        walk = list()
        self._preorder_walk(self._root,  walk)
        return walk

    def _preorder_walk(self, node, walk):
        if node is None:
            return
        walk.append(node.key)
        self._preorder_walk(node.left, walk)
        self._preorder_walk(node.right, walk)

        return walk

    def _smallest(self, node):
        if node.left is None:
            return node
        return self._smallest(node.left)

    def smallest(self):
        node = self._smallest(self._root)
        return (node.key, node.value)

    def _largest(self, node):
        if node.right is None:
            return node
        return self._largest(node.right)

    def largest(self):
        node = self._largest(self._root)
        return (node.key, node.value)

    def remove(self, key):
        node = self._search(key, self._root)

        if node is not None:
            right = node.right
            left = node.left
            if left and right:
                largest = self._largest(left)
                node.replace_with(largest)
                self._size -= 1
                return True
            node.replace_with(left if left else right)
            self._size -= 1
            return True
        return False

    def size(self):
        return self._size
