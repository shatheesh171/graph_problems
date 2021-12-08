#Given a BST, design a algo which creates a LL of all nodes at each depth 
#(ie, if tree of depth D then D LLs)
#Solution is implemented with pre-order traversal instead of level order traversal. Think the space
#complexity with Queue is avoided.A dictonary with depth as key is taken and linked list as value,
#its appended as we traverse through diff levels

class LinkedList:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None

    def add(self,val):
        if self.next==None:
            self.next=LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self) -> str:
        return "({val})".format(val=self.val)+str(self.next)

class BinaryTree:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

def depth(tree):
    if tree==None:
        return 0
    if tree.left==None and tree.right==None:
        return 1
    else:
        depthLeft=1+depth(tree.left)
        depthRight=1+depth(tree.right)
        if depthLeft>depthRight:
            return depthLeft
        else:
            return depthRight

def treeToLinkedList(tree,custDict={},d=None):
    if d==None:
        d=depth(tree)
    if custDict.get(d)==None:
        custDict[d]=LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d==1:
            return custDict
    if tree.left!=None:
        custDict=treeToLinkedList(tree.left,custDict,d-1)
    if tree.right!=None:
        custDict=treeToLinkedList(tree.right,custDict,d-1)
    return custDict

mainTree=BinaryTree(1)
two=BinaryTree(2)
three=BinaryTree(3)
four=BinaryTree(4)
five=BinaryTree(5)
six=BinaryTree(6)
seven=BinaryTree(7)
mainTree.left=two
mainTree.right=three
two.left=four
two.right=five
two.left=six
two.right=seven

custDict=treeToLinkedList(mainTree)
for depthLevel,linkedList in custDict.items():
    print("{0} {1}".format(depthLevel,linkedList))