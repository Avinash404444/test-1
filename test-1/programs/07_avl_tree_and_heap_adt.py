class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        temp = x.right
        x.right = y
        y.left = temp
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left
        y.left = x
        x.right = temp
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, data):
        if root is None:
            return AVLNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def display(self):
        print(self.heap)


avl = AVLTree()
root = None
for value in [30, 20, 10, 25, 40, 50]:
    root = avl.insert(root, value)
print("AVL Tree - Inorder Traversal:")
avl.inorder(root)

heap = MaxHeap()
for value in [50, 30, 40, 10, 20, 35]:
    heap.insert(value)
print("\n\nMax Heap:")
heap.display()
