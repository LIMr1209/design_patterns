class Node:
    """节点类"""
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

# 深度遍历而言还有三种方式：先序遍历/中序遍历/后序遍历
# 广度遍历
class Tree:
    """树类"""
    def __init__(self, root=None):
        self._root = root

    def add(self, item):
        node = Node(item)
        if not self._root:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
                queue.append(cur.lchild)

    def preorder(self, root):
        """
        先序遍历-递归实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """
        中序遍历-递归实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        """
        后序遍历-递归实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    def breadth_travel(self, root):
        """
        广度遍历
        广度优先-队列实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            elif node.rchild:
                queue.append(node.rchild)