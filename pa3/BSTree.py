import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None
    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        if self.root is None:
            return
        current = self.root
        stack = []
        ans = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left_child
            current = stack.pop()
            ans.append(current.value)
            current = current.right_child
        
        print((" ").join(str(i) for i in ans) + " ", file=output)

    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        if self.root is None:
            return
        current = self.root
        stack = []
        ans = []
        stack.append(current)
        while stack:
            current = stack.pop()
            if current.right_child is not None:
                stack.append(current.right_child)
            if current.left_child is not None:
                stack.append(current.left_child) 
            ans.append(current.value)      
        
        print((" ").join(str(i) for i in ans) + " ", file=output) 

    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        if self.root is None:
            return
        current = self.root
        stack = []
        ans = []
        stack.append(current)
        while stack:
            current = stack.pop()
            ans.append(current.value)
            if current.left_child is not None:
                stack.append(current.left_child)
            if current.right_child is not None:
                stack.append(current.right_child)

   
        ans.reverse()      
        
        print((" ").join(str(i) for i in ans) + " ", file=output)

    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        if self.root is None:
            return
        current = self.root
        while True:
            if current.right_child is None:
                break
            else:
                current = current.right_child

        print(str(current.value), file=output)

    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        current = self.root
        while True:
            if current.left_child is None:
                break
            else:
                current = current.left_child

        print(str(current.value), file=output)

    def insert(self, key):          # insert one node
        # TODO
        new = Node(key)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                if new.value < current.value:
                    if current.left_child is not None:
                        current = current.left_child
                    else:
                        current.left_child = new
                        break

                elif new.value > current.value:
                    if current.right_child is not None:
                        current = current.right_child
                    else:
                        current.right_child = new
                        break             
                  
    def delete(self, key):          # delete one node
        # TODO
        def deleteNode(root, key):
            if root is None:
                return root

            if root.value == key:
                if root.left_child is None and root.right_child is None:
                    return None
                elif root.right_child is None: 
                    return root.left_child
                elif root.left_child is None:
                    return root.right_child
                else:
                    rSecessor = root.right_child
                    while rSecessor.left_child is not None:
                        rSecessor = rSecessor.left_child
                    root.value = rSecessor.value
                    root.right_child = deleteNode(root.right_child, root.value)
                    return root

            elif root.value < key:
                root.right_child = deleteNode(root.right_child, key)
                return root

            elif root.value > key:
                root.left_child = deleteNode(root.left_child, key)
                return root

        self.root = deleteNode(self.root, key)


    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        if self.root is None:
            return
        current = self.root
        queue = []
        lev = 0
        queue.append(current)

        while queue:
            size = len(queue)
            while size > 0:
                current = queue.pop(0)
                if current.left_child is not None:
                    queue.append(current.left_child)
                if current.right_child is not None:
                    queue.append(current.right_child) 

                size -= 1
            lev += 1
        lev -= 1    
        print(str(lev), file=output)   

    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        # TODO
        if self.root is None:
            return
        current = self.root
        ans = []
        queue = []
        queue.append(current)
        while len(queue):
            current = queue.pop(0)
            check = False
            if current.left_child is not None:
                check = True
                queue.append(current.left_child)
            if current.right_child is not None:
                check = True
                queue.append(current.right_child)

            if check:
                ans.append(current.value)
        ans.sort()
        print((" ").join(str(i) for i in ans) + " ", file=output) 

    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        if self.root is None:
            return
        current = self.root
        stack = []
        ans = []
        stack.append(current)
        while stack:
            current = stack.pop()
            if current.right_child is not None:
                stack.append(current.right_child)

            if current.left_child is not None:
                stack.append(current.left_child) 

            if current.right_child is None and current.left_child is None:
                ans.append(current.value)        
        print((" ").join(str(i) for i in ans) + " ", file=output) 

    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)

    

