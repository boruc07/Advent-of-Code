import anytree as at
import re


# Input text
with open("day7/input.txt", 'rt') as f:
    input_string = f.readlines()


class TreeWrapper:
    def __init__(self):
        self.tree_dict = {"/root":  at.Node("root", parent=None, children=None, isDir=True, size=0)}
        self.current_dir = self.tree_dict["/root"]
        self.ls_flag = False

    def addNode(self, node_name: str = None, parent: at.Node = None, isDir: str = None, size: int = None) -> None:
        node = at.Node(node_name, parent=parent, children=None, isDir=isDir, size=size)
        self.tree_dict[self.getPath(node)] = node
        # print(f"Added node: {node} as path: {self.getPath(node)}")

    def getPath(self, node: at.Node = None) -> str:
        return node.separator.join([""] + [str(parent.name) for parent in node.path])

    def getPathForCurrDir(self, node_name: str = None):

        output = self.current_dir.separator.join([""] + [str(node.name) for node in self.current_dir.path])
        return output + self.current_dir.separator[0] + node_name

    def getParent(self, node: at.Node = None):
        # In case it's already root then return root as a parent
        return self.tree_dict[self.getPath(node)].parent if node.is_root is False else node

    def setCurrentDir(self, action: str = None, node_name: str = None) -> None:
        if action == "..":  # Go one up
            self.current_dir = self.current_dir.parent if self.current_dir.is_root is False else self.current_dir
        elif action == "/":  # Go to root
            self.current_dir = self.current_dir.root
        else:
            # In order to set it as new current dir check if it exists in current directory
            for children in self.tree_dict[self.getPath(self.current_dir)].children:
                if children.name == node_name and children.isDir is True:
                    self.current_dir = children
        self.ls_flag = False

    def executeLine(self, line: str = None) -> None:
        if line[0:7] == "$ cd ..":
            # Parent of current directory is set as new current directory
            self.setCurrentDir("..")

        elif line[0:6] == "$ cd /":
            self.setCurrentDir("/")

        elif re.search(r"(\$ cd )(.+)", line):
            command = re.search(r"(\$ cd )(.+)", line)
            dir_name = command.group(2)
            self.setCurrentDir(None, dir_name)

        elif line[0:4] == "$ ls":
            # Start lisitng mode, it will last until another $ command occurs
            self.ls_flag = True

        elif self.ls_flag is True:
            # Add files and dirs
            line = line.replace("\n", "")
            p1, p2 = line.split(" ")
            if p1 == "dir":
                self.addNode(p2, parent=self.current_dir, isDir=True, size=0)
            else:  # If not dir then file
                self.addNode(p2, parent=self.current_dir, isDir=False, size=int(p1))

    def updateParentDirectorySize(self):
        # Propagate size of every file to every parent up to root directory
        for node in at.PreOrderIter(self.current_dir.root, filter_=lambda n: n.size > 0 and n.isDir is False):
            temp_parent = node.parent
            while temp_parent:
                temp_parent.size += int(node.size)
                temp_parent = temp_parent.parent


# Initialize Tree
treewrapper = TreeWrapper()
for curr_line in input_string:
    treewrapper.executeLine(curr_line)

treewrapper.updateParentDirectorySize()

# Render tree
for pre, fill, node in at.RenderTree(treewrapper.current_dir.root):
    print("%s%s %s" % (pre, node.name, node.size))

# Calculate files size for defined threshold
threshold = 100000
global_sum_size = 0
for node in at.PreOrderIter(treewrapper.current_dir.root, filter_=lambda n: (n.size <= threshold and n.isDir is True)):
    global_sum_size += node.size
print(global_sum_size)
