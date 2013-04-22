def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def set_deep_left(tree,newBranch):
    tree1 = tree[1]
    while True:
        if len(tree1) != None:
            tree1 = tree[1]
        else:
            insertLeft(tree1,newBranch)
            break

    print tree
            
        
