class TreeNode:
    
    def __init__(self, key, val, left_child = None, right_child = None, parent = None):
        self.key = key
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
    
    def has_left_child(self):
        return bool(self.left_child)

    def is_left_child(self):
        return bool(self == self.parent.left_child)

    def is_right_child(self):
        return bool(self == self.parent.right_child)

    def has_right_child(self):
        return bool(self.right_child)

    def _iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def isLeaf():
        return self.parent
    
    def has_one_child(self):
        return bool((self.left_child and not self.right_child) or (self.right_child and not self.left_child))
    
    def replace_node_data(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right


class BinarySearchTree:
    
    def __init__(self):
        
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
        # return self.__iter__(self)

    def put(self, key, val):
        
        if self.root:
            self.root = TreeNode(key, val)
            self._put(key, val, self.root)
        else:
            cur_node = TreeNode(key, val)
            self._put(key, val, cur_node)

    def _put(self, key, val, cur_node):

        if key == cur_node.key:
            cur_node.val = val
        elif key < cur_node.key:
            if cur_node.left_child:
                cur_node.left_child = TreeNode(key, val, parent = cur_node)
            else:
                if cur_node.right_child:
                    self._put(key, val, cur_node.right_child)
                else:
                    cur_node.right_child = TreeNode(key, val, parent = cur_node)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
            else:
                return None
        else:
            return None

    def _get(self, key, cur_node):
        if not cur_node:
            return None
        elif key == cur_node.key:
            return cur_node
        else:
            if key < cur_node.key:
                return self._get(key, cur_node.left_child)
            else:
                return self._get(key, cur_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self.get(key))

    def __delitem__(key):
        # check if it is a leaf
        cur_node = self.get(key)
        if cur_node.isLeaf():
            if cur_node.parent.left_child == cur_node:
                cur_node.parent.left_child = None
            elif cur_node.parent.right_child == cur_node:
                cur_node.parent.right_child = None

        # check if it is 1 child
        elif cur_node.has_one_child:
            if cur_node.has_left_child():
                if cur_node.is_left_child():
                    cur_node.left_child.parent = cur_node.parent
                    cur_node.parent.left_child = cur_node.left_child
                elif cur_node.is_right_child():
                    cur_node.right_child.parent = cur_node.parent
                    cur_node.parent.right_child = cur_node.left_child
                else:
                    cur_node.replace_node_data(cur_node.left_child.key, cur_node.left_child.value,
                    cur_node.left_child.left_child, cur_node.left_child.right_child)
            else:
                if cur_node.is_right_child():
                    cur_node.right_child.parent = cur_node.parent
                    cur_node.parent.right_child = cur_node.parent
                elif cur_node.is_left_child():
                    cur_node.right_child.parent = cur_node.parent
                    cur_node.parent.lef_child = cur_node.right_child
                else:
                    cur_node.replace_node_data(cur_node.right_child.key, cur_node.right_child.value,
                    cur_node.right_child.left_child, cur_node.right_child.right_child)

        else:
            s = self.successor(key)
            cur_node.key = s.key
            cur_node.val = s.val
            self.__delitem__(s.key)

        # check if it is 2 child

    def succesor(self, key):
        cur_node = self.get(key)
        if cur_node.has_right_child():
            cur_node = cur_node.right_child
        
            while cur_node.has_left_child():
                cur_node = cur_node.left_child

        return cur_node

    def __contains__(key):
        pass

    

b = BinarySearchTree()
b.put(15, 0)
b.put(7, 0)
b.put(27, 0)
b.put(3, 0)
b.put(8, 0)
b.put(18, 0)
b.put(33, 0)
b.put(1, 0)
b.put(5, 0)
b.put(10, 0)


#print(b.root.key)
print(b.get(15))