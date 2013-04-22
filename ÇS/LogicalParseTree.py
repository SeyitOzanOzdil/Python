class Stack :
    def __init__(self):
        self.items = []
    def push (self,item):
        return self.items.append(item)
    def isEmpty (self):
        return self.items == []
    def pop (self):
        return self.items.pop()
    def peek (self):
        return self.items[len(self.items)-1]

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newranch],t,[])
    else:
        root.insert(1,[newBranch],[],[])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newranch],t,[])
    else:
        root.insert(1,[newBranch],[],[])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == "(":
            currentTree.insertLeft(currentTree,'')
            pStack.push(currentTree)
            currentTree = getLeftChild(currentTree)
        elif i not in '+*)':
            setRootVal(currentTree, i)
            parent = pStack.pop()
            currentTree = parent
        elif i in "+*":
            setRootVal(currentTree,i)
            currentTree.insertRight(currentTree,'')
            pStack.push(currentTree)
            currentTree = getRightChild(currentTree)
        elif i == ')':
            currentTree = pStack.pop()
        else:
            print "error: I don’t recognize " + i

    return eTree
